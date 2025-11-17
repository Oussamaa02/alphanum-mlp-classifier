import { Mode } from '../api/_index';

interface ModeSelectorProps {
  mode: Mode;
  onModeChange: (mode: Mode) => void;
}

export const ModeSelector = ({ mode, onModeChange }: ModeSelectorProps) => {
  return (
    <div className="flex gap-2 mb-6 p-1 bg-gray-100 rounded-lg">
      <button
        className={`flex-1 py-2.5 px-4 rounded-md text-sm font-medium transition-all duration-200 ${
          mode === 'digit'
            ? 'bg-gray-900 text-white shadow-sm'
            : 'text-gray-600 hover:text-gray-900'
        }`}
        onClick={() => onModeChange('digit')}
      >
        Digits
      </button>
      <button
        className={`flex-1 py-2.5 px-4 rounded-md text-sm font-medium transition-all duration-200 ${
          mode === 'letter'
            ? 'bg-gray-900 text-white shadow-sm'
            : 'text-gray-600 hover:text-gray-900'
        }`}
        onClick={() => onModeChange('letter')}
      >
        Letters
      </button>
    </div>
  );
};
