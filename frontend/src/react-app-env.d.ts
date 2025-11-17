declare module '*.css' {
  const content: { [className: string]: string };
  export default content;
}

declare module 'react-canvas-draw' {
  import { Component } from 'react';

  interface CanvasDrawProps {
    brushColor?: string;
    brushRadius?: number;
    lazyRadius?: number;
    canvasWidth?: number;
    canvasHeight?: number;
    backgroundColor?: string;
    hideGrid?: boolean;
    className?: string;
    ref?: React.Ref<any>;
  }

  export default class CanvasDraw extends Component<CanvasDrawProps> {
    clear(): void;
    canvas: {
      drawing: HTMLCanvasElement;
    };
  }
}
