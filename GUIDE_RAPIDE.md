# Guide Rapide - Projet Neural Networks

## 📋 Description du Projet

**Projet**: Reconnaissance de caractères alphanumériques par Perceptron Multicouche (MLP)

**Objectif**: Développer un MLP pour reconnaître des chiffres (0-9) et des lettres (A-Z) à partir d'images

**Datasets utilisés**: 
- MNIST (chiffres manuscrits)
- EMNIST Letters (lettres manuscrites)

## ✅ Ce qui a été fait

1. **Nettoyage du code** - Correction de tous les problèmes de compatibilité
2. **Simplification** - Notebook structuré et facile à suivre
3. **Optimisation** - Réduction du temps d'entraînement (50 epochs au lieu de 196)
4. **Documentation** - Commentaires en français et explications claires

## 🚀 Installation Rapide

### 1. Installer les dépendances

```bash
pip install tensorflow keras scikit-learn scipy matplotlib opencv-python
```

### 2. Vérifier que les données sont présentes

Assurez-vous que le fichier `data/emnist-letters.mat` existe dans votre répertoire.

## 📁 Fichiers Importants

- **`mnist_emnist_classification_clean.ipynb`** ← LE FICHIER À UTILISER
- `image-classification-mnist-emist.ipynb` (ancien fichier, peut être ignoré)
- `data/emnist-letters.mat` (données EMNIST)

## 🎯 Comment Exécuter

### Option 1: Tout Exécuter (Recommandé)
1. Ouvrir `mnist_emnist_classification_clean.ipynb`
2. Cliquer sur "Run All" ou exécuter cellule par cellule
3. Attendre l'entraînement (15-30 minutes selon votre machine)

### Option 2: MNIST Seulement (Plus Rapide - 5-10 minutes)
1. Exécuter les sections 1 et 2 uniquement
2. Ignorer la section 3 (EMNIST)
3. Vous obtiendrez ~99% de précision sur les chiffres

### Option 3: Utiliser les Modèles Pré-entraînés
Si les fichiers `.h5` existent déjà:
```python
from tensorflow.keras.models import load_model
model = load_model('mnist_v13.h5')  # ou emnist_v5.h5
```

## 📊 Résultats Attendus

### MNIST (Chiffres 0-9)
- **Training accuracy**: ~99.9%
- **Validation accuracy**: ~99.6%
- **Test accuracy**: ~99.5%

### EMNIST Letters (Lettres A-Z)
- **Training accuracy**: ~98.7%
- **Validation accuracy**: ~95.1%
- **Test accuracy**: ~94.9%

## 🏗️ Architecture du Réseau

```
Input (28x28x1)
    ↓
Conv2D (32 filtres, 3x3) + ReLU + BatchNorm + MaxPooling
    ↓
Conv2D (64 filtres, 3x3) + ReLU + BatchNorm + MaxPooling + Dropout(0.5)
    ↓
Flatten
    ↓
Dense(1568) + ReLU + BatchNorm + Dropout(0.5)
    ↓
Dense(1000) + ReLU + BatchNorm + Dropout(0.5)
    ↓
Dense(700) + ReLU + BatchNorm + Dropout(0.5)
    ↓
Dense(300) + ReLU + BatchNorm + Dropout(0.5)
    ↓
Dense(100) + ReLU + BatchNorm
    ↓
Dense(10 ou 27) + Softmax
```

**Total**: ~5-6 millions de paramètres

## 🔧 Techniques Utilisées

1. **Batch Normalization** - Évite le problème de vanishing gradient
2. **Dropout (0.5)** - Réduit l'overfitting
3. **Adadelta Optimizer** - Learning rate adaptatif automatique
4. **Early Stopping** - Arrêt automatique si pas d'amélioration
5. **Data Split** - Train (83.3%) / Validation (16.7%) / Test

## ⏱️ Temps d'Exécution

- **MNIST seul**: 5-10 minutes
- **EMNIST seul**: 10-20 minutes
- **Les deux**: 20-30 minutes

*Note: Temps avec CPU. Avec GPU, c'est 5-10x plus rapide*

## 📈 Visualisations Incluses

- Courbes d'accuracy (train vs validation)
- Courbes de loss
- Exemples d'erreurs de classification
- Exemples de prédictions correctes avec confiance

## 🎓 Pour la Présentation

### Points Clés à Mentionner:

1. **Architecture MLP profonde** avec 5 couches fully connected
2. **Techniques modernes**: Batch Normalization, Dropout, Early Stopping
3. **Résultats excellents**: 99.5% sur MNIST, 95% sur EMNIST
4. **Généralisation**: Validation/test splits pour éviter l'overfitting
5. **Optimizer intelligent**: Adadelta (pas besoin de tuner le learning rate)

### Défis Résolus:

- **Vanishing gradient**: Résolu avec Batch Normalization
- **Overfitting**: Résolu avec Dropout et régularisation
- **Learning rate**: Résolu avec Adadelta optimizer
- **Dead ReLU**: Minimisé avec Batch Normalization

## 🐛 Problèmes Courants

### Erreur: "No module named tensorflow"
```bash
pip install tensorflow
```

### Erreur: "File not found: emnist-letters.mat"
Vérifiez que le fichier est dans le dossier `data/`

### Le modèle n'apprend pas bien
- Vérifiez que les données sont normalisées (division par 255)
- Augmentez le nombre d'epochs si nécessaire

## 📞 Aide Rapide

Si vous avez des problèmes:
1. Vérifiez que toutes les bibliothèques sont installées
2. Vérifiez que les données EMNIST sont présentes
3. Utilisez MNIST seul pour tester rapidement
4. Réduisez les epochs à 10 pour un test rapide

## 🎯 Version Minimale (Si Vraiment Pressé)

Si vous manquez vraiment de temps, utilisez seulement la **Section 2 (MNIST)**:
- Temps: 5-10 minutes
- Résultat: 99% de précision
- Suffit largement pour le projet!

---

**Bon courage! 🚀**
