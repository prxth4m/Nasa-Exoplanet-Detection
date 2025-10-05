# 🚀 Deployment Guide

## Overview
This guide will help you deploy your NASA Exoplanet Detection application:
- **Frontend**: Vercel (React/Vite app)
- **Backend**: Render (Flask API)

---

## 📋 Prerequisites
- ✅ GitHub account with this repository pushed
- ✅ Vercel account (connected to GitHub)
- ✅ Render account (connected to GitHub)

---

## 🔧 Backend Deployment (Render)

### Step 1: Deploy to Render

1. **Go to Render Dashboard**: https://dashboard.render.com/
2. **Click "New +"** and select **"Web Service"**
3. **Connect your GitHub repository**
4. **Configure the service**:
   - **Name**: `exoplanet-detection-api` (or your choice)
   - **Root Directory**: `backend`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --threads 2 --timeout 120`
   - **Instance Type**: `Free` (or your choice)

5. **Add Environment Variables** (if needed):
   - Click "Advanced" → "Add Environment Variable"
   - Add any required variables

6. **Click "Create Web Service"**

7. **Wait for deployment** (this may take 5-10 minutes)

8. **Copy your backend URL**: It will be something like:
   ```
   https://exoplanet-detection-api.onrender.com
   ```

### Important Notes:
- ⚠️ Free tier services may spin down after inactivity (takes 30-60s to wake up)
- 📦 The ML models (`exoplanet_model.pkl`, `scaler.pkl`, `exoplanet_model.h5`) must be in the backend directory
- 🔍 Check logs in Render dashboard if deployment fails

---

## 🎨 Frontend Deployment (Vercel)

### Step 1: Update Environment Variables

1. **Edit** `frontend/.env.production`:
   ```env
   VITE_API_URL=https://your-actual-backend-url.onrender.com
   ```
   Replace with your **actual Render backend URL** from above.

2. **Commit and push** this change to GitHub:
   ```bash
   git add frontend/.env.production
   git commit -m "Update production API URL"
   git push
   ```

### Step 2: Deploy to Vercel

1. **Go to Vercel Dashboard**: https://vercel.com/dashboard
2. **Click "Add New..."** → **"Project"**
3. **Import your GitHub repository**
4. **Configure the project**:
   - **Framework Preset**: `Vite`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm run build`
   - **Output Directory**: `dist`
   - **Install Command**: `npm install`

5. **Add Environment Variables**:
   - Click "Environment Variables"
   - Add: `VITE_API_URL` = `https://your-backend-url.onrender.com`
   - Apply to: `Production`, `Preview`, and `Development`

6. **Click "Deploy"**

7. **Wait for deployment** (usually 1-2 minutes)

8. **Your app will be live** at:
   ```
   https://your-project-name.vercel.app
   ```

---

## ✅ Verify Deployment

### Backend Health Check
Visit: `https://your-backend-url.onrender.com/`

You should see the Flask welcome response or API documentation.

### Frontend Check
1. Visit your Vercel URL
2. Try the prediction form
3. Check browser console for any CORS or API errors

---

## 🔍 Troubleshooting

### CORS Errors
If you see CORS errors in the browser console:
- Verify the backend has `flask-cors` installed
- Check that CORS is configured in `app.py`

### API Connection Failed
- Verify the `VITE_API_URL` in Vercel environment variables
- Check Render logs for backend errors
- Ensure backend service is running (not sleeping)

### Build Failures

**Backend (Render)**:
- Check `requirements.txt` has all dependencies
- Review build logs in Render dashboard
- Ensure Python version compatibility

**Frontend (Vercel)**:
- Check `package.json` dependencies
- Review build logs in Vercel dashboard
- Verify environment variables are set

---

## 🔄 Continuous Deployment

Both platforms support automatic deployments:

- **Vercel**: Auto-deploys on every push to main branch
- **Render**: Auto-deploys on every push to main branch

To disable auto-deploy, check the settings in each platform.

---

## 📝 Post-Deployment Checklist

- [ ] Backend deployed successfully on Render
- [ ] Backend URL copied and saved
- [ ] Frontend `.env.production` updated with backend URL
- [ ] Frontend deployed successfully on Vercel
- [ ] Test prediction form works end-to-end
- [ ] Test lightcurve upload functionality
- [ ] Check all features are working
- [ ] Share your deployed URL! 🎉

---

## 🆘 Need Help?

- **Render Docs**: https://render.com/docs
- **Vercel Docs**: https://vercel.com/docs
- **Check deployment logs** in both platforms for error details

---

## 🎯 Quick Commands

### Push to GitHub
```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

### Update Frontend API URL (after backend is deployed)
```bash
# Edit frontend/.env.production with your backend URL
git add frontend/.env.production
git commit -m "Update production API URL"
git push
```

---

Good luck with your deployment! 🚀
