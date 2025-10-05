from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
import numpy as np
import os
from scipy.ndimage import gaussian_filter
from scipy.fftpack import fft

app = Flask(__name__)
CORS(app)

# Load table-based model and scaler (RandomForest)
table_model = joblib.load('exoplanet_model.pkl')
table_scaler = joblib.load('scaler.pkl')
feature_columns = ['period','duration','depth','radius','insolation','eq_temp','st_teff','st_rad','st_mass']

# Load CNN model for lightcurve analysis (if available)
cnn_model = None
try:
    import tensorflow as tf
    if os.path.exists('exoplanet_cnn_model.h5'):
        cnn_model = tf.keras.models.load_model('exoplanet_cnn_model.h5')
        print("✓ CNN model loaded successfully")
    elif os.path.exists('exoplanet_model.h5'):
        cnn_model = tf.keras.models.load_model('exoplanet_model.h5')
        print("✓ CNN model loaded successfully")
except Exception as e:
    print(f"Warning: CNN model not loaded: {e}")

label_map = {0: 'FALSE POSITIVE', 1: 'CANDIDATE', 2: 'CONFIRMED'}

def preprocess_input_df(df, feature_cols):
    # Add missing columns with 0
    for col in feature_cols:
        if col not in df.columns:
            df[col] = 0
    # Drop extra columns
    df = df[feature_cols]
    return df


@app.route('/', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'service': 'Exoplanet Detection API',
        'cnn_model_loaded': cnn_model is not None
    })


@app.route('/api/predict', methods=['POST'])
def predict():
    """Table-based prediction using planet parameters (backward compatible)"""
    try:
        if 'file' in request.files:
            file = request.files['file']
            df = pd.read_csv(file, comment='#')
            X = preprocess_input_df(df, feature_columns)
            X_scaled = table_scaler.transform(X)
            preds = table_model.predict(X_scaled)
            prob = table_model.predict_proba(X_scaled) if hasattr(table_model, 'predict_proba') else None

            out = df.copy()
            out['prediction'] = [label_map[p] for p in preds]
            if prob is not None:
                for i in range(prob.shape[1]):
                    out[f'prob_{i}'] = prob[:, i]
            return out.to_json(orient='records')

        data = request.get_json(force=True)
        df = pd.DataFrame([data])
        X = preprocess_input_df(df, feature_columns)
        X_scaled = table_scaler.transform(X)
        pred = table_model.predict(X_scaled)[0]
        prob = table_model.predict_proba(X_scaled)[0].tolist() if hasattr(table_model, 'predict_proba') else None
        return jsonify({'prediction': label_map[int(pred)], 'prob': prob})

    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/predict/lightcurve', methods=['POST'])
