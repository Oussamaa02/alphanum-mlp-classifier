# React Frontend for Character Recognition

Beautiful, simple interface for MNIST/EMNIST character recognition.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Start Development Server

```bash
npm start
```

The app will open at `http://localhost:3000`

## ⚙️ Configuration

The backend API URL is set in `src/App.js`:
```javascript
const API_URL = 'http://localhost:5000';
```

Change this if your Flask backend runs on a different port.

## 📝 Features

- ✨ Clean, modern UI with gradient design
- 🎨 Smooth drawing canvas
- 🔢 Switch between digit (0-9) and letter (A-Z) recognition
- 📊 Show top 3 predictions with confidence scores
- 📱 Responsive design for mobile devices
- ⚡ Real-time predictions

## 🛠️ Technologies

- **React 18** - UI framework
- **react-canvas-draw** - Drawing canvas library
- **Fetch API** - HTTP requests to backend

## 📦 Build for Production

```bash
npm run build
```

This creates an optimized production build in the `build/` folder.

## 🐛 Troubleshooting

**Canvas not drawing:**
- Check if `react-canvas-draw` is installed: `npm list react-canvas-draw`
- Reinstall: `npm install react-canvas-draw`

**CORS errors:**
- Make sure Flask backend has CORS enabled (`flask-cors` installed)
- Check that backend is running on `http://localhost:5000`

**Prediction not working:**
- Open browser console (F12) to see error messages
- Verify backend is running: `curl http://localhost:5000/health`
- Check network tab for failed requests

## 🎨 Customization

### Change Colors

Edit `src/App.css`:
```css
.mode-button.active {
  background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
}
```

### Change Canvas Size

Edit `src/App.js`:
```javascript
<CanvasDraw
  canvasWidth={280}  // Change this
  canvasHeight={280} // Change this
  brushRadius={8}    // Change brush size
/>
```

## 📱 Screenshots

[Add screenshots of your app here]

## 🎯 Next Steps

- Deploy frontend to Netlify/Vercel
- Deploy backend to Heroku/Railway
- Add more features (save drawings, history, etc.)
