from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )
quadro = 0

def desenha():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glPushMatrix()
    glRotatef(quadro,0.0,1.0,0.0)
   # glRotatef(90.0+quadro,1.0,0.0,0.0)
    raio = 0.7
    n = 100 #mudança feita em relação ao exemplo fornecido pelo professor.

    #o código abaixo possui a mesma lógica que o código da pirâmide hexagonal. Lá, o código está devidamente comentado.
    glBegin(GL_TRIANGLES)    
    for i in range(0,n): # Faces
	    glColor3fv(cores[(i)%len(cores)])
	    glVertex3f(0.0,0.0,-1.0)
	    a = (i/n) * 2 * math.pi
	    x = raio * math.cos(a)
	    y = raio * math.sin(a)
	    glVertex3f(x,y,0.0)
	    a = ((i+1)/n) * 2 * math.pi
	    x = raio * math.cos(a)
	    y = raio * math.sin(a)
	    glVertex3f(x,y,0.0)
    glEnd()
    glBegin(GL_TRIANGLE_FAN)    
    glColor3f(0.3,0.3,0.3)
    glVertex3f(0.0,0.0,0.0)
    for i in range(0,n+1):
	    a = (i/n) * 2 * math.pi
	    x = raio * math.cos(a)
	    y = raio * math.sin(a)
	    glVertex3f(x,y,0.0)
    glEnd()
    glutSwapBuffers()
    quadro += 1
    glPopMatrix()
    
def desenha2():
    global quadro
    glClear(GL_COLOR_BUFFER_BIT ) 
    glPushMatrix()
    glRotatef(quadro,0.0,1.0,0.0)
    glRotatef(90.0,1.0,0.0,0.0)
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv(cores[0])
    glVertex3f(0.0,0.0,-1.0)
    raio = 0.7
    n = 5
    for i in range(0,n+1):
        a = (i/n) * 2 * math.pi
        x = raio * math.cos(a)
        y = raio * math.sin(a)
        glColor3fv(cores[(i+1)%len(cores)])
        glVertex3f(x,y,0.0)
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
glutCreateWindow("CONE")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45.0,  800.0/600.0,  0.1,       100.0)
glTranslatef(0.0,0.0,-5.0)
glutTimerFunc(10,timer,1)
glutMainLoop()


