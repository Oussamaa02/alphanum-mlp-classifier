import { useState, useRef } from 'react';
import CanvasDraw from 'react-canvas-draw';
import { predictCharacter, canvasToBase64, Mode, PredictionResult } from './api/_index';
import {
  ModeSelector,
  ActionButtons,
  PredictionDisplay,
  ErrorDisplay,
  Instructions,
} from './components/_index';

function App() {
  const [mode, setMode] = useState<Mode>('digit');
  const [prediction, setPrediction] = useState<PredictionResult | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const [error, setError] = useState<string | null>(null);
  const canvasRef = useRef<CanvasDraw>(null);

  const clearCanvas = (): void => {
    if (canvasRef.current) {
      canvasRef.current.clear();
      setPrediction(null);
      setError(null);
    }
  };

  const handleModeChange = (newMode: Mode): void => {
    setMode(newMode);
    clearCanvas();
  };

  const handlePredict = async (): Promise<void> => {
    if (!canvasRef.current) return;

    setLoading(true);
    setError(null);
    setPrediction(null);

    try {
      const canvas = (canvasRef.current as any).canvas.drawing as HTMLCanvasElement;
      const canvasData = canvasToBase64(canvas);
      const result = await predictCharacter(canvasData, mode);

      setPrediction(result);
    } catch (err) {
      const errorMessage = err instanceof Error 
        ? err.message 
        : 'Failed to get prediction. Make sure backend is running!';
      setError(errorMessage);
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 flex items-center justify-center p-8">
      <div className="bg-white rounded-2xl shadow-xl max-w-6xl w-full overflow-hidden">
        <div className="bg-gray-900 text-white p-6 border-b border-gray-200">
          <h1 className="text-2xl font-light tracking-wide text-center">
            Character Recognition
          </h1>
        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-0">
          <div className="p-8 bg-white border-r border-gray-100">
            <ModeSelector mode={mode} onModeChange={handleModeChange} />

            <div className="mb-6 rounded-lg overflow-hidden border border-gray-200 bg-white">
              <CanvasDraw
                ref={canvasRef}
                brushColor="#000"
                brushRadius={8}
                lazyRadius={0}
                canvasWidth={450}
                canvasHeight={450}
                backgroundColor="#fff"
                hideGrid={true}
              />
            </div>

            <ActionButtons 
              onClear={clearCanvas} 
              onPredict={handlePredict} 
              loading={loading} 
            />
          </div>

          <div className="p-8 bg-gray-50 flex flex-col">
            <div className="flex-1">
              <h2 className="text-lg font-medium text-gray-900 mb-6">
                Prediction Results
              </h2>

              {error && <ErrorDisplay error={error} />}

              {prediction && prediction.success && (
                <PredictionDisplay prediction={prediction} mode={mode} />
              )}

              {!error && !prediction && (
                <div className="text-center py-12 text-gray-400">
                  <svg className="w-16 h-16 mx-auto mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1} d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                  </svg>
                  <p className="text-sm">Draw a character and click predict</p>
                </div>
              )}
            </div>

            <Instructions />
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
