# 🎨 Frontend Deployment on Vercel - Step-by-Step Guide

**Complete guide to deploy your NASA Exoplanet Detection frontend to Vercel**

---

## ⚠️ BEFORE YOU START

Make sure you have:
- ✅ Backend deployed on Render (and you have the URL)
- ✅ Code pushed to GitHub repository
- ✅ Vercel account created and connected to GitHub

**Your Render Backend URL** (copy it here for reference):
```
https://__________________________________.onrender.com
```

---

## 📋 Step-by-Step Instructions

### Step 1: Open Vercel Dashboard

1. Open your browser
2. Go to: **https://vercel.com/dashboard**
3. Sign in with your GitHub account (if not already signed in)

---

### Step 2: Create New Project

1. Look for the **"Add New..."** button (usually top-right corner)
2. Click on it
3. From the dropdown, select **"Project"**

**Screenshot hint:** You should see "Add New..." next to your profile picture

---

### Step 3: Import Git Repository

1. You'll see a page titled **"Import Git Repository"**
2. Look for your repository: **`nasa-exoplanet-detection`**
   - It should appear in the list of your repositories
   - If you don't see it, click **"Adjust GitHub App Permissions"** and grant access
3. Click **"Import"** next to your `nasa-exoplanet-detection` repository

---

### Step 4: Configure Your Project

Now you'll see the **"Configure Project"** page. Fill in these settings:

#### A. Project Name
- **Field:** Project Name
- **Value:** `nasa-exoplanet-detection` (or any name you like)
- **Note:** This will be part of your URL: `your-name.vercel.app`

#### B. Framework Preset
- **Field:** Framework Preset
- **Value:** Should auto-detect as **`Vite`**
- **Action:** Verify it says "Vite" - if not, select it from dropdown

#### C. Root Directory ⚠️ **CRITICAL**
- **Field:** Root Directory
- **Current Value:** `./` (root)
- **Action:** Click **"Edit"** button next to Root Directory
- **New Value:** Select **`frontend`** from the folder list
- **Or type:** `frontend`
- **Why:** Your frontend code is in the `frontend` folder, not root

#### D. Build and Output Settings
These should auto-populate, but verify:
- **Build Command:** `npm run build` ✅ (leave as default)
- **Output Directory:** `dist` ✅ (leave as default)
- **Install Command:** `npm install` ✅ (leave as default)

---

### Step 5: Add Environment Variable ⚠️ **VERY IMPORTANT**

Scroll down to find **"Environment Variables"** section:

1. **Expand the section** if it's collapsed
2. You'll see three input fields:
   - Key/Name
   - Value
   - Environment (checkboxes)

3. **Fill in the variable:**

   **Name/Key:**
   ```
   VITE_API_URL
   ```

   **Value:**
   ```
   https://your-backend-url.onrender.com
   ```
   ⚠️ **Replace with YOUR actual Render backend URL!**
   
   **Example:**
   ```
   https://exoplanet-api-abcd1234.onrender.com
   ```

   **Environments:** Check ALL three boxes:
   - ✅ Production
   - ✅ Preview  
   - ✅ Development

4. **Click "Add"** button

**You should now see:**
```
VITE_API_URL = https://your-backend-url.onrender.com
```

---

### Step 6: Review Configuration

Double-check these settings before deploying:

```
┌─────────────────────────────────────────────────┐
│ Configuration Summary                           │
├─────────────────────────────────────────────────┤
│ Project Name:     nasa-exoplanet-detection      │
│ Framework:        Vite                          │
│ Root Directory:   frontend                      │
│ Build Command:    npm run build                 │
│ Output Directory: dist                          │
│ Environment Var:  VITE_API_URL = [YOUR URL]     │
└─────────────────────────────────────────────────┘
```

Everything looks good? Let's deploy!

---

### Step 7: Deploy! 🚀

1. Click the **"Deploy"** button (big blue/black button at bottom)
2. Vercel will start building your project

**What you'll see:**
```
1. Initializing build...
2. Installing dependencies... (npm install)
3. Building application... (npm run build)
4. Uploading build outputs...
5. Deploying...
```

**Time:** Usually takes 1-3 minutes

---

### Step 8: Wait for Deployment

During deployment, you'll see:
- ✅ Green checkmarks for completed steps
- 🔄 Spinning icons for in-progress steps
- ❌ Red X if something fails

**Status messages you'll see:**
1. "Building..."
2. "Uploading..."
3. "Deploying..."
4. **"Success! 🎉"** ← You want to see this!

---

### Step 9: Access Your Deployed App

Once deployment succeeds:

1. You'll see a **"Visit"** button or preview image
2. Click **"Visit"** or click on the preview
3. Your app will open in a new tab!

**Your URL will be:**
```
https://nasa-exoplanet-detection.vercel.app
```
(or similar, based on your project name)

**SAVE THIS URL!** This is your live app link! 📝

---

### Step 10: Copy Your URLs

Copy both URLs for your records:

