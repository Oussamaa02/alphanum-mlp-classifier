import { Mode, PredictionResult } from '../api/_index';

interface PredictionDisplayProps {
  prediction: PredictionResult;
  mode: Mode;
}

export const PredictionDisplay = ({ prediction, mode }: PredictionDisplayProps) => {
  return (
    <div className="p-6 rounded-lg bg-white border border-gray-200 mb-6 animate-fade-in">
      <div className="mb-6">
        <p className="text-sm text-gray-500 mb-1">Predicted Character</p>
        <h2 className="text-5xl font-light text-gray-900">
          {prediction.prediction}
        </h2>
        <p className="text-sm text-gray-600 mt-2">
          {(prediction.confidence * 100).toFixed(1)}% confidence
        </p>
      </div>

      {/* Top 3 Predictions */}
      {prediction.top_3 && (
        <div>
          <p className="text-xs font-medium text-gray-500 uppercase tracking-wide mb-3">
            Top Predictions
          </p>
          <div className="space-y-2">
            {prediction.top_3.map((item, idx) => (
              <div
                key={idx}
                className="flex justify-between items-center py-2 border-b border-gray-100 last:border-0"
              >
                <span className="text-sm font-medium text-gray-700">
                  {mode === 'digit' ? item.digit : item.letter}
                </span>
                <span className="text-sm text-gray-500">
                  {(item.confidence * 100).toFixed(1)}%
                </span>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
