from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

a = 0
cores = ((1, 0, 0), (1, 1, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1), (1, 0, 1), (0.5, 1, 1), (1, 0, 0.5))

#Este exemplo é derivado do cilindro. A ideia é desenhar duas bases, e um corpo.
#Aqui, alteramos somente o número de vértices das bases.
#Aqui, temos um prisma de bases pentagonais

def cilindro():
    raio = 0.5
    verticesBases = 5
    theta = (2 * math.pi) / verticesBases  # As bases são poligonos "circulares"
    pontosBaseBaixa = []
    pontosBaseAlta = []


    glPushMatrix()
    glTranslatef(0, -1, 0)
    glRotatef(a, 0.0, 1.0, 0.0)
    glRotatef(-121, 1.0, 0.0, 0.0)  # dar uma leve inclinadinha para exibir as bases
    glColor3fv(cores[0])


    #BASE ALTA
    glBegin(GL_POLYGON)
    for i in range(0, verticesBases):
        xBaseAlta = raio * math.cos(i * theta)
        yBaseAlta = raio * math.sin(i * theta)
        pontosBaseAlta += [(xBaseAlta, yBaseAlta)]
        glVertex3f(xBaseAlta, yBaseAlta, 1.0)  # emissão de vértices, mas apenas um polígono na altura 5
    glEnd()

    # BASE BAIXA
    glBegin(GL_POLYGON)
    for i in range(0, verticesBases):
        xBaseBaixa = raio * math.cos(i * theta)
        yBaseBaixa = raio * math.sin(i * theta)
        pontosBaseBaixa += [(xBaseBaixa, yBaseBaixa)]
        glVertex3f(xBaseBaixa, yBaseBaixa, 0.0)  # emissão de vértices, mas apenas um polígono "no chão"
    glEnd()

    # LATERAL
    glBegin(GL_QUAD_STRIP)  # emitir quadriláteros
    for i in range(0, verticesBases):
        glColor3fv(cores[(i + 1) % len(cores)])  # uma cor para cada face
        glVertex3f(pontosBaseBaixa[i][0], pontosBaseBaixa[i][1], 0.0)  # primeiro parâmetro é x, segundo parâmetro é y
        # terceiro parâmetro indica que está no chão

        glVertex3f(pontosBaseBaixa[(i + 1) % verticesBases][0], pontosBaseBaixa[(i + 1) % verticesBases][1], 0.0)
        # permite uma distribuição proporcional dos pontos (?)

        glVertex3f(pontosBaseAlta[i][0], pontosBaseAlta[i][1],
                   1.0)  # primeiro parâmetro é x, segundo parâmetro é y
        # terceiro parâmetro indica que está na altura 5

        glVertex3f(pontosBaseAlta[(i + 1) % verticesBases][0], pontosBaseAlta[(i + 1) % verticesBases][1],
                   1.0)
        # permite uma distribuição proporcional dos pontos
    glEnd()

    glPopMatrix()

def desenhar_cilindro():
    global a
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    cilindro()
    a += 1
    glutSwapBuffers()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("CILINDRO")
glutDisplayFunc(desenhar_cilindro)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45.0,  800.0/600.0,  0.1,       100.0)
glTranslatef(0.0,0.0,-5)
glutTimerFunc(50,timer,1)
glutMainLoop()


