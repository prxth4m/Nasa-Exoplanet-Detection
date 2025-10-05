# Planopticon Backend

Flask API server for exoplanet classification using machine learning models.

## Features
- RandomForest model for tabular exoplanet data classification
- CNN model for lightcurve time-series analysis
- Batch processing support
- CORS enabled for frontend integration

## Setup

### Local Development
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
```

Server runs on http://localhost:5000

## API Endpoints

### Health Check
- `GET /api/health` - Server status

### Classification
- `POST /api/predict` - Classify single exoplanet (tabular data)
- `POST /api/predict/batch` - Batch classification (CSV upload)
- `POST /api/predict/lightcurve` - Lightcurve classification (CNN model)
- `POST /api/predict/lightcurve/batch` - Batch lightcurve classification

## Models
- `exoplanet_model.pkl` - RandomForest classifier (74% accuracy)
- `exoplanet_model.h5` - CNN model for lightcurve analysis
- `scaler.pkl` - Feature scaler for tabular data

## Deployment
Configured for Render/Railway with Procfile and gunicorn.
