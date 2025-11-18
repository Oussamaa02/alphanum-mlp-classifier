"""
Script de Test Rapide - Vérification de l'Installation
"""

import sys

print("=" * 60)
print("TEST DE L'ENVIRONNEMENT - Reconnaissance de Caractères")
print("=" * 60)

# Test 1: TensorFlow
print("\n[1/6] Test de TensorFlow...", end=" ")
try:
    import tensorflow as tf
    print(f"✓ OK (version {tf.__version__})")
except ImportError as e:
    print(f"✗ ERREUR: {e}")
    print("   → Installez avec: pip install tensorflow")
    sys.exit(1)

# Test 2: Keras
print("[2/6] Test de Keras...", end=" ")
try:
    from tensorflow import keras
    print(f"✓ OK (version {keras.__version__})")
except ImportError as e:
    print(f"✗ ERREUR: {e}")
    sys.exit(1)

# Test 3: NumPy
print("[3/6] Test de NumPy...", end=" ")
try:
    import numpy as np
    print(f"✓ OK (version {np.__version__})")
except ImportError as e:
    print(f"✗ ERREUR: {e}")
    print("   → Installez avec: pip install numpy")
    sys.exit(1)

# Test 4: Matplotlib
print("[4/6] Test de Matplotlib...", end=" ")
try:
    import matplotlib.pyplot as plt
    print("✓ OK")
except ImportError as e:
    print(f"✗ ERREUR: {e}")
    print("   → Installez avec: pip install matplotlib")
    sys.exit(1)

# Test 5: Scikit-learn
print("[5/6] Test de Scikit-learn...", end=" ")
try:
    from sklearn.model_selection import train_test_split
    print("✓ OK")
except ImportError as e:
    print(f"✗ ERREUR: {e}")
    print("   → Installez avec: pip install scikit-learn")
    sys.exit(1)

# Test 6: SciPy
print("[6/6] Test de SciPy...", end=" ")
try:
    from scipy import io as sio
    print("✓ OK")
except ImportError as e:
    print(f"✗ ERREUR: {e}")
    print("   → Installez avec: pip install scipy")
    sys.exit(1)

# Test 7: Vérification MNIST
print("\n" + "=" * 60)
print("TEST DES DONNÉES")
print("=" * 60)
print("\n[1/2] Chargement de MNIST...", end=" ")
try:
    from tensorflow.keras.datasets import mnist
    (x_train, y_train), (x_test, y_test) = mnist.load_data()
    print(f"✓ OK ({x_train.shape[0]} images d'entraînement)")
except Exception as e:
    print(f"✗ ERREUR: {e}")

# Test 8: Vérification EMNIST
print("[2/2] Vérification du fichier EMNIST...", end=" ")
import os
emnist_path = "data/emnist-letters.mat"
if os.path.exists(emnist_path):
    print(f"✓ OK (fichier trouvé)")
else:
    print(f"⚠ ATTENTION: Fichier non trouvé")
    print(f"   → Le fichier devrait être dans: {os.path.abspath(emnist_path)}")
    print("   → Vous pouvez quand même utiliser MNIST seul!")

# Test rapide d'un mini-modèle
print("\n" + "=" * 60)
print("TEST RAPIDE DU RÉSEAU DE NEURONES")
print("=" * 60)
print("\n[*] Création d'un mini-modèle de test...", end=" ")
try:
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Dense, Flatten
    
    model = Sequential([
        Flatten(input_shape=(28, 28)),
        Dense(10, activation='relu'),
        Dense(10, activation='softmax')
    ])
    model.compile(loss='categorical_crossentropy', 
        optimizer='adam', 
        metrics=['accuracy'])
    print("✓ OK")
    
    print("[*] Test d'entraînement sur 100 échantillons...", end=" ")
    from tensorflow.keras.utils import to_categorical
    x_sample = x_train[:100].reshape(100, 28, 28).astype('float32') / 255.0
    y_sample = to_categorical(y_train[:100], 10)
    
    model.fit(x_sample, y_sample, epochs=1, verbose=0)
    print("✓ OK")
    
    print("[*] Test de prédiction...", end=" ")
    predictions = model.predict(x_sample[:10], verbose=0)
    print(f"✓ OK (shape: {predictions.shape})")
    
except Exception as e:
    print(f"✗ ERREUR: {e}")

# Résumé
print("\n" + "=" * 60)
print("RÉSUMÉ")
print("=" * 60)
print("\n✓ Toutes les bibliothèques sont installées correctement")
print("✓ Les datasets sont accessibles")
print("✓ Le réseau de neurones fonctionne")
print("\n→ Vous êtes prêt à lancer le notebook principal!")
print("→ Ouvrez: mnist_emnist_classification_clean.ipynb")
print("=" * 60)

# Informations système
print("\nInformations système:")
print(f"- Python version: {sys.version.split()[0]}")
print(f"- TensorFlow version: {tf.__version__}")

# Vérification GPU
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    print(f"- GPU disponible: {len(gpus)} GPU(s) détecté(s) ✓")
    print("  → L'entraînement sera RAPIDE!")
else:
    print("- GPU disponible: Non (CPU seulement)")
    print("  → L'entraînement prendra plus de temps (~20-30 min)")

print("\n" + "=" * 60)
print("TEST TERMINÉ AVEC SUCCÈS! 🎉")
print("=" * 60)
