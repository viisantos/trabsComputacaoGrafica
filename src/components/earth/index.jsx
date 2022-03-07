import React, {useRef } from 'react';
import { useLoader } from "@react-three/fiber";

//textures
import EarthMap from "../../textures/mapa.png";
import EarthNormal from "../../textures/earth-normal.jpg";
import EarthSpecular from "../../textures/earth-specular.jpg"
import EarthClouds from "../../textures/earth-clouds.jpg";
import * as THREE from "three";

//essa biblioteca faz com que possamos definir órbitas independentes para cada textura. 
//com isso, podemos colocar a textura das nuvens para orbitar de uma forma que possamos enxergar o movimento delas sobre o mapamundi.
import { OrbitControls, Stars} from "@react-three/drei"; 

import { TextureLoader } from "three";

export function Earth(props){
    
  const [earthMap, earthNormal, earthSpecular, cloudsMap] = useLoader(
      TextureLoader, [EarthMap, EarthNormal, EarthSpecular, EarthClouds]);

  return <>
      {/**Removendo o código abaixo,
       * obtemos um efeito incrível, onde podemos ver o brilho do sol 
       * sobre uma face especifica da terra, enquanto demais partes ficam escuras.
       */}
      <ambientLight intensity={1.54} /> 
      <pointLight color="#f6f3ea" position={[2, 0, 2]} intensity={1.4} />
      <Stars radius={300} depth={60} count={20000} factor={7} saturation={0} fade={true} />
      <mesh>
          <sphereGeometry args ={[1, 32, 32]} />
          <meshPhongMaterial
           map={cloudsMap} 
           opacity={0.4} 
           depthWrite={true} 
           transparent={true} 
           side={THREE.DoubleSide} 
           />
      </mesh>
      <mesh> 
        <sphereGeometry args={[1, 32, 32]} />
        <meshPhongMaterial specularMap={earthSpecular} />
        <meshStandardMaterial 
            map={earthMap} 
            normalMap={earthNormal} 
            metalness={0.4}
            roughness={0.7}
        />
        <OrbitControls 
            enableZoom={true} 
            enablePan={true} 
            enableRotate={true} 
            zoomSpeed={0.6} 
            panSpeed={0.5} 
            rotateSpeed={0.4} 
        />
      </mesh>
    </>;
}