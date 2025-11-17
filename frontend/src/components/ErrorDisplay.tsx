interface ErrorDisplayProps {
  error: string;
}

export const ErrorDisplay = ({ error }: ErrorDisplayProps) => {
  return (
    <div className="p-4 rounded-lg bg-red-50 border border-red-200 mb-6 animate-fade-in">
      <p className="text-sm text-red-700">{error}</p>
    </div>
  );
};
