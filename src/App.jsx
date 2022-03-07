import './App.css';
import styled from "styled-components";
import { Canvas } from "@react-three/fiber";
import { Suspense } from "react";
import { Earth } from "./components/earth";

const CanvasContainer = styled.div`
  width: 1024px;
  height: 800px;
`;

function App() {
  return (<CanvasContainer>
    <Canvas>
      <Suspense fallback={null}>
        <Earth />
      </Suspense>
    </Canvas>
  </CanvasContainer>
  );
}

export default App;