def predict_lightcurve():
    """CNN-based prediction using time-series lightcurve data"""
    if cnn_model is None:
        return jsonify({'error': 'CNN model not available'}), 503
    
    try:
        # Handle file upload
        if 'file' in request.files:
            file = request.files['file']
            filename = file.filename
            
            # Check if it's a CSV file (exoTrain/exoTest format)
            if filename.endswith('.csv'):
                # Read CSV - each row is a complete lightcurve
                df = pd.read_csv(file)
                
                # Check if it has LABEL column (exoTrain/exoTest format)
                if 'LABEL' in df.columns:
                    # Process multiple rows (limit to first 10 for performance)
                    num_samples = min(10, len(df))
                    results = []
                    
                    for i in range(num_samples):
                        flux_values = df.iloc[i, 1:].values.astype(float)
                        original_label = int(df.iloc[i, 0])
                        
                        # Apply preprocessing
                        flux_normalized = (flux_values - np.mean(flux_values)) / (np.std(flux_values) + 1e-8)
                        flux_gaussian = gaussian_filter(flux_normalized, sigma=7.0)
                        flux_fft = np.abs(fft(flux_gaussian))
                        
                        target_length = 3197
                        if len(flux_fft) < target_length:
                            flux_padded = np.pad(flux_fft, (0, target_length - len(flux_fft)), mode='constant')
                        else:
                            flux_padded = flux_fft[:target_length]
                        
                        X = flux_padded.reshape(1, target_length, 1)
                        prediction = cnn_model.predict(X, verbose=0)
                        prob_exoplanet = float(prediction[0][0])
                        
                        results.append({
                            'filename': f"{filename} - Row {i+1}",
                            'prediction': 'CONFIRMED' if prob_exoplanet > 0.5 else 'FALSE POSITIVE',
                            'probability': prob_exoplanet,
                            'confidence': abs(prob_exoplanet - 0.5) * 2,
                            'data_points': len(flux_values),
                            'original_label': 'EXOPLANET' if original_label == 2 else 'NO EXOPLANET'
                        })
                    
                    return jsonify(results)
                else:
                    # Try to read as regular flux data
                    flux_values = df.iloc[:, 1].values if df.shape[1] > 1 else df.iloc[:, 0].values
                    original_label = None
            else:
                # Read as text file (TIME FLUX FLUX_ERR format)
                text = file.read().decode('utf-8')
                lines = text.strip().split('\n')
                lines = [line for line in lines if line.strip() and not line.startswith('#')]
                
                flux_values = []
                for line in lines:
                    parts = line.split()
                    if len(parts) >= 2:
                        try:
                            flux = float(parts[1])  # Second column is FLUX
                            flux_values.append(flux)
                        except ValueError:
                            continue
                
                flux_values = np.array(flux_values)
                original_label = None
        else:
            data = request.get_json(force=True)
            if 'lightcurve' not in data:
                return jsonify({'error': 'Missing lightcurve data'}), 400
            
            # Parse JSON lightcurve data
            text = data['lightcurve']
            lines = text.strip().split('\n')
            lines = [line for line in lines if line.strip() and not line.startswith('#')]
            
            flux_values = []
            for line in lines:
                parts = line.split()
                if len(parts) >= 2:
                    try:
                        flux = float(parts[1])
                        flux_values.append(flux)
                    except ValueError:
                        continue
            
            flux_values = np.array(flux_values)
            original_label = None
        
        if len(flux_values) == 0:
            return jsonify({'error': 'No valid flux data found'}), 400
        
        # Apply the same preprocessing as training:
        # 1. Normalize
        flux_normalized = (flux_values - np.mean(flux_values)) / (np.std(flux_values) + 1e-8)
        
        # 2. Apply Gaussian filter (sigma=7.0 as in training)
        flux_gaussian = gaussian_filter(flux_normalized, sigma=7.0)
        
        # 3. Apply FFT (as in training)
        flux_fft = np.abs(fft(flux_gaussian))
        
        # 4. Pad or truncate to expected length
        target_length = 3197
        if len(flux_fft) < target_length:
            flux_padded = np.pad(flux_fft, (0, target_length - len(flux_fft)), mode='constant')
        else:
            flux_padded = flux_fft[:target_length]
        
        # 5. Reshape for CNN input (batch_size, sequence_length, features)
        X = flux_padded.reshape(1, target_length, 1)
        
        # Predict
        prediction = cnn_model.predict(X, verbose=0)
        prob_exoplanet = float(prediction[0][0])
        
        result = {
            'prediction': 'CONFIRMED' if prob_exoplanet > 0.5 else 'FALSE POSITIVE',
            'probability': prob_exoplanet,
            'confidence': abs(prob_exoplanet - 0.5) * 2,  # 0 to 1 scale
            'data_points': len(flux_values)
        }
        
        # Add original label if available (for verification)
        if original_label is not None:
            result['original_label'] = 'EXOPLANET' if original_label == 2 else 'NO EXOPLANET'
        
        return jsonify(result)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/predict/lightcurve/batch', methods=['POST'])
