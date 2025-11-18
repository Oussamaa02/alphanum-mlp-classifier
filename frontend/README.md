# React Frontend for Character Recognition

Beautiful, simple interface for MNIST/EMNIST character recognition.

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd frontend
npm install --legacy-peer-deps
```

**Note**: Use `--legacy-peer-deps` due to React version compatibility with `react-canvas-draw`.

### 2. Start Development Server

```bash
npm start
```

The app will open at `http://localhost:3000`

## ⚙️ Configuration

The backend API URL can be configured via environment variable:

**Create a `.env` file in the frontend directory:**
```bash
REACT_APP_API_URL=http://localhost:5000
```

Or set it when starting the app:
```bash
REACT_APP_API_URL=http://localhost:5000 npm start
```

For production deployment, set this environment variable on your hosting platform (e.g., Vercel).

## 📝 Features

- ✨ Clean, modern UI with gradient design
- 🎨 Smooth drawing canvas
- 🔢 Switch between digit (0-9) and letter (A-Z) recognition
- 📊 Show top 3 predictions with confidence scores
- 📱 Responsive design for mobile devices
- ⚡ Real-time predictions

## 🛠️ Technologies

- **React 18** - UI framework
- **TypeScript** - Type safety
- **react-canvas-draw** - Drawing canvas library
- **Tailwind CSS** - Styling
- **Fetch API** - HTTP requests to backend

## 📦 Build for Production

```bash
npm run build
```

This creates an optimized production build in the `build/` folder.

## 🚀 Deployment

See [DEPLOYMENT.md](../DEPLOYMENT.md) for detailed deployment instructions to free hosting platforms like Vercel.

## 🐛 Troubleshooting

**Installation errors:**
- Use `npm install --legacy-peer-deps` to resolve peer dependency conflicts

**Canvas not drawing:**
- Check if `react-canvas-draw` is installed: `npm list react-canvas-draw`
- Reinstall: `npm install react-canvas-draw --legacy-peer-deps`

**CORS errors:**
- Make sure Flask backend has CORS enabled (`flask-cors` installed)
- Check that `REACT_APP_API_URL` environment variable is set correctly

**Prediction not working:**
- Open browser console (F12) to see error messages
- Verify backend is running: `curl http://localhost:5000/health`
- Check network tab for failed requests

## 🎨 Customization

### Change Canvas Size

Edit `src/App.tsx`:
```typescript
<CanvasDraw
  canvasWidth={450}  // Change this
  canvasHeight={450} // Change this
  brushRadius={8}    // Change brush size
/>
```

## 🎯 Next Steps

- Deploy frontend to Vercel (free) - See [DEPLOYMENT.md](../DEPLOYMENT.md)
- Deploy backend to Railway/Render (free) - See [DEPLOYMENT.md](../DEPLOYMENT.md)
- Add more features (save drawings, history, etc.)
