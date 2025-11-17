export const Instructions = () => {
  return (
    <div className="p-6 rounded-lg bg-gray-100 border border-gray-200">
      <p className="text-xs font-medium text-gray-500 uppercase tracking-wide mb-3">
        Tips for Better Results
      </p>
      <ul className="space-y-2 text-sm text-gray-700">
        <li className="flex items-start">
          <span className="text-gray-400 mr-2">•</span>
          <span>Draw large and centered</span>
        </li>
        <li className="flex items-start">
          <span className="text-gray-400 mr-2">•</span>
          <span>Use bold strokes</span>
        </li>
        <li className="flex items-start">
          <span className="text-gray-400 mr-2">•</span>
          <span>Clear canvas between characters</span>
        </li>
      </ul>
    </div>
  );
};
