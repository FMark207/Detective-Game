import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import DetectiveGame from './DetectiveGame.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <DetectiveGame></DetectiveGame>
  </StrictMode>,
)
