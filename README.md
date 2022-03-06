# Trabalhos de Computação Gráfica
## Fase 1
### Exemplos 2D no processing (Java)
Coletânea de trabalhos de computação Gráfica 2021.2
- Sol-Terra-Lua : Adicione a imagem "espaço" um nível acima da pasta com o projeto. Isso fará com que o background do projeto mostre a imagem. 

<img src="https://github.com/viisantos/trabsComputacaoGrafica/blob/main/solTerraLua_funcionando.png" align="center" height="400" width="400">


- Espiral de Arquimedes não interativo : Aqui, temos uma espiral de arquimedes, cuja equação é r=a+b*theta 
    - Referência : https://pt.wikipedia.org/wiki/Espiral_de_Arquimedes

<img src="https://github.com/viisantos/trabsComputacaoGrafica/blob/main/espiral_arquimedes1_funcionando.png" align="center" height="400" width="400">

- Curva de bézier cúbica, segue o mesmo princípio da quadrática, é parametrizada, mas com 6 pontos internos para formação da curva. 
    - Referência : https://pt.wikipedia.org/wiki/Curva_de_Bézier
<img src="https://github.com/viisantos/trabsComputacaoGrafica/blob/main/bezier_grau3.png" align="center" height="400" width="400">

### Exemplos 3D em pyOpenGL e pyGLUT
- Cilindro 
    - Este exemplo é derivado do tronco de pirâmide. A ideia é desenhar duas bases, e um corpo. Este exemplo pode ser facilmente transformado em um prisma alterando-se o número de vértices.
<img src="https://github.com/viisantos/trabsComputacaoGrafica/blob/main/prints_3D_funcionando/cilindro.png" align="center" height="400" width="400">

- Cone
    - O código do cone possui a mesma lógica que o código da pirâmide hexagonal. Na pirâmide hexagonal o código está devidamente comentado. A única diferença é o número de vértices na base.
<img src="https://github.com/viisantos/trabsComputacaoGrafica/blob/main/prints_3D_funcionando/cone.png" align="center" height="400" width="400">

- Pirâmide Hexagonal
<img src="https://github.com/viisantos/trabsComputacaoGrafica/blob/main/prints_3D_funcionando/piramide_hexagonal_comentada.png" align="center" height="400" width="400">

- Prisma
    - Este exemplo é derivado do cilindro. A ideia é desenhar duas bases, e um corpo. A única alteração é no número de vértices das bases. 
<img src="https://github.com/viisantos/trabsComputacaoGrafica/blob/main/prints_3D_funcionando/prisma.png" align="center" height="400" width="400">

- Tronco de pirâmide
<img src="https://github.com/viisantos/trabsComputacaoGrafica/blob/main/prints_3D_funcionando/tronco_piramide_comentado.png" align="center" height="400" width="400">

## Fase 2
### Aplicação de textura em esfera utilizando react-fiber-THREEJS
<img src="https://user-images.githubusercontent.com/47664639/156944340-98dcfa4b-5894-411f-acaa-d67c52b33b54.png" align="center" height="400" width="450">
Para aplicar a textura de globo terrestre, trabalhamos com uma biblioteca do react chamada “react three fiber” - https://docs.pmnd.rs/react-three-fiber/getting-started/introduction , que adiciona ao react algumas funcionalidades vistas no three js, embora estas funcionalidades sejam expressas no código à moda react. 

Sabemos que o react trabalha com componentes. Um menu pode ser um componente, uma página, outra… e assim por diante. A componentização permite reutilização de um mesmo componente em diversos lugares da aplicação.

Então, expressamos cada “primitiva” do three js como uma componente no nosso app react.
em especial, para o mapeamento da textura, utilizamos o “useLoader”, que irá associar cada import à uma variável declarada no array que o antecede, para que possamos utilizar estas variáveis para “forrar” o globo terrestre com a devida textura.

Utilizamos 4 texturas. Cada uma delas diz respeito a um aspecto diferente da imagem. Em especial, temos a textura normal, o mapamundi “basiquinho”, a “normal earth”, que confere uma noção de relevo à imagem, e o “clouds map”, que são as nuvens sobre o globo.

Temos dois blocos “Mesh”. O mesh serve justamente para configurarmos a textura, e, nele, podemos colocar mais itens que irão dar maior sofisticação ao sólido sendo gerado.

Para cada bloco “Mesh”, declaramos  um “sphereGeometry”, de argumentos (raio, num_segmentos_horizontais, num_segmentos_verticais), e um “mashPhongMaterial”, onde inserimos a textura de fato, definindo atributos como opacidade, transparência, depthWrite, que é uma propriedade que pode ser melhor definida pelo exemplo do material sendo mostrado no link da documentação desse elemento: https://threejs.org/docs/?q=meshPhong#api/en/materials/MeshPhongMaterial - Podemos ver que esse atributo, quando setado como True, permite que partes do objeto respeitem a noção de se estar na frente de outra parte.)

Ainda, utilizamos uma textura especial, a “earth-specular”, em um meshPhongMaterial, para que os espaços com água pareçam ter um certo brilho. É uma aplicação de reflexo especular. No projeto, essa funcionalidade não apareceu com muito destaque. Talvez seja porque a imagem do mapa básico seja um pouco escura demais.

Aplicamos ainda o componente “OrbitControls” que serve justamente para que consigamos interagir com nosso planetinha utilizando o mouse, arrastando de um lado, de outro… e podendo aplicar zoom.

### Pirâmide utilizando ThreeJS
<img src="https://user-images.githubusercontent.com/47664639/156946324-77afda37-d0e4-4133-9852-8d03f70795bd.png" align="center" height="400" width="450">

### Prisma utilizando ThreeJS
<img src="https://user-images.githubusercontent.com/47664639/156946424-ce3b95f6-6bd1-4e28-8321-a68c154246e4.png" align="center" height="400" width="450">





p.s : Agradeço aos colegas do curso que disponibilizaram seus repositórios com material de computação gráfica produzido que me auxiliou no desenvolvimento de alguns exemplos 🤝🙃
