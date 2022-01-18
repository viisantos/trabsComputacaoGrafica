from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
quadro = 0

def desenharPiramideHexagonal():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(quadro,0.0,1.0,0.0) #rotação em torno do eixo y
    #glRotatef(90.0+quadro,1.0,0.0,0.0) #rotação em torno de x, tendo os quadros somados a 90
    raio = 0.7
    n = 6

    glBegin(GL_TRIANGLE_FAN)  # precisamos agora desenhar a "tampa" da piramide. Emitimos "GL_TRIANGLE_FAN"
    glColor3f(0.64, 0.2478, 0.64)
    glVertex3f(0.0, 0.0, 0.0)
    # então, aqui neste "for", realizamos o desenho propriamente dito do "GLTRIANGLE_FAN".
    for i in range(0, n + 1):
        a = (i / n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glVertex3f(x, y, 0.0)
    glEnd()

    glBegin(GL_TRIANGLES)   #inicio da definição do corpo do desenho
    for i in range(0,n):    #Faces
        glColor3fv(cores[(i)%len(cores)]) #colorindo as faces
        glVertex3f(0.0,0.0,1)             #emitindo vértice no z, para destacar a pirâmide.
        a = (i/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glVertex3f(x,y, 0.0)
        a = ((i+1)/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glVertex3f(x,y, 0.0)

        #repare que, "glVertex3f" é chamado 3 vezes a cada iteração.
        #Isso é para que seja possível desenharmos várias facetas de triângulos
    glEnd()

    glutSwapBuffers()
    quadro += 1
    glPopMatrix()

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(10,timer,1)


# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Piramide hexagonal")
glutDisplayFunc(desenharPiramideHexagonal)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
#gluPerspective(45.0,  800.0/600.0,  0.1,       100.0)
glFrustum(-0.5, 0.5, -0.5, 0.5, 1, 10.2) #uma outra maneira de se implementar perspectiva
glTranslatef(0.0,0.0,-5.0)
glutTimerFunc(10,timer,1)
glutMainLoop()


