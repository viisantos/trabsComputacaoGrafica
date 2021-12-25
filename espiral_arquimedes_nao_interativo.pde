int pontos_por_volta = 250;
float ang = TWO_PI/pontos_por_volta; //definimos que queremos emitir 20 pontos por volta.
                       //portanto, queremos dividir uma volta completa(2pi)
                       //por 20 setores circulares.
int num_voltas = 10;
float theta;           //este é o ângulo. Ele deverá ser atualizado a cada volta completa.
float raio = 0.8*width/2;

void setup()
{
 size(800,800);
 frameRate(500); //taxa de atualização de quadros
 background(176,196,222);
}

float funcaoRaio(float t, int volta){
  return volta + (5*t);   //espiral de arquimedes
                          //"5" é a distância das curvaturas em cada volta.
}

void draw()
{
stroke(72,61,139); //setar cor de arestas ou pontos.
/*
if(ang < TWO_PI*2){ //talvez não passe de pi por causa dos ângulos primos (?)
  point(width/2 + cos(ang)*u, height/2 + sin(ang)*u);
  ang = ang + 0.01;
  u = u + 0.15;}
 */

translate(width/2, height/2);
beginShape(); //Serve para definirmos formas personalizadas.
              //experimentamos a remoção desse comando aqui, e, sem ele
              //não conseguimos desenhar o formato que desejamos.

  for(int v = 0; v < num_voltas; v++){
    for(int p = 0; p < pontos_por_volta; p++){
      theta = (TWO_PI*v) + (p * ang);
      raio = funcaoRaio(theta,v);
      fill(176,196,222);
      vertex(raio*cos(theta), raio*sin(theta));
    }
  }

endShape();
 
}
