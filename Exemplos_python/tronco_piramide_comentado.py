from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a = 0

cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5))


def troncoDePiramide():
    raioBaseMaior = 4
    raioBaseMenor = 2
    qtdVerticesBases = 4
    altura = 4
    pontosBaseMaior = []
    pontosBaseMenor = []

    angulo = (2 * math.pi) / qtdVerticesBases #As bases são poligonos "circulares"

    glPushMatrix()
    glTranslatef(0, -2, 0)
    glRotatef(a, 0.0, 1.0, 0.0)
    glRotatef(-121, 1.0, 0.0, 0.0) #dar uma leve inclinadinha para exibir as bases
    glColor3fv(cores[0])

    # BASES
    glBegin(GL_POLYGON)
    for i in range(0, qtdVerticesBases):
        xBaseMaior = raioBaseMaior * math.cos(i * angulo)
        yBaseMaior = raioBaseMaior * math.sin(i * angulo)
        pontosBaseMaior += [(xBaseMaior, yBaseMaior)]
        glVertex3f(xBaseMaior, yBaseMaior, 0.0)  #emissão de vértices, mas apenas um polígono "no chão"
    glEnd()

    glBegin(GL_POLYGON)
    for j in range(0, qtdVerticesBases):
        xBaseMenor = raioBaseMenor * math.cos(j * angulo)
        yBaseMenor = raioBaseMenor * math.sin(j * angulo)
        pontosBaseMenor += [(xBaseMenor, yBaseMenor)]
        glVertex3f(xBaseMenor, yBaseMenor, altura) #emissão de vértices, porém numa dada altura, que vale 4.
    glEnd()

    # LATERAL
    glBegin(GL_QUAD_STRIP)  #emitir quadriláteros
    for i in range(0, qtdVerticesBases):
        glColor3fv(cores[(i + 1) % len(cores)]) #uma cor para cada face
        glVertex3f(pontosBaseMaior[i][0], pontosBaseMaior[i][1], 0.0) #primeiro parâmetro é x, segundo parâmetro é y
                                                                      #terceiro parâmetro indica que está no chão

        glVertex3f(pontosBaseMaior[(i + 1) % qtdVerticesBases][0], pontosBaseMaior[(i + 1) % qtdVerticesBases][1], 0.0)
        #permite uma distribuição proporcional dos pontos (?)

        glVertex3f(pontosBaseMenor[i][0], pontosBaseMenor[i][1], altura)#primeiro parâmetro é x, segundo parâmetro é y
                                                                        #terceiro parâmetro indica que está na altura dada

        glVertex3f(pontosBaseMenor[(i + 1) % qtdVerticesBases][0], pontosBaseMenor[(i + 1) % qtdVerticesBases][1], altura)
        # permite uma distribuição proporcional dos pontos
    glEnd()

    glPopMatrix()


def desenhaTronco():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    troncoDePiramide()
    a += 1  #permitir o funcionamento da animação
    glutSwapBuffers()


def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10, timer, 1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800, 600)
glutCreateWindow("TRONCO DE PIRAMIDE")
glutDisplayFunc(desenhaTronco)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0, 0, 0, 1)
gluPerspective(85, 800.0 / 600.0, 0.1, 100.0)
glTranslatef(0.0, 0.0, -10)
glutTimerFunc(10, timer, 1)
glutMainLoop()
