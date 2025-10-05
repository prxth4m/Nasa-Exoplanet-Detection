# ✅ Vercel Deployment Checklist

**Quick checklist - follow along as you deploy!**

---

## Before Starting

- [ ] Backend deployed on Render ✅
- [ ] Backend URL copied: ______________________________
- [ ] Code pushed to GitHub ✅
- [ ] Vercel account created ✅

---

## Deployment Steps

### 1️⃣ Open Vercel
- [ ] Go to https://vercel.com/dashboard
- [ ] Signed in with GitHub

### 2️⃣ Create Project
- [ ] Click "Add New..." → "Project"
- [ ] Found my repository: `nasa-exoplanet-detection`
- [ ] Clicked "Import"

### 3️⃣ Configure Project
- [ ] Project Name: `nasa-exoplanet-detection`
- [ ] Framework Preset: `Vite`
- [ ] **Root Directory: `frontend`** ⚠️ IMPORTANT!
- [ ] Build Command: `npm run build` (default)
- [ ] Output Directory: `dist` (default)

### 4️⃣ Add Environment Variable ⚠️ CRITICAL
- [ ] Expanded "Environment Variables" section
- [ ] Added variable:
  - Name: `VITE_API_URL`
  - Value: `https://my-backend-url.onrender.com`
  - Environments: ✅ All three checked
- [ ] Clicked "Add"
- [ ] Variable appears in the list ✅

### 5️⃣ Deploy
- [ ] Reviewed all settings
- [ ] Clicked "Deploy" button
- [ ] Watching build progress...

### 6️⃣ Wait for Success
- [ ] "Building..." ⏳
- [ ] "Deploying..." ⏳
- [ ] "Success! 🎉" ✅

### 7️⃣ Copy URL
- [ ] Clicked "Visit"
- [ ] App opened in browser
- [ ] Copied URL: ______________________________

---

## Testing

- [ ] App loads without errors
- [ ] Data Explorer works
- [ ] AI Classifier works
- [ ] Lightcurve upload works
- [ ] No CORS errors in console (F12)

---

## My Deployment Info

**Live URLs:**
```
Frontend: https://________________________________.vercel.app
Backend:  https://________________________________.onrender.com
GitHub:   https://github.com/prxth4m/nasa-exoplanet-detection
```

**Deployment Date:** _______________

**Status:** ✅ DEPLOYED SUCCESSFULLY!

---

## If Something Goes Wrong

Check the detailed guide: `VERCEL_DEPLOYMENT_GUIDE.md`

**Common fixes:**
1. Environment variable missing → Add in Vercel Settings
2. Build failed → Check logs in Vercel dashboard
3. CORS error → Verify backend URL is correct
4. 404 on refresh → vercel.json should be in frontend folder

---

**Total Time:** ~5 minutes

🎉 **DONE!** Your app is live!