def predict_lightcurve_batch():
    """Batch CNN-based prediction for multiple lightcurve files"""
    if cnn_model is None:
        return jsonify({'error': 'CNN model not available'}), 503
    
    try:
        # Check if files were uploaded
        if not request.files:
            return jsonify({'error': 'No files uploaded'}), 400
        
        results = []
        files = request.files.getlist('files')  # Get all files from the 'files' field
        
        if not files or len(files) == 0:
            return jsonify({'error': 'No files in request'}), 400
        
        for file in files:
            try:
                filename = file.filename
                
                # Check if it's a CSV file (exoTrain/exoTest format)
                if filename.endswith('.csv'):
                    # Read CSV - each row is a complete lightcurve
                    df = pd.read_csv(file)
                    
                    # Check if it has LABEL column (exoTrain/exoTest format)
                    if 'LABEL' in df.columns:
                        # Process first row only (for batch, we process one row per file)
                        flux_values = df.iloc[0, 1:].values.astype(float)
                        original_label = int(df.iloc[0, 0])
                    else:
                        # Try to read as regular flux data
                        flux_values = df.iloc[:, 1].values if df.shape[1] > 1 else df.iloc[:, 0].values
                        original_label = None
                else:
                    # Read as text file (TIME FLUX FLUX_ERR format)
                    text = file.read().decode('utf-8')
                    lines = text.strip().split('\n')
                    lines = [line for line in lines if line.strip() and not line.startswith('#')]
                    
                    flux_values = []
                    for line in lines:
                        # Try different delimiters (whitespace, comma, tab)
                        parts = line.replace(',', ' ').replace('\t', ' ').split()
                        if len(parts) >= 2:
                            try:
                                flux = float(parts[1])  # Second column is FLUX
                                flux_values.append(flux)
                            except ValueError:
                                continue
                    
                    flux_values = np.array(flux_values)
                    original_label = None
                
                if len(flux_values) == 0:
                    results.append({
                        'filename': filename,
                        'error': 'No valid flux data found',
                        'prediction': 'ERROR',
                        'probability': 0,
                        'confidence': 0,
                        'data_points': 0
                    })
                    continue
                
                # Apply the same preprocessing as training:
                # 1. Normalize
                flux_normalized = (flux_values - np.mean(flux_values)) / (np.std(flux_values) + 1e-8)
                
                # 2. Apply Gaussian filter (sigma=7.0 as in training)
                flux_gaussian = gaussian_filter(flux_normalized, sigma=7.0)
                
                # 3. Apply FFT (as in training)
                flux_fft = np.abs(fft(flux_gaussian))
                
                # 4. Pad or truncate to expected length
                target_length = 3197
                if len(flux_fft) < target_length:
                    flux_padded = np.pad(flux_fft, (0, target_length - len(flux_fft)), mode='constant')
                else:
                    flux_padded = flux_fft[:target_length]
                
                # 5. Reshape for CNN input
                X = flux_padded.reshape(1, target_length, 1)
                
                # Predict
                prediction = cnn_model.predict(X, verbose=0)
                prob_exoplanet = float(prediction[0][0])
                
                result = {
                    'filename': filename,
                    'prediction': 'CONFIRMED' if prob_exoplanet > 0.5 else 'FALSE POSITIVE',
                    'probability': prob_exoplanet,
                    'confidence': abs(prob_exoplanet - 0.5) * 2,
                    'data_points': len(flux_values)
                }
                
                # Add original label if available (for verification)
                if original_label is not None:
                    result['original_label'] = 'EXOPLANET' if original_label == 2 else 'NO EXOPLANET'
                
                results.append(result)
                
            except Exception as e:
                results.append({
                    'filename': file.filename,
                    'error': str(e),
                    'prediction': 'ERROR',
                    'probability': 0,
                    'confidence': 0,
                    'data_points': 0
                })
        
        return jsonify(results)
    
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'models': {
            'table_model': 'loaded',
            'cnn_model': 'loaded' if cnn_model is not None else 'not available'
        }
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)