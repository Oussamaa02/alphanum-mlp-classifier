interface ActionButtonsProps {
  onClear: () => void;
  onPredict: () => void;
  loading: boolean;
}

export const ActionButtons = ({ onClear, onPredict, loading }: ActionButtonsProps) => {
  return (
    <div className="flex gap-3 mb-6">
      <button
        onClick={onClear}
        className="flex-1 py-2.5 px-4 bg-white border border-gray-300 text-gray-700 rounded-lg hover:bg-gray-50 transition-colors duration-200 text-sm font-medium"
      >
        Clear
      </button>
      <button
        onClick={onPredict}
        disabled={loading}
        className="flex-1 py-2.5 px-4 bg-gray-900 text-white rounded-lg hover:bg-gray-800 disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200 text-sm font-medium"
      >
        {loading ? 'Processing...' : 'Predict'}
      </button>
    </div>
  );
};
