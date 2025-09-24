import { useEffect, useRef } from 'react';
import './Banner.css';

const Banner = () => {
  const canvasRef = useRef(null);
  const mousePos = useRef({ x: 0, y: 0 });
  const requestRef = useRef();

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const animate = (currentTime) => {
      const ctx = canvas.getContext('2d', { alpha: false });
      if (!ctx) return;

      const pixelSize = 50; // 增大像素大小 from 30 to 50
      const cols = Math.ceil(canvas.width / pixelSize);
      const rows = Math.ceil(canvas.height / pixelSize);

      // Clear canvas with white background
      ctx.fillStyle = 'white';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      const maxDist = 250; // 增大渐变范围 from 150 to 250
      const time = currentTime * 0.001;

      // Calculate center point
      const centerX = canvas.width / 2;
      const centerY = canvas.height / 2;

      // Calculate symmetric point
      const symmetricX = 2 * centerX - mousePos.current.x;
      const symmetricY = 2 * centerY - mousePos.current.y;

      for (let i = 0; i < cols; i++) {
        for (let j = 0; j < rows; j++) {
          const x = i * pixelSize;
          const y = j * pixelSize;

          // Distance to mouse
          const dx = x - mousePos.current.x;
          const dy = y - mousePos.current.y;
          const distToMouse = Math.sqrt(dx * dx + dy * dy);

          // Distance to symmetric point
          const dxSymmetric = x - symmetricX;
          const dySymmetric = y - symmetricY;
          const distToSymmetric = Math.sqrt(dxSymmetric * dxSymmetric + dySymmetric * dySymmetric);

          // Draw pixel if within range of mouse
          if (distToMouse < maxDist) {
            const t = 1 - distToMouse / maxDist;
            const hue = (time * 50) % 360;
            const saturation = 100;
            const lightness = 50 + Math.sin(time * 2 + i * 0.1 + j * 0.1) * 20;
            ctx.fillStyle = `hsla(${hue}, ${saturation}%, ${lightness}%, ${t})`;
            ctx.fillRect(x, y, pixelSize, pixelSize);
          }

          // Draw pixel if within range of symmetric point
          if (distToSymmetric < maxDist) {
            const t = 1 - distToSymmetric / maxDist;
            const hue = ((time * 50) % 360 + 180) % 360; // Complementary color
            const saturation = 100;
            const lightness = 50 + Math.sin(time * 2 + i * 0.1 + j * 0.1) * 20;
            ctx.fillStyle = `hsla(${hue}, ${saturation}%, ${lightness}%, ${t})`;
            ctx.fillRect(x, y, pixelSize, pixelSize);
          }
        }
      }

      requestRef.current = requestAnimationFrame(animate);
    };

    const handleResize = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    };

    const handleMouseMove = (event) => {
      mousePos.current = {
        x: event.clientX,
        y: event.clientY
      };
    };

    // Initialize
    handleResize();
    window.addEventListener('resize', handleResize);
    window.addEventListener('mousemove', handleMouseMove, { passive: true });
    requestRef.current = requestAnimationFrame(animate);

    // Cleanup
    return () => {
      window.removeEventListener('resize', handleResize);
      window.removeEventListener('mousemove', handleMouseMove);
      if (requestRef.current) {
        cancelAnimationFrame(requestRef.current);
      }
    };
  }, []);

  return (
    <div className="banner">
      <canvas ref={canvasRef} className="banner-canvas" />
      <div className="banner-content">
        <h1 className="banner-title">RISSE @ SIT</h1>
        <p className="banner-subtitle">Research in Software Engineering for the Future</p>
      </div>
    </div>
  );
};

export default Banner;