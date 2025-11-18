# Flask Backend for MNIST/EMNIST Recognition

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 2. Run the Server

```bash
python app.py
```

The server will start at `http://localhost:5000` (or the port specified by the `PORT` environment variable).

### 3. Test the API

**Health Check:**
```bash
curl http://localhost:5000/health
```

**Test Prediction:**
```bash
curl -X POST http://localhost:5000/predict/digit \
  -H "Content-Type: application/json" \
  -d '{"image": "data:image/png;base64,YOUR_BASE64_IMAGE_HERE"}'
```

## 📡 API Endpoints

### GET `/`
Health check endpoint

**Response:**
```json
{
  "status": "running",
  "message": "MNIST/EMNIST Recognition API",
  "endpoints": {
    "/predict/digit": "Predict digit (0-9)",
    "/predict/letter": "Predict letter (A-Z)",
    "/health": "Check model status"
  }
}
```

### GET `/health`
Check model loading status

**Response:**
```json
{
  "mnist_model": "loaded",
  "emnist_model": "loaded"
}
```

### POST `/predict/digit`
Predict a digit (0-9)

**Request:**
```json
{
  "image": "data:image/png;base64,iVBORw0KGgoAAAANS..."
}
```

**Response:**
```json
{
  "success": true,
  "prediction": 7,
  "confidence": 0.9876,
  "top_3": [
    {"digit": 7, "confidence": 0.9876},
    {"digit": 1, "confidence": 0.0098},
    {"digit": 9, "confidence": 0.0015}
  ]
}
```

### POST `/predict/letter`
Predict a letter (A-Z)

**Request:**
```json
{
  "image": "data:image/png;base64,iVBORw0KGgoAAAANS..."
}
```

**Response:**
```json
{
  "success": true,
  "prediction": "A",
  "confidence": 0.9234,
  "top_3": [
    {"letter": "A", "confidence": 0.9234},
    {"letter": "H", "confidence": 0.0456},
    {"letter": "R", "confidence": 0.0123}
  ]
}
```

## 🔧 Configuration

### Environment Variables

- **PORT:** Server port (default: 5000)
  ```bash
  PORT=8080 python app.py
  ```

### Settings

- **Host:** 0.0.0.0 (accessible from network)
- **Debug Mode:** Disabled in production
- **CORS:** Enabled for all origins (configured via flask-cors)

## 📁 Required Files

Make sure these model files exist in the `model/` directory:
- `model/mnist_optimized.h5` - Digit recognition model
- `model/emnist_optimized.h5` - Letter recognition model

## 📦 Dependencies

All dependencies are listed in `requirements.txt`:
- `flask` - Web framework
- `flask-cors` - CORS support
- `tensorflow` - Machine learning framework
- `pillow` - Image processing
- `numpy` - Numerical computing
- `gunicorn` - WSGI HTTP server (for production)

## 🚀 Deployment

See [DEPLOYMENT.md](../DEPLOYMENT.md) for detailed deployment instructions to free hosting platforms like Railway or Render.

**Quick deployment options:**
- **Railway**: Automatic Python detection, deploys with `python app.py`
- **Render**: Uses gunicorn for production serving
- **Heroku**: Use the included `Procfile`

## ⚠️ Troubleshooting

**Models not loading:**
- Check that `.h5` files exist in the `model/` directory
- Verify TensorFlow is installed: `pip list | grep tensorflow`
- Ensure model files are not in `.gitignore` (or use Git LFS for large files)

**Port already in use:**
- Change port: `PORT=5001 python app.py`
- Or edit `app.py` directly

**CORS errors:**
- Verify `flask-cors` is installed
- Check browser console for detailed error messages
- Ensure frontend URL is making requests to the correct backend URL

**Memory issues on free hosting:**
- TensorFlow models can be large (100MB+)
- Consider using TensorFlow Lite for smaller model sizes
- Some free tiers have memory limitations (512MB-1GB)

## 🔒 Production Considerations

When deploying to production:

1. **Disable debug mode** (already handled in `app.py`)
2. **Use gunicorn** instead of Flask's development server:
   ```bash
   gunicorn --bind 0.0.0.0:$PORT app:app
   ```
3. **Set appropriate CORS origins** (currently allows all for development)
4. **Use HTTPS** (automatic on most hosting platforms)
5. **Monitor resource usage** (model inference can be CPU/memory intensive)

## 🎯 Next Steps

After backend is running:
1. Start the React frontend (see `../frontend/README.md`)
2. Configure frontend with backend URL
3. Deploy both to free hosting platforms (see `../DEPLOYMENT.md`)
