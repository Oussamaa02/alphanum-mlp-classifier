# Handwritten Character Recognition

A complete web application that recognizes handwritten digits (0-9) and letters (A-Z) using deep learning. Draw on a canvas and get instant predictions!

**Model Performance:**
- Digits (MNIST): 99.18% accuracy
- Letters (EMNIST): ~90-95% accuracy

## Technologies Used

- **Machine Learning**: TensorFlow, Keras, NumPy
- **Backend**: Flask, Pillow, flask-cors
- **Frontend**: React, TypeScript, react-canvas-draw
- **Data**: MNIST, EMNIST Datasets

### Running the Application

1. **Backend**
```bash
cd backend
pip install -r requirements.txt
C:\tfvenv\Scripts\python.exe app.py
```

2. **Frontend**
```bash
cd frontend
npm install
npm start
```

## Model Training

1. Open the Jupyter notebook:
```bash
jupyter notebook model/mnist_emnist_classification.ipynb
```

2. Make sure the kernel is configured to `C:\tfvenv\Scripts\python.exe`

3. Execute all cells 


## Project Structure

```
├── backend/               # Flask API server
│   ├── app.py            # Main server file
│   └── requirements.txt  # Python dependencies
├── frontend/             # React web application
│   ├── src/
│   │   ├── App.tsx      # Main component
│   │   └── App.css      # Styles
│   └── package.json     # npm dependencies
├── model/                # ML models and training
│   ├── mnist_optimized.h5      # Digit recognition model
│   ├── emnist_optimized.h5     # Letter recognition model
│   ├── mnist_emnist_classification.ipynb  # Training notebook
│   └── data/
│       └── emnist-letters.mat  # EMNIST dataset
└── README.md           
```

## Technical Details

### Model Architecture
```
Input (28x28 grayscale image)
    ↓
Conv2D (32 filters, 3x3) + ReLU + BatchNorm + MaxPool
    ↓
Conv2D (64 filters, 3x3) + ReLU + BatchNorm + MaxPool + Dropout(0.5)
    ↓
Flatten
    ↓
Dense(1568) + ReLU + BatchNorm + Dropout(0.5)
Dense(1000) + ReLU + BatchNorm + Dropout(0.5)
Dense(700) + ReLU + BatchNorm + Dropout(0.5)
Dense(300) + ReLU + BatchNorm + Dropout(0.5)
Dense(100) + ReLU + BatchNorm
    ↓
Output (10 or 27 classes) + Softmax
```

### Image Preprocessing Pipeline
```
User draws a 280x280 image
    ↓
Convert to grayscale
    ↓
Resize to 28x28 (training data size)
    ↓
Invert colors (white digits on black background)
    ↓
Normalize pixel values to [0, 1]
    ↓
Reshape to (1, 28, 28, 1)
    ↓
Ready for prediction!
```

## Results

**MNIST Digits:**
- Training: 99.92%
- Validation: 99.60%
- Test: 99.18% (only 82 errors out of 10,000 images!)

**EMNIST Letters:**
- Training: 98.7%
- Validation: 95.1%
- Test: ~94.9%


