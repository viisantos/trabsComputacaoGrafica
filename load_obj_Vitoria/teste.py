from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from OBJFileLoader import *

#Para permitir a exibição do coelho, coloquei o seguinte no início
#das declarações de faces: usemtl white. Ou seja, a cor do material 
#base sendo utilizado no coelho.

#Mas podemos ajustar, no init, o material do coelho, a cor dele...

x = 100

def display():
    global obj, x
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(1,1,3,0)

    glPushMatrix()
    obj.draw()
    glPopMatrix()

    glPushMatrix()
    glTranslate(x,10,-80)
    obj.draw()
    glPopMatrix()
    glutSwapBuffers()

    x = x-0.5

def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45,float(w)/float(h),0.1,200.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

    #Se rodarmos o código, simplesmente carregando o .obj, o coelho
    #irá aparecer muito pequenininho.
    #Então, a grande sacada para ajustar este código para
    #a exibição o coelho é
    #alterar o z do "eye", permitindo que o coelho fique mais próximo ao observador
    gluLookAt(0,0.3,0.3,  0,0,0,  0,1,0)

def init():
    global obj
    
    #Definindo iluminação
    glLightfv(GL_LIGHT0, GL_POSITION,   (5, 5, 5, 1.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.4, 0.4, 0.4, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (0.6, 0.6, 0.6, 1.0))

    glEnable(GL_LIGHT0)
    glEnable(GL_LIGHTING)
    glEnable(GL_COLOR_MATERIAL)
    glClearColor(0.0,0.0,0.0,0.0)
    glShadeModel(GL_SMOOTH)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_MULTISAMPLE)
    obj = OBJ("bunny.obj")

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
    glutInitWindowSize(800,600)
    glutCreateWindow("Stanford's Bunny")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    glutTimerFunc(50,timer,1)
    init()
    glutMainLoop()

main()
