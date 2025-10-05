# 🌌 Planopticon - Exoplanet Classification Platform

AI-powered web application for exploring and classifying exoplanets using NASA mission data (Kepler, K2, TESS).

## 📁 Project Structure

```
organized-project/
├── frontend/          # React + TypeScript + Vite
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── hooks/
│   │   └── lib/
│   ├── public/
│   │   └── data/     # CSV catalogs
│   └── package.json
│
└── backend/          # Flask API + ML Models
    ├── app.py
    ├── exoplanet_model.h5      # CNN model
    ├── exoplanet_model.pkl     # RandomForest model
    ├── scaler.pkl
    └── requirements.txt
```

## 🚀 Features

### 1. Data Explorer
- Browse 5000+ exoplanets from Kepler, K2, and TESS missions
- Advanced filtering (radius, period, temperature)
- Pagination with page jump
- Detailed planet information

### 2. Lightcurve Classifier
- Upload lightcurve CSV files (3,197 flux measurements)
- CNN-based classification
- Batch processing support
- Real-time probability predictions

### 3. AI Classifier
- Classify exoplanets using orbital parameters
- Random Forest model (74% accuracy)
- Single and batch CSV upload
- Manual parameter entry

## 🛠️ Tech Stack

### Frontend
- React 18.3.1
- TypeScript 5.8.3
- Vite 5.4.19
- Tailwind CSS
- shadcn/ui

### Backend
- Flask 3.0.0
- TensorFlow 2.13.0 (CNN model)
- scikit-learn (RandomForest)
- NumPy, Pandas, SciPy

## 📦 Installation

### Prerequisites
- Node.js 18+
- Python 3.11+
- pip

### Frontend Setup
```bash
cd frontend
npm install
cp .env.example .env.local
# Edit .env.local with backend URL
npm run dev
```

### Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## 🌐 Deployment

### Frontend (Vercel)
1. Deploy from GitHub
2. Framework: Vite
3. Add env: `VITE_API_BASE=https://your-backend-url`

### Backend (Render/Railway)
1. Deploy from GitHub
2. Build: `pip install -r requirements.txt`
3. Start: `gunicorn app:app`

See individual README files in `frontend/` and `backend/` for detailed instructions.

## 📊 Data Sources
- [NASA Exoplanet Archive](https://exoplanetarchive.ipac.caltech.edu/)
- Kepler Mission confirmed planets
- K2 Mission extended survey
- TESS All-Sky Survey

## 🤖 Models

### CNN Model (`exoplanet_model.h5`)
- Input: 3,197 flux measurements
- Preprocessing: Gaussian filter + FFT
- Output: Binary classification (EXOPLANET/NOT EXOPLANET)

### Random Forest Model (`exoplanet_model.pkl`)
- Input: Orbital parameters (period, radius, mass, temperature)
- Features: 21,271 training samples
- Accuracy: 74%

## 📝 API Endpoints

- `GET /api/health` - Health check
- `POST /api/predict` - Single prediction (tabular)
- `POST /api/predict/batch` - Batch prediction (CSV)
- `POST /api/predict/lightcurve` - Lightcurve classification
- `POST /api/predict/lightcurve/batch` - Batch lightcurve

## 🎨 Screenshots

### Dashboard
Three main features accessible via tabs with tooltips

### Data Explorer
Filterable table with pagination (10/25/50/100 per page)

### Lightcurve Classifier
Upload CSV, view classification results with confidence scores

### AI Classifier
Manual entry or batch CSV upload for parameter-based classification

## 📄 License
MIT

## 🌐 Deployment

This application is ready for deployment on:
- **Frontend**: Vercel (recommended)
- **Backend**: Render (recommended)

See **[DEPLOYMENT.md](DEPLOYMENT.md)** for complete deployment instructions.

Quick start: **[DEPLOY_QUICK.md](DEPLOY_QUICK.md)**

## 👥 Authors
- **prxth4m** - [GitHub](https://github.com/prxth4m)

## 🙏 Acknowledgments
- NASA Exoplanet Archive
- Kepler, K2, and TESS mission teams
- Open-source community

---

**Note**: This is the organized version of the project. Old folders (`cosmic-classifier-web`, `EXOPLANETS`, `EXOPLANETS 1`) can be safely deleted after verifying this structure works.
