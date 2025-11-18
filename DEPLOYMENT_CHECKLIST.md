# Quick Deployment Checklist

Use this checklist to deploy your handwritten character recognition app to free hosting platforms.

## ✅ Pre-Deployment Checklist

### Model Files
- [ ] Ensure `.h5` model files are available:
  - [ ] `model/mnist_optimized.h5` (digit recognition)
  - [ ] `model/emnist_optimized.h5` (letter recognition)
- [ ] If model files are > 100MB, consider using Git LFS or uploading manually to hosting platform

### Repository Setup
- [ ] All code is committed to your GitHub repository
- [ ] `.gitignore` is properly configured
- [ ] Configuration files are present:
  - [ ] `vercel.json` (frontend deployment)
  - [ ] `railway.json` or `render.yaml` (backend deployment)
  - [ ] `Procfile` (optional, for Heroku)

## 🚀 Backend Deployment (Choose One)

### Option A: Railway
- [ ] Sign up at [Railway.app](https://railway.app)
- [ ] Create new project from GitHub repository
- [ ] Verify Railway detected Python runtime
- [ ] Check build logs for successful dependency installation
- [ ] Note your Railway URL (e.g., `https://your-app.railway.app`)
- [ ] Test backend health endpoint: `curl https://your-app.railway.app/health`

### Option B: Render
- [ ] Sign up at [Render.com](https://render.com)
- [ ] Create new Web Service from GitHub repository
- [ ] Configure:
  - [ ] Build Command: `cd backend && pip install -r requirements.txt`
  - [ ] Start Command: `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app`
  - [ ] Environment: Python 3
  - [ ] Plan: Free
- [ ] Wait for deployment to complete
- [ ] Note your Render URL (e.g., `https://your-app.onrender.com`)
- [ ] Test backend health endpoint: `curl https://your-app.onrender.com/health`

## 🎨 Frontend Deployment (Vercel)

- [ ] Sign up at [Vercel.com](https://vercel.com)
- [ ] Import project from GitHub
- [ ] Configure:
  - [ ] Framework: Create React App
  - [ ] Root Directory: `frontend`
  - [ ] Build Command: `npm run build` (or leave default)
  - [ ] Output Directory: `build`
  - [ ] Install Command: `npm install --legacy-peer-deps`
- [ ] Set environment variable:
  - [ ] Name: `REACT_APP_API_URL`
  - [ ] Value: Your backend URL from Railway/Render
- [ ] Deploy!
- [ ] Note your Vercel URL (e.g., `https://your-app.vercel.app`)

## 🧪 Post-Deployment Testing

- [ ] Visit your Vercel frontend URL
- [ ] Check browser console for errors (F12)
- [ ] Try drawing a digit and clicking "Predict"
- [ ] Verify prediction works correctly
- [ ] Try switching to letter mode and test
- [ ] Check that confidence scores are displayed
- [ ] Test on mobile device (optional)

## 🐛 Common Issues & Solutions

### Backend Not Responding
- [ ] Check backend deployment logs
- [ ] Verify backend health endpoint responds
- [ ] Ensure model files were deployed/uploaded
- [ ] Check free tier hasn't exceeded limits

### Frontend Can't Connect to Backend
- [ ] Verify `REACT_APP_API_URL` environment variable is set in Vercel
- [ ] Check that URL doesn't have trailing slash
- [ ] Ensure backend URL is HTTPS (not HTTP)
- [ ] Check browser console for CORS errors

### Cold Starts (Slow First Request)
- [ ] This is normal on free tiers (Railway, Render)
- [ ] Apps sleep after 15 minutes of inactivity
- [ ] First request after sleep can take 30-60 seconds
- [ ] Consider upgrading to paid tier if needed

### Model Loading Errors
- [ ] Ensure model files are in the repository or accessible
- [ ] Check backend logs for specific error messages
- [ ] Verify model files are not corrupted
- [ ] Consider using Git LFS for large files

## 📊 Monitoring

### Backend Monitoring
- [ ] Set up monitoring in Railway/Render dashboard
- [ ] Check resource usage (memory, CPU)
- [ ] Monitor free tier credit usage (Railway: $5/month)
- [ ] Watch deployment logs for errors

### Frontend Monitoring
- [ ] Check Vercel analytics dashboard
- [ ] Monitor bandwidth usage (100GB/month free)
- [ ] Review deployment history

## 🔄 Updating Your Deployment

### When You Make Changes:
- [ ] Commit and push changes to GitHub
- [ ] Railway/Render will auto-deploy backend changes
- [ ] Vercel will auto-deploy frontend changes
- [ ] Verify changes in production
- [ ] Test functionality after deployment

### If Auto-Deploy Fails:
- [ ] Check deployment logs
- [ ] Manually trigger redeploy from dashboard
- [ ] Verify all configuration is correct

## 📝 Documentation

- [ ] Update your README with live demo links
- [ ] Add screenshots of the deployed app
- [ ] Document any custom configuration
- [ ] Share your deployment story (optional)

## 🎉 Success Criteria

Your deployment is successful when:
- ✅ Frontend loads without errors
- ✅ Backend API responds to health checks
- ✅ Digit predictions work correctly
- ✅ Letter predictions work correctly
- ✅ UI is responsive and displays properly
- ✅ No CORS errors in browser console

## 🆘 Need Help?

If you encounter issues:
1. Check the detailed [DEPLOYMENT.md](./DEPLOYMENT.md) guide
2. Review platform-specific documentation (Vercel, Railway, Render)
3. Check deployment logs for error messages
4. Test backend independently with curl/Postman
5. Verify environment variables are set correctly

---

**Congratulations!** 🎊 Your AI-powered handwritten character recognition app is now live and accessible to the world!

Share your deployment:
- Tweet your project
- Add to your portfolio
- Share on LinkedIn
- Submit to project showcases

Happy deploying! 🚀
