# 🚀 Quick Deployment Steps

## Step 1: Push to GitHub (if not already done)
```bash
git add .
git commit -m "Prepare for deployment"
git push origin main
```

## Step 2: Deploy Backend to Render

1. Go to https://dashboard.render.com/
2. Click **"New +"** → **"Web Service"**
3. Select your GitHub repository
4. Configure:
   - Root Directory: `backend`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --threads 2 --timeout 120`
5. Click **"Create Web Service"**
6. **COPY THE URL** (e.g., `https://your-app.onrender.com`)

## Step 3: Update Frontend Environment

1. Edit `frontend/.env.production`
2. Replace the URL with your Render backend URL:
   ```env
   VITE_API_URL=https://your-actual-backend-url.onrender.com
   ```
3. Commit and push:
   ```bash
   git add frontend/.env.production
   git commit -m "Update production API URL"
   git push
   ```

## Step 4: Deploy Frontend to Vercel

1. Go to https://vercel.com/dashboard
2. Click **"Add New..."** → **"Project"**
3. Import your GitHub repository
4. Configure:
   - Framework: `Vite`
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`
5. Add Environment Variable:
   - Name: `VITE_API_URL`
   - Value: `https://your-backend-url.onrender.com`
6. Click **"Deploy"**

## Step 5: Test Your Deployment

1. Visit your Vercel URL
2. Test the prediction form
3. Test lightcurve upload
4. Check browser console for errors

## ✅ Done!

Your app is now live! 🎉

---

**Need detailed instructions?** See `DEPLOYMENT.md`