```
┌─────────────────────────────────────────────────┐
│ My Live Application URLs                        │
├─────────────────────────────────────────────────┤
│ Frontend (Vercel):                              │
│ https://________________________________.app    │
│                                                 │
│ Backend (Render):                               │
│ https://________________________________.com    │
│                                                 │
│ GitHub Repository:                              │
│ https://github.com/prxth4m/nasa-exoplanet-      │
│ detection                                       │
└─────────────────────────────────────────────────┘
```

---

## ✅ Step 11: Test Your Deployed App

Now test that everything works:

### Test 1: Open the App
- ✅ App loads without errors
- ✅ You see the NASA Exoplanet Detection interface

### Test 2: Data Explorer
1. Click on **"Data Explorer"** tab
2. Check if exoplanet data loads
3. Try filtering and pagination
- ✅ Data loads correctly

### Test 3: AI Classifier
1. Click on **"AI Classifier"** tab
2. Try entering some values manually
3. Click **"Predict"**
- ✅ Prediction works (you get a result)

### Test 4: Lightcurve Viewer
1. Click on **"Lightcurve Classifier"** tab
2. Try uploading a sample file from your computer
3. Click **"Classify"**
- ✅ Classification works

### Test 5: Check Browser Console
1. Press **F12** to open Developer Tools
2. Click **"Console"** tab
3. Look for any red error messages
- ✅ No CORS errors
- ✅ No 404 errors
- ✅ No failed network requests

---

## 🐛 Troubleshooting Common Issues

### Issue 1: "Failed to fetch" or Network Error

**Cause:** Backend might be sleeping (free tier)

**Solution:**
1. Wait 30-60 seconds
2. Try again
3. Your backend is waking up from sleep

---

### Issue 2: CORS Error in Console

**Error looks like:**
```
Access to fetch at 'https://...' has been blocked by CORS policy
```

**Solutions:**
1. Check that `VITE_API_URL` is set correctly in Vercel
2. Verify backend is running (visit backend URL directly)
3. Check backend has `flask-cors` installed

**To verify environment variable:**
1. Go to Vercel dashboard
2. Click on your project
3. Go to **Settings** → **Environment Variables**
4. Check `VITE_API_URL` is there and correct

---

### Issue 3: 404 Page Not Found on Routes

**Cause:** Routing issue

**Solution:**
- This should work automatically because we have `vercel.json`
- If not, check that `vercel.json` exists in `frontend/` folder

---

### Issue 4: Build Failed

**What to do:**
1. Click on the failed deployment
2. Read the error logs
3. Common causes:
   - Missing dependencies in `package.json`
   - Syntax errors in code
   - Wrong Node version

**Fix:**
1. Fix the error in your code
2. Commit and push:
   ```powershell
   git add .
   git commit -m "Fix build error"
   git push
   ```
3. Vercel will auto-deploy again

---

### Issue 5: Environment Variable Not Working

**Symptoms:**
- API calls go to `localhost:5000` instead of Render URL
- Console shows connection refused

**Solution:**
1. Go to Vercel Dashboard → Your Project
2. Click **Settings** tab
3. Click **Environment Variables** in sidebar
4. Verify `VITE_API_URL` exists
5. If missing, add it:
   - Name: `VITE_API_URL`
   - Value: Your Render URL
   - Environments: All checked
6. After adding/updating, you need to **redeploy**:
   - Go to **Deployments** tab
   - Click "..." on latest deployment
   - Click **"Redeploy"**

---

## 🔄 Future Updates - Automatic Deployment

Good news! From now on, every time you push to GitHub:

```
git add .
git commit -m "Your changes"
git push
```

**Vercel will automatically:**
1. Detect the push
2. Build your app
3. Deploy the new version
4. Update your live site

**No manual steps needed!** 🎉

---

## 📊 Vercel Dashboard Features

After deployment, explore these useful features:

### 1. Deployments
- See all your deployments
- Each commit creates a preview URL
- Roll back to previous versions

### 2. Analytics
- See visitor stats
- Performance metrics
- Core Web Vitals

### 3. Logs
- Real-time logs
- Error tracking
- Debug issues

### 4. Settings
- Environment variables
- Custom domains
- Build settings

---

## 🌐 Optional: Add Custom Domain

Want a custom domain like `exoplanet.yourname.com`?

1. Go to **Settings** → **Domains**
2. Click **"Add"**
3. Enter your domain
4. Follow DNS configuration steps
5. Vercel provides free SSL certificate!

---

## 🎉 Congratulations!

Your frontend is now deployed! 🚀

**What you've accomplished:**
- ✅ Deployed React/Vite app to Vercel
- ✅ Connected frontend to backend
- ✅ Set up automatic deployments
- ✅ App is live and accessible worldwide!

**Share your app:**
```
Check out my NASA Exoplanet Detection app:
https://your-app.vercel.app
```

---

## 📚 Quick Reference

**Vercel Dashboard:** https://vercel.com/dashboard

**Commands to update:**
```powershell
git add .
git commit -m "Update message"
git push
```

**Environment Variable:**
- Name: `VITE_API_URL`
- Value: `https://your-backend.onrender.com`

**Support:**
- Vercel Docs: https://vercel.com/docs
- Your Project Settings: Vercel Dashboard → Your Project → Settings

---

**Need help?** Check the troubleshooting section above or review the deployment logs in Vercel dashboard!

Good luck! 🌌✨
