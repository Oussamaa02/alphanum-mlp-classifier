from flask import Flask, request, jsonify
from flask_cors import CORS
import tensorflow as tf
from tensorflow import keras
import numpy as np
from PIL import Image
import io
import base64
import os

app = Flask(__name__)
CORS(app) 

# Global variables for models
mnist_model = None
emnist_model = None

MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model')
MNIST_MODEL_PATH = os.path.join(MODEL_DIR, 'mnist_optimized.h5')
EMNIST_MODEL_PATH = os.path.join(MODEL_DIR, 'emnist_optimized.h5')

def load_models():
    """Load the trained models at startup"""
    global mnist_model, emnist_model
    
    print("🔄 Loading models...")
    
    try:
        if os.path.exists(MNIST_MODEL_PATH):
            mnist_model = keras.models.load_model(MNIST_MODEL_PATH)
            print(f"✅ MNIST model loaded from {MNIST_MODEL_PATH}")
        else:
            print(f"⚠️  MNIST model not found at {MNIST_MODEL_PATH}")
            
        if os.path.exists(EMNIST_MODEL_PATH):
            emnist_model = keras.models.load_model(EMNIST_MODEL_PATH)
            print(f"✅ EMNIST model loaded from {EMNIST_MODEL_PATH}")
        else:
            print(f"⚠️  EMNIST model not found at {EMNIST_MODEL_PATH}")
            
    except Exception as e:
        print(f"❌ Error loading models: {e}")

def preprocess_image(image_data, target_size=(28, 28)):
    """
    Preprocess image for model prediction
    - Convert to grayscale
    - Resize to 28x28
    - Invert colors (black background, white digit)
    - Normalize to [0, 1]
    """
    try:
        # Decode base64 image
        if ',' in image_data:
            image_data = image_data.split(',')[1]
        
        image_bytes = base64.b64decode(image_data)
        image = Image.open(io.BytesIO(image_bytes))
        
        # Convert to grayscale
        image = image.convert('L')
        
        image = image.resize(target_size, Image.Resampling.LANCZOS)
        
        image_array = np.array(image)
        
        # Invert colors (MNIST uses white digits on black background)
        image_array = 255 - image_array
        
        # Normalize to [0, 1]
        image_array = image_array.astype('float32') / 255.0
        
        print(f"📸 Image stats: min={image_array.min():.3f}, max={image_array.max():.3f}, mean={image_array.mean():.3f}")
        
        image_array = image_array.reshape(1, 28, 28, 1)
        
        return image_array
        
    except Exception as e:
        print(f"Error preprocessing image: {e}")
        return None

@app.route('/')
def home():
    """Health check endpoint"""
    return jsonify({
        'status': 'running',
        'message': 'MNIST/EMNIST Recognition API',
        'endpoints': {
            '/predict/digit': 'Predict digit (0-9)',
            '/predict/letter': 'Predict letter (A-Z)',
            '/health': 'Check model status'
        },
    })

@app.route('/health')
def health():
    """Check if models are loaded"""
    return jsonify({
        'mnist_model': 'loaded' if mnist_model is not None else 'not loaded',
        'emnist_model': 'loaded' if emnist_model is not None else 'not loaded'
    })

@app.route('/predict/digit', methods=['POST'])
def predict_digit():
    """Predict digit (0-9) from drawn image"""
    try:
        if mnist_model is None:
            return jsonify({'error': 'MNIST model not loaded'}), 500
        
        data = request.get_json()
        if 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400
        
        print(f"\n🔍 Processing digit prediction...")
        print(f"📦 Received image data length: {len(data['image'])}")
        
        image_array = preprocess_image(data['image'])
        if image_array is None:
            return jsonify({'error': 'Failed to process image'}), 400
        
        predictions = mnist_model.predict(image_array, verbose=0)
        predicted_class = int(np.argmax(predictions[0]))
        confidence = float(predictions[0][predicted_class])
        
        top_3_indices = np.argsort(predictions[0])[-3:][::-1]
        top_3_predictions = [
            {
                'digit': int(idx),
                'confidence': float(predictions[0][idx])
            }
            for idx in top_3_indices
        ]
        
        return jsonify({
            'success': True,
            'prediction': predicted_class,
            'confidence': confidence,
            'top_3': top_3_predictions,
            'all_probabilities': predictions[0].tolist()
        })
        
    except Exception as e:
        print(f"Error in predict_digit: {e}")
        return jsonify({'error': str(e)}), 500

@app.route('/predict/letter', methods=['POST'])
def predict_letter():
    """Predict letter (A-Z) from drawn image"""
    try:
        if emnist_model is None:
            return jsonify({'error': 'EMNIST model not loaded'}), 500
        
        data = request.get_json()
        if 'image' not in data:
            return jsonify({'error': 'No image data provided'}), 400
        
        print(f"\n🔍 Processing letter prediction...")
        print(f"📦 Received image data length: {len(data['image'])}")
        
        image_array = preprocess_image(data['image'])
        if image_array is None:
            return jsonify({'error': 'Failed to process image'}), 400
        
        predictions = emnist_model.predict(image_array, verbose=0)
        predicted_class = int(np.argmax(predictions[0]))
        confidence = float(predictions[0][predicted_class])
        
        # EMNIST Letters uses classes 1-26 for A-Z (class 0 is typically unused/background)
        # So we map: class 1 -> A, class 2 -> B, ..., class 26 -> Z
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
                   'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        
        num_classes = len(predictions[0])
        print(f"📊 Model output shape: {num_classes} classes")
        print(f"🎯 Predicted class: {predicted_class}, Confidence: {confidence:.4f}")
        
        if num_classes == 26:
            # Model uses 0-25 indexing directly
            predicted_letter = letters[predicted_class] if 0 <= predicted_class < 26 else '?'
        else:
            # Model uses 1-26 indexing (class 0 unused)
            predicted_letter = letters[predicted_class - 1] if 1 <= predicted_class <= 26 else '?'
        
        top_3_indices = np.argsort(predictions[0])[-3:][::-1]
        top_3_predictions = []
        for idx in top_3_indices:
            if num_classes == 26:
                letter = letters[idx] if 0 <= idx < 26 else '?'
            else:
                letter = letters[idx - 1] if 1 <= idx <= 26 else '?'
            top_3_predictions.append({
                'letter': letter,
                'confidence': float(predictions[0][idx])
            })
        
        return jsonify({
            'success': True,
            'prediction': predicted_letter,
            'confidence': confidence,
            'top_3': top_3_predictions,
            'all_probabilities': predictions[0].tolist()
        })
        
    except Exception as e:
        print(f"Error in predict_letter: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    load_models()
    
    print("\n" + "="*60)
    print("🚀 Starting Flask API Server")
    print("="*60)
    print("📍 Server running at: http://localhost:5000")
    print("📝 Endpoints:")
    print("   • GET  /           - Health check")
    print("   • GET  /health     - Model status")
    print("   • POST /predict/digit  - Predict digit (0-9)")
    print("   • POST /predict/letter - Predict letter (A-Z)")
    print("="*60 + "\n")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
else:
    # This runs when started with gunicorn (production)
    load_models()
