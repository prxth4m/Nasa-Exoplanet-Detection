# ✅ Deployment Checklist - Follow Along!

## ☑️ PART 1: GitHub (5 minutes)
- [ ] Go to https://github.com/new
- [ ] Create repository: `nasa-exoplanet-detection`
- [ ] Copy your GitHub username: __________________
- [ ] Run these commands (replace YOUR_USERNAME):
  ```powershell
  cd "c:\Users\prath\OneDrive\Documents\NASA-SPACE APP"
  git remote add origin https://github.com/YOUR_USERNAME/nasa-exoplanet-detection.git
  git branch -M main
  git push -u origin main
  ```
- [ ] ✅ Code is on GitHub!

---

## ☑️ PART 2: Render Backend (10 minutes)
- [ ] Go to https://dashboard.render.com/
- [ ] Click "New +" → "Web Service"
- [ ] Connect your GitHub repository
- [ ] Root Directory: `backend`
- [ ] Build: `pip install -r requirements.txt`
- [ ] Start: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --threads 2 --timeout 120`
- [ ] Instance Type: Free
- [ ] Click "Create Web Service"
- [ ] Wait for deployment (5-10 min)
- [ ] Copy backend URL: __________________________________
- [ ] ✅ Backend is live!

---

## ☑️ PART 3: Update Frontend (2 minutes)
- [ ] Open `frontend/.env.production` in VS Code
- [ ] Paste your backend URL:
  ```
  VITE_API_URL=https://your-backend-url.onrender.com
  ```
- [ ] Save file
- [ ] Run these commands:
  ```powershell
  cd "c:\Users\prath\OneDrive\Documents\NASA-SPACE APP"
  git add frontend/.env.production
  git commit -m "Update production API URL"
  git push
  ```
- [ ] ✅ Configuration updated!

---

## ☑️ PART 4: Vercel Frontend (5 minutes)
- [ ] Go to https://vercel.com/dashboard
- [ ] Click "Add New..." → "Project"
- [ ] Import your GitHub repository
- [ ] Root Directory: `frontend`
- [ ] Add Environment Variable:
  - Name: `VITE_API_URL`
  - Value: (your backend URL)
- [ ] Click "Deploy"
- [ ] Wait for deployment (1-3 min)
- [ ] Copy frontend URL: __________________________________
- [ ] ✅ Frontend is live!

---

## ☑️ PART 5: Test (3 minutes)
- [ ] Visit your frontend URL
- [ ] Test Data Explorer
- [ ] Test AI Classifier
- [ ] Test Lightcurve Upload
- [ ] ✅ Everything works!

---

## 🎉 DONE!

**My Live URLs:**
- Frontend: ___________________________________
- Backend: ___________________________________
- GitHub: https://github.com/_______________/nasa-exoplanet-detection

**Total Time**: ~25 minutes

---

**Detailed instructions**: See `STEP_BY_STEP_DEPLOY.md`
