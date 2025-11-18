# Deployment Guide for Alphanum MLP Classifier

This guide covers deploying your Flask backend and React frontend to free hosting platforms.

## Overview

- **Frontend (React)**: Deploy to Vercel (free)
- **Backend (Flask)**: Deploy to Railway or Render (both have free tiers)

## Prerequisites

- GitHub account
- Accounts on deployment platforms (Vercel, Railway, or Render)
- Your model files (`.h5` files) must be in the repository or accessible

## 🚀 Deployment Options

### Option 1: Vercel (Frontend) + Railway (Backend)

#### Step 1: Deploy Backend to Railway

1. **Sign up** at [Railway.app](https://railway.app)

2. **Create New Project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your `alphanum-mlp-classifier` repository
   - Railway will auto-detect it's a Python project

3. **Configure Environment**:
   - Railway will automatically install dependencies from `backend/requirements.txt`
   - Make sure your `.h5` model files are included in the repository (not in `.gitignore`)
   - Railway will assign a public URL automatically

4. **Set Build Command** (if needed):
   ```
   cd backend && pip install -r requirements.txt
   ```

5. **Set Start Command**:
   ```
   cd backend && python app.py
   ```

6. **Note your Railway URL**: e.g., `https://your-app.railway.app`

#### Step 2: Deploy Frontend to Vercel

1. **Sign up** at [Vercel.com](https://vercel.com)

2. **Import Project**:
   - Click "Add New" → "Project"
   - Import your GitHub repository
   - Select the repository `alphanum-mlp-classifier`

3. **Configure Build Settings**:
   - Framework Preset: Create React App
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `build`

4. **Set Environment Variables**:
   - Add environment variable:
     - Name: `REACT_APP_API_URL`
     - Value: Your Railway backend URL (e.g., `https://your-app.railway.app`)

5. **Deploy**: Click "Deploy"

6. **Your app is live!** Vercel will provide a URL like `https://your-app.vercel.app`

---

### Option 2: Vercel (Frontend) + Render (Backend)

#### Step 1: Deploy Backend to Render

1. **Sign up** at [Render.com](https://render.com)

2. **Create New Web Service**:
   - Click "New" → "Web Service"
   - Connect your GitHub repository
   - Select `alphanum-mlp-classifier`

3. **Configure Service**:
   - **Name**: `alphanum-classifier-api`
   - **Runtime**: Python 3
   - **Build Command**: `cd backend && pip install -r requirements.txt`
   - **Start Command**: `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app`
   - **Plan**: Free

4. **Environment Variables**:
   - `PYTHON_VERSION`: `3.11.0`
   - Render will automatically set `PORT`

5. **Note your Render URL**: e.g., `https://your-app.onrender.com`

#### Step 2: Deploy Frontend to Vercel

Follow the same steps as in Option 1, Step 2, but use your Render backend URL for the `REACT_APP_API_URL` environment variable.

---

## 📝 Configuration Files Included

This repository includes configuration files for easy deployment:

- **`vercel.json`**: Vercel configuration for frontend
- **`railway.json`**: Railway configuration for backend
- **`render.yaml`**: Render configuration for backend
- **`.env.example`**: Example environment variables

## ⚙️ Environment Variables

### Frontend (`frontend/.env`)
```env
REACT_APP_API_URL=https://your-backend-url.com
```

### Backend
```env
PORT=5000
FLASK_ENV=production
```

## 🔧 Important Notes

### Model Files
- The `.h5` model files are currently in `.gitignore` to avoid large files in git
- For deployment, you have two options:
  1. **Remove from .gitignore** and commit them (if < 100MB)
  2. **Use Git LFS** (Large File Storage) for files > 100MB
  3. **Upload manually** to the hosting service after deployment

### Free Tier Limitations

**Railway Free Tier**:
- $5 free credit/month
- No credit card required initially
- Apps sleep after 15 minutes of inactivity

**Render Free Tier**:
- 750 hours/month free
- Apps sleep after 15 minutes of inactivity
- Cold starts (takes ~30 seconds to wake up)

**Vercel Free Tier**:
- Unlimited deployments
- 100GB bandwidth/month
- Automatic HTTPS

### CORS Configuration
The backend already includes CORS support via `flask-cors`, allowing cross-origin requests from your frontend.

## 🐛 Troubleshooting

### Backend Issues

**Problem**: Models not loading
- **Solution**: Ensure `.h5` files are in the `model/` directory and accessible

**Problem**: Memory issues on free tier
- **Solution**: TensorFlow models can be large. Consider:
  - Using TensorFlow Lite versions of models
  - Quantizing models to reduce size
  - Upgrading to paid tier if needed

### Frontend Issues

**Problem**: API calls failing
- **Solution**: Check that `REACT_APP_API_URL` environment variable is set correctly in Vercel

**Problem**: CORS errors
- **Solution**: Verify backend URL is correct and CORS is enabled (already configured)

## 🔄 Updating Your Deployment

### Railway/Render
- Push changes to GitHub
- Railway/Render will automatically redeploy

### Vercel
- Push changes to GitHub
- Vercel will automatically redeploy
- Update environment variables in Vercel dashboard if needed

## 💰 Cost Comparison

| Platform | Free Tier | Best For |
|----------|-----------|----------|
| **Vercel** | Generous free tier | Frontend static sites |
| **Railway** | $5/month credit | Quick backend deployment |
| **Render** | 750 hrs/month | Backend APIs with cold starts OK |

## 🎉 Quick Start Commands

### Local Development
```bash
# Backend
cd backend
pip install -r requirements.txt
python app.py

# Frontend (in new terminal)
cd frontend
npm install
REACT_APP_API_URL=http://localhost:5000 npm start
```

### Build Frontend for Production
```bash
cd frontend
npm run build
```

## 📚 Additional Resources

- [Vercel Documentation](https://vercel.com/docs)
- [Railway Documentation](https://docs.railway.app/)
- [Render Documentation](https://render.com/docs)
- [Flask Deployment Guide](https://flask.palletsprojects.com/en/2.3.x/deploying/)
- [Create React App Deployment](https://create-react-app.dev/docs/deployment/)

## ⚠️ Security Considerations

1. **Never commit sensitive data** (API keys, secrets) to git
2. **Use environment variables** for all configuration
3. **Enable HTTPS** (automatic on Vercel, Railway, Render)
4. **Keep dependencies updated** for security patches

---

## Need Help?

If you encounter issues:
1. Check the deployment logs on your hosting platform
2. Verify environment variables are set correctly
3. Test the backend health endpoint: `https://your-backend-url.com/health`
4. Check browser console for frontend errors

Happy deploying! 🚀
