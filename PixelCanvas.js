import React, { useEffect, useRef, useCallback } from 'react'

export function PixelCanvas() {
  const canvasRef = useRef(null)
  const mousePos = useRef({ x: 0, y: 0 })
  const timeRef = useRef(0)
  const requestRef = useRef()

  const animate = useCallback((currentTime) => {
    const canvas = canvasRef.current
    if (!canvas) return

    const ctx = canvas.getContext('2d', { alpha: false })
    if (!ctx) return

    const pixelSize = 30
    const cols = Math.ceil(canvas.width / pixelSize)
    const rows = Math.ceil(canvas.height / pixelSize)

    ctx.fillStyle = 'white'
    ctx.fillRect(0, 0, canvas.width, canvas.height)

    const maxDist = 150
    const time = currentTime * 0.001

    // 计算中心点
    const centerX = canvas.width / 2
    const centerY = canvas.height / 2

    // 计算对称点
    const symmetricX = 2 * centerX - mousePos.current.x
    const symmetricY = 2 * centerY - mousePos.current.y

    for (let i = 0; i < cols; i++) {
      for (let j = 0; j < rows; j++) {
        const x = i * pixelSize
        const y = j * pixelSize
        const dx = x - mousePos.current.x
        const dy = y - mousePos.current.y
        const distToMouse = Math.sqrt(dx * dx + dy * dy)

        const dxSymmetric = x - symmetricX
        const dySymmetric = y - symmetricY
        const distToSymmetric = Math.sqrt(dxSymmetric * dxSymmetric + dySymmetric * dySymmetric)

        if (distToMouse < maxDist) {
          const t = 1 - distToMouse / maxDist
          const hue = (time * 50) % 360
          const saturation = 100
          const lightness = 50 + Math.sin(time * 2 + i * 0.1 + j * 0.1) * 20
          ctx.fillStyle = `hsla(${hue}, ${saturation}%, ${lightness}%, ${t})`
          ctx.fillRect(x, y, pixelSize, pixelSize)
        }

        if (distToSymmetric < maxDist) {
          const t = 1 - distToSymmetric / maxDist
          const hue = ((time * 50) % 360 + 180) % 360 // 互补色
          const saturation = 100
          const lightness = 50 + Math.sin(time * 2 + i * 0.1 + j * 0.1) * 20
          ctx.fillStyle = `hsla(${hue}, ${saturation}%, ${lightness}%, ${t})`
          ctx.fillRect(x, y, pixelSize, pixelSize)
        }
      }
    }

    requestRef.current = requestAnimationFrame(animate)
  }, [])

  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return

    const handleResize = () => {
      canvas.width = window.innerWidth
      canvas.height = window.innerHeight
    }

    const handleMouseMove = (event) => {
      mousePos.current = {
        x: event.clientX,
        y: event.clientY
      }
    }

    handleResize()
    window.addEventListener('resize', handleResize)
    window.addEventListener('mousemove', handleMouseMove, { passive: true })

    requestRef.current = requestAnimationFrame(animate)

    return () => {
      window.removeEventListener('resize', handleResize)
      window.removeEventListener('mousemove', handleMouseMove)
      cancelAnimationFrame(requestRef.current)
    }
  }, [animate])

  return <canvas ref={canvasRef} style={{ width: '100%', height: '100%' }} />
}