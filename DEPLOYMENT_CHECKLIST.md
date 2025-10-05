# 📋 Deployment Status Checklist

## Pre-Deployment
- [ ] Code is working locally (frontend + backend)
- [ ] GitHub repository is created and code is pushed
- [ ] Vercel account created and connected to GitHub
- [ ] Render account created and connected to GitHub

## Backend Deployment (Render)
- [ ] Created new Web Service on Render
- [ ] Selected correct GitHub repository
- [ ] Configured root directory: `backend`
- [ ] Build command: `pip install -r requirements.txt`
- [ ] Start command: `gunicorn app:app --bind 0.0.0.0:$PORT --workers 1 --threads 2 --timeout 120`
- [ ] Deployment successful
- [ ] Backend URL copied: `_________________________________`
- [ ] Backend health check passed (visit URL in browser)

## Frontend Configuration
- [ ] Updated `frontend/.env.production` with backend URL
- [ ] Committed and pushed changes to GitHub
  ```bash
  git add frontend/.env.production
  git commit -m "Update production API URL"
  git push
  ```

## Frontend Deployment (Vercel)
- [ ] Created new Project on Vercel
- [ ] Imported GitHub repository
- [ ] Configured root directory: `frontend`
- [ ] Framework preset: `Vite`
- [ ] Build command: `npm run build`
- [ ] Output directory: `dist`
- [ ] Added environment variable: `VITE_API_URL`
- [ ] Deployment successful
- [ ] Frontend URL: `_________________________________`

## Testing
- [ ] Can access frontend URL
- [ ] Data Explorer loads correctly
- [ ] Can submit manual predictions (AI Classifier)
- [ ] Can upload CSV for batch predictions
- [ ] Can upload lightcurve files
- [ ] No CORS errors in browser console
- [ ] Backend API responds correctly
- [ ] All features working end-to-end

## Post-Deployment
- [ ] Shared deployment URL with team/users
- [ ] Updated README with live URL (optional)
- [ ] Monitored logs for errors (first 24 hours)
- [ ] Set up custom domain (optional)

## Troubleshooting Notes
Write any issues encountered and solutions:
```
Issue 1: 

Solution: 


Issue 2: 

Solution: 

```

## Important URLs
- **GitHub Repo**: _________________________________
- **Render Backend**: _________________________________
- **Vercel Frontend**: _________________________________
- **Custom Domain** (if any): _________________________________

---

**Deployment Date**: _______________
**Deployed By**: _______________
**Status**: ⬜ In Progress  ⬜ Complete  ⬜ Failed
