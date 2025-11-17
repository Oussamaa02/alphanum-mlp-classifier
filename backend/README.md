# Flask Backend for MNIST/EMNIST Recognition

## 🚀 Quick Start

### 1. Install Dependencies

Using your existing virtual environment:

```bash
# Activate the venv
C:\tfvenv\Scripts\activate

# Install Flask dependencies
pip install flask flask-cors pillow
```

### 2. Run the Server

```bash
cd backend
C:\tfvenv\Scripts\python.exe app.py
# python app.py
```

The server will start at `http://localhost:5000`

### 3. Test the API

**Health Check:**
```bash
curl http://localhost:5000/health
```

**Test Prediction (PowerShell):**
```powershell
$body = @{
    image = "data:image/png;base64,YOUR_BASE64_IMAGE_HERE"
} | ConvertTo-Json

Invoke-RestMethod -Uri "http://localhost:5000/predict/digit" -Method POST -Body $body -ContentType "application/json"
```

## 📡 API Endpoints

### GET `/`
Health check endpoint

**Response:**
```json
{
  "status": "running",
  "message": "MNIST/EMNIST Recognition API"
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

- **Port:** 5000 (default)
- **Host:** 0.0.0.0 (accessible from network)
- **Debug Mode:** Enabled (disable in production)
- **CORS:** Enabled for all origins (restrict in production)

## 📁 Required Files

Make sure these model files exist in the `model/` directory:
- `model/mnist_optimized.h5` - Digit recognition model
- `model/emnist_optimized.h5` - Letter recognition model

## ⚠️ Troubleshooting

**Models not loading:**
- Check that `.h5` files exist in the `model/` directory
- Verify TensorFlow is installed: `pip list | findstr tensorflow`

**Port already in use:**
- Change port in `app.py`: `app.run(port=5001)`

**CORS errors:**
- Verify `flask-cors` is installed
- Check browser console for detailed error messages

## 🎯 Next Steps

After backend is running, proceed to create the React frontend!
