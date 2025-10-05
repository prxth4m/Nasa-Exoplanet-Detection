# 🚀 Step-by-Step Deployment Guide

Follow these exact steps to deploy your app!

---

## PART 1: Create GitHub Repository (5 minutes)

### Step 1: Create Repository on GitHub
1. Open your browser and go to: https://github.com/new
2. Fill in the details:
   - **Repository name**: `nasa-exoplanet-detection` (or your choice)
   - **Description**: `AI-powered exoplanet detection using NASA mission data`
   - **Visibility**: ✅ Public (recommended) or Private
   - **DO NOT** check "Initialize with README" (we already have one)
3. Click **"Create repository"**

### Step 2: Copy the Commands
After creating the repo, GitHub will show you commands. **IGNORE THEM** and use these instead:

Open PowerShell in VS Code and run:

```powershell
cd "c:\Users\prath\OneDrive\Documents\NASA-SPACE APP"

# Set your GitHub username (replace YOUR_USERNAME)
git remote add origin https://github.com/YOUR_USERNAME/nasa-exoplanet-detection.git

# Push to GitHub
git branch -M main
git push -u origin main
```

**Replace `YOUR_USERNAME` with your actual GitHub username!**

If it asks for credentials:
- Username: your GitHub username
- Password: use a **Personal Access Token** (not your password)
  - Get token at: https://github.com/settings/tokens
  - Click "Generate new token (classic)"
  - Select scopes: `repo` (all checkboxes under repo)
  - Copy and save the token (you'll use it as password)

---

## PART 2: Deploy Backend to Render (10 minutes)

### Step 3: Deploy Backend

1. **Open Render**: https://dashboard.render.com/
2. **Sign in** with your GitHub account
3. Click **"New +"** button (top right)
4. Select **"Web Service"**
5. Click **"Connect a repository"** (if first time)
   - Authorize Render to access your GitHub
6. Find and select **`nasa-exoplanet-detection`** repository
7. Click **"Connect"**

### Step 4: Configure Backend Service

Fill in these settings:

- **Name**: `exoplanet-api` (or your choice)
- **Region**: Choose closest to you
- **Branch**: `main`
- **Root Directory**: `backend` ← **IMPORTANT!**
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --threads 2 --timeout 120`

### Step 5: Choose Plan
- **Instance Type**: Select **"Free"** (for testing)
  - Note: Free tier sleeps after 15 min inactivity
  - First request after sleep takes ~30-60 seconds

### Step 6: Deploy!
1. Click **"Create Web Service"** (bottom of page)
2. Wait 5-10 minutes for deployment
3. Watch the logs - should see "BUILD SUCCESSFUL" then "DEPLOY SUCCESSFUL"
4. **COPY YOUR BACKEND URL** - It will look like:
   ```
   https://exoplanet-api-xxxx.onrender.com
   ```
   
**SAVE THIS URL! You'll need it for the frontend!**

---

## PART 3: Update Frontend Configuration (2 minutes)

### Step 7: Update Environment File

1. In VS Code, open: `frontend/.env.production`
2. Replace the content with your actual backend URL:
   ```env
   VITE_API_URL=https://exoplanet-api-xxxx.onrender.com
   ```
   **Use YOUR actual Render URL from Step 6!**

3. Save the file

### Step 8: Push Updated Configuration

Run in PowerShell:
```powershell
cd "c:\Users\prath\OneDrive\Documents\NASA-SPACE APP"
git add frontend/.env.production
git commit -m "Update production API URL"
git push
```

---

## PART 4: Deploy Frontend to Vercel (5 minutes)

### Step 9: Deploy Frontend

1. **Open Vercel**: https://vercel.com/dashboard
2. **Sign in** with your GitHub account
3. Click **"Add New..."** button (top right)
4. Select **"Project"**
5. Click **"Import Git Repository"**
6. Find and select **`nasa-exoplanet-detection`**
7. Click **"Import"**

### Step 10: Configure Frontend

Vercel should auto-detect Vite, but verify these settings:

- **Project Name**: `nasa-exoplanet-detection` (or your choice)
- **Framework Preset**: `Vite` ← Should auto-detect
- **Root Directory**: Click **"Edit"** → Select **`frontend`** ← **IMPORTANT!**
- **Build Command**: `npm run build` (default is fine)
- **Output Directory**: `dist` (default is fine)
- **Install Command**: `npm install` (default is fine)

### Step 11: Add Environment Variable

1. Click **"Environment Variables"** (expand if needed)
2. Add this variable:
   - **Name**: `VITE_API_URL`
   - **Value**: `https://exoplanet-api-xxxx.onrender.com` (YOUR backend URL)
   - **Environments**: Check all ✅ Production ✅ Preview ✅ Development
3. Click **"Add"**

### Step 12: Deploy!

1. Click **"Deploy"** button
2. Wait 1-3 minutes
3. You'll see "Building..." then "Deploying..." then "Success! 🎉"
4. Click **"Visit"** to open your live app!

Your frontend URL will be:
```
https://nasa-exoplanet-detection.vercel.app
```

---

## ✅ VERIFY YOUR DEPLOYMENT

### Test Your Live App:

1. **Visit your Vercel URL**
2. **Test the Data Explorer** - Should load exoplanet data
3. **Test AI Classifier** - Try manual prediction
4. **Test Lightcurve Upload** - Upload a sample file from `public/data/`

### Check for Issues:

**If you see errors:**
1. Open browser Console (F12 → Console tab)
2. Look for error messages
3. Check if API URL is correct

**Common Issues:**

❌ **"Failed to fetch"** → Backend might be waking up (wait 30-60 seconds)
❌ **CORS error** → Check backend logs on Render
❌ **404 on routes** → Vercel routing is configured (vercel.json exists)

---

## 🎉 YOU'RE DONE!

Your app is now live at:
- **Frontend**: https://nasa-exoplanet-detection.vercel.app
- **Backend**: https://exoplanet-api-xxxx.onrender.com

### Share Your URLs!

Fill this in and save:
```
Frontend: _________________________________
Backend:  _________________________________
GitHub:   https://github.com/YOUR_USERNAME/nasa-exoplanet-detection
```

---

## 🔄 Future Updates

When you make changes:

1. Commit and push:
   ```powershell
   git add .
   git commit -m "Your change description"
   git push
   ```

2. **Automatic deployment**:
   - Render will auto-deploy backend
   - Vercel will auto-deploy frontend

No manual steps needed! 🚀

---

## 🆘 Need Help?

- **Render Logs**: https://dashboard.render.com → Your Service → Logs
- **Vercel Logs**: https://vercel.com/dashboard → Your Project → Deployments
- **GitHub Issues**: Create an issue in your repo

---

**Good luck! 🌌**
