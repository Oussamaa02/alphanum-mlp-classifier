const API_URL = 'http://localhost:5000';

export type Mode = 'digit' | 'letter';

export interface TopPrediction {
  digit?: string;
  letter?: string;
  confidence: number;
}

export interface PredictionResult {
  success: boolean;
  prediction: string;
  confidence: number;
  top_3?: TopPrediction[];
}


export const canvasToBase64 = (canvas: HTMLCanvasElement): string => {
  const outputCanvas = document.createElement('canvas');
  outputCanvas.width = canvas.width;
  outputCanvas.height = canvas.height;
  const ctx = outputCanvas.getContext('2d');
  
  if (!ctx) {
    throw new Error('Failed to get canvas context');
  }
  
  ctx.fillStyle = '#FFFFFF';
  ctx.fillRect(0, 0, outputCanvas.width, outputCanvas.height);
  
  ctx.drawImage(canvas, 0, 0);
  
  return outputCanvas.toDataURL('image/png');
};


export const predictCharacter = async (
  canvasData: string,
  mode: Mode
): Promise<PredictionResult> => {
  console.log('📤 Sending canvas data, length:', canvasData.length);

  const endpoint = mode === 'digit' ? '/predict/digit' : '/predict/letter';
  const response = await fetch(`${API_URL}${endpoint}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ image: canvasData }),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.error || 'Prediction failed');
  }

  const result: PredictionResult = await response.json();
  console.log('📥 Received prediction:', result);
  
  return result;
};
