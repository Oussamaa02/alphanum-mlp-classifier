# 🧠 Model Directory

This folder contains all the machine learning model files and training resources for the MNIST/EMNIST character recognition project.

## 📁 Contents

### Trained Models
- **`mnist_optimized.h5`** - Digit recognition model (0-9)
  - Accuracy: 99.18%
  - Size: ~2.5 MB
  - Architecture: CNN with 2 Conv layers + Dense layers
  - Trained with Adam optimizer

- **`emnist_optimized.h5`** - Letter recognition model (A-Z)
  - Accuracy: ~90-95%
  - Size: ~2.5 MB
  - Architecture: CNN with 2 Conv layers + Dense layers
  - Trained with Adam optimizer

### Training Resources
- **`mnist_emnist_classification.ipynb`** - Jupyter notebook for training both models
  - Complete training pipeline
  - Data preprocessing
  - Model architecture definition
  - Training with validation
  - Performance visualization
  - Model evaluation

- **`requirements.txt`** - Python dependencies needed for training
  ```
  tensorflow>=2.10.0
  keras>=2.10.0
  scikit-learn>=1.0.0
  scipy>=1.7.0
  numpy>=1.21.0
  matplotlib>=3.4.0
  opencv-python>=4.5.0
  ```

- **`test_installation.py`** - Installation verification script
  - Tests all dependencies
  - Verifies TensorFlow/Keras setup
  - Checks GPU availability
  - Tests model loading
  - Quick neural network test

### Dataset
- **`data/emnist-letters.mat`** - EMNIST Letters dataset
  - Format: MATLAB .mat file
  - Contains: Training and test sets for letters A-Z
  - Size: ~145,000+ handwritten letter images
  - Image size: 28x28 grayscale

## 🚀 Quick Start

### To Test Installation
```bash
cd model
C:\tfvenv\Scripts\python.exe test_installation.py
```

### To Train Models
1. Open `mnist_emnist_classification.ipynb` in Jupyter/VS Code
2. Select Python kernel: `C:\tfvenv\Scripts\python.exe`
3. Run all cells to train both models

### To Use Models in Backend
The Flask backend in `../backend/app.py` automatically loads these models:
```python
MODEL_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'model')
MNIST_MODEL_PATH = os.path.join(MODEL_DIR, 'mnist_optimized.h5')
EMNIST_MODEL_PATH = os.path.join(MODEL_DIR, 'emnist_optimized.h5')
```

## 🏗️ Model Architecture

Both models use similar CNN architecture:

```
Input (28x28x1 grayscale image)
    ↓
Conv2D(32 filters, 3x3) + ReLU + BatchNorm + MaxPool(2x2)
    ↓
Conv2D(64 filters, 3x3) + ReLU + BatchNorm + MaxPool(2x2) + Dropout(0.25)
    ↓
Flatten
    ↓
Dense(128) + ReLU + BatchNorm + Dropout(0.5)
    ↓
Dense(10 or 27) + Softmax
    ↓
Output (probabilities for each class)
```

### Key Techniques
- **Batch Normalization**: Prevents vanishing gradient
- **Dropout**: Reduces overfitting (0.25 after conv, 0.5 after dense)
- **Adam Optimizer**: Fast convergence with adaptive learning rate
- **Early Stopping**: Prevents overtraining

## 📊 Model Performance

### MNIST (Digits)
- Training accuracy: 99.92%
- Validation accuracy: 99.60%
- Test accuracy: 99.18%
- Training time: ~10-15 minutes

### EMNIST (Letters)
- Training accuracy: ~98%
- Validation accuracy: ~95%
- Test accuracy: ~90-95%
- Training time: ~15-20 minutes

## 🔄 Retraining Models

If you need to retrain:

1. **Adjust hyperparameters** in the notebook:
   - Learning rate
   - Batch size
   - Number of epochs
   - Dropout rates

2. **Run all cells** to train from scratch

3. **Models will be saved** as:
   - `mnist_optimized.h5`
   - `emnist_optimized.h5`

4. **Backend will automatically** use the new models

## 📈 Training Tips

- **GPU recommended**: Training is 5-10x faster with GPU
- **Monitor validation accuracy**: Stop if it plateaus
- **Early stopping**: Built-in to prevent overfitting
- **Data augmentation**: Consider adding for better generalization

## 🐛 Troubleshooting

**Model won't load:**
- Check TensorFlow version: `pip list | findstr tensorflow`
- Verify file exists and isn't corrupted
- Try retraining if necessary

**Low accuracy:**
- Check data preprocessing
- Verify image inversion (white on black for MNIST)
- Ensure proper normalization [0, 1]

**Out of memory:**
- Reduce batch size
- Use CPU instead of GPU
- Close other applications

## 📚 Resources

- [TensorFlow Documentation](https://www.tensorflow.org/)
- [Keras API Reference](https://keras.io/)
- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)
- [EMNIST Dataset](https://www.nist.gov/itl/products-and-services/emnist-dataset)

---

**Note:** This folder is self-contained and can be used independently for training/evaluation without the web application.
