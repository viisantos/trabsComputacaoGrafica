float a = 0;
PImage bg;

void setup() {
  size(800,800);
  bg = loadImage("../espaco.jpg");
  ellipseMode(CENTER); //modificar a origem da elipse
}
void sol(){
  fill(242,204,47,250);
  circle(0,0,200);
}

void terra(){
  fill(116,193,206,250);
  circle(0,0,50);
}

void lua(){
  translate(0.38*width/4,0); //deslocar o eixo da lua em relacao a uma parte do eixo da terra
  fill(255,255,255,250);
  circle(0,0,20);
}

void draw() {
    background(bg);
    translate(width/2, height/2);  //essa linha tranfsere o centro do universo para o centro da tela.
    //line(-width/2, 0, width/2, 0); //traçar uma linha no eixo X
    //line(0,-height/2, 0,height/2); //traçar uma linha no eixo Y
    
    pushMatrix();
    sol(); 
    popMatrix();
    
    pushMatrix();
    rotate(frameCount/(20*TWO_PI));  //framecount armazena a quantidade de frames contados desde o início do programa.
                                     //20/TWO_PI significa que temos 20 setores circulares.
    
    /* muito importante: devido as regras de operações com matrizes,
    primeiro é feito o translate, ou seja, o círculo é levado para uma posição 
    do eixo y correspondente a 1/4 da parte positiva. 
    basta comentar "rotate" para observar isso.
    depois é feito o rotate. */
    translate(1.4*width/4,0);   
    terra();
    rotate(frameCount/(20*TWO_PI)); 
    pushMatrix();
    lua();
    popMatrix();
    popMatrix();
    
    /* Utilizamos batante o pushMatrix() e o popMatrix().
       A importância desses métodos é empilhar operações de matrizes para armazenar por um tempo o resultado delas
       e desempilhar essas informações a fim de que seja possivel a reversão das mesmas. Basicamente, oferecer flexibilidade quando se desejar voltar 
       a um estado anterior do sistema, sem que seja preciso desfazer manualmente tudo o que foi feito até então, tarefa que seria impossível num projeto grande.
       
       Por exemplo, todas as operações realizadas antes do pushMatrix() serão armazenadas em uma pilha(no topo) que armazena resultados de operações matriciais
       (translações, rotações...), ao passo que, se colocarmos outras operações após esse comando, e em seguida dar um popMatrix(), voltamos o sistema ao estado original
       de antes do pushMatrix(). É uma questão de boas práticas de programação e de operações matriciais. 
       
       Para este projeto, na verdade, não tem tanto efeito, do ponto de vista de estados, utilizar pushMatrix() e popMatrix(). (Confirmar isso).
       Utilizamos apenas para efeito de demonstrar boas práticas de programação gráfica.
    */
}
