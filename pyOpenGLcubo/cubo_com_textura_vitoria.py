#defeito neste código: localizar o 2. e visualizar o cubo nas  coordenadas


from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import png

# Some api in the chain is translating the keystrokes to this octal string
# so instead of saying: ESCAPE = 27, we use the following.
ESCAPE = b'\033'

# Number of the glut window.
window = 0

# Rotations for cube. 
xrot = yrot = zrot = 0.0
dx = 0.1
dy = 0
dz = 0

# texture = []

def LoadTextures():
    #carregar textura e definir um id para ela. O uso do id permite que possamos utilizar mais de uma textura no código.
    global texture
    texture = [ glGenTextures(1) ]

    ################################################################################
    #vamos trabalhar com texture[0], afinal, além de ser essa a posição onde se encontra a textura em uso,
    #iremos utilizar apenas uma textura
    glBindTexture(GL_TEXTURE_2D, texture[0])
    reader = png.Reader(filename='../texturas/dado.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    ################################################################################


def InitGL(Width, Height):             
    LoadTextures()
    glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0.0) 
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)               
    glEnable(GL_DEPTH_TEST)            
    glShadeModel(GL_SMOOTH)            
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0:                        
        Height = 1
    glViewport(0, 0, Width, Height)      
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
    global xrot, yrot, zrot, texture

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)    
    glLoadIdentity()                   
    glClearColor(0.5,0.5,0.5,1.0)            
    glTranslatef(0.0,0.0,-5.0)
    glRotatef(xrot,1.0,0.0,0.0)          
    glRotatef(yrot,0.0,1.0,0.0)           
    glRotatef(zrot,0.0,0.0,1.0) 
    

    #Este trecho do código é o ponto chave.
    #Aqui, faremos a textura funcionar no cubo
    #através do mapeamento dela.
    #temos as posições dos vértices do cubo,
    #mas também devemos mapear algumas coordenadas da 
    #nossa textura para que a mesma se encaixe no cubo da forma 
    #como nós queremos.
    glBindTexture(GL_TEXTURE_2D, texture[0])

    #Vamos emitir a primitiva "quads", emitir 4 vértices para que a mesma renderize,
    #e iremos mapear a textura, informando coordenadas que se adequem aos vértices de nosso cubo.
    glBegin(GL_QUADS)              
    
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0,  1.0)    
    glTexCoord2f(1/3, 0.0); glVertex3f( 1.0, -1.0,  1.0)   
    glTexCoord2f(1/3, 1/2); glVertex3f( 1.0,  1.0,  1.0)   
    glTexCoord2f(0.0, 1/2); glVertex3f(-1.0,  1.0,  1.0)  

    # Back Face
    glTexCoord2f(1/3, 0.0); glVertex3f(-1.0, -1.0, -1.0)    
    glTexCoord2f(2/3, 0.0); glVertex3f(-1.0,  1.0, -1.0)    
    glTexCoord2f(2/3, 1/2); glVertex3f( 1.0,  1.0, -1.0)    
    glTexCoord2f(1/3, 1/2); glVertex3f( 1.0, -1.0, -1.0)   
    
    # Top Face
    glTexCoord2f(2/3, 0.0); glVertex3f(-1.0,  1.0, -1.0)   
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0,  1.0,  1.0)    
    glTexCoord2f(1.0, 1/2); glVertex3f( 1.0,  1.0,  1.0)    
    glTexCoord2f(2/3, 1/2); glVertex3f( 1.0,  1.0, -1.0)   

    # Bottom Face       
    glTexCoord2f(0, 1/2); glVertex3f(-1.0, -1.0, -1.0)   
    glTexCoord2f(1/3, 1/2); glVertex3f( 1.0, -1.0, -1.0)   
    glTexCoord2f(1/3, 1); glVertex3f( 1.0, -1.0,  1.0)   
    glTexCoord2f(0, 1.0); glVertex3f(-1.0, -1.0,  1.0)    
    
    # Right face
    glTexCoord2f(1/3, 1/2); glVertex3f( 1.0, -1.0, -1.0)    
    glTexCoord2f(2/3, 1/2); glVertex3f( 1.0,  1.0, -1.0)   
    glTexCoord2f(2/3, 1.0); glVertex3f( 1.0,  1.0,  1.0)    
    glTexCoord2f(1/3, 1.0); glVertex3f( 1.0, -1.0,  1.0)  
    
    # Left Face
    glTexCoord2f(2/3, 1/2); glVertex3f(-1.0, -1.0, -1.0)  
    glTexCoord2f(1.0, 1/2); glVertex3f(-1.0, -1.0,  1.0)    
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0,  1.0,  1.0)   
    glTexCoord2f(2/3, 1.0); glVertex3f(-1.0,  1.0, -1.0)   
    
    glEnd()                # Done Drawing The Cube
    
    xrot = xrot + 0.01                # X rotation
    yrot = yrot + 0.01                 # Y rotation
    zrot = zrot + 0.01                 # Z rotation

    glutSwapBuffers()

#As funções a seguir permitem que interajamos com o cubo através do mouse.
def keyPressed(tecla, x, y):
    global dx, dy, dz
    if tecla == ESCAPE:
        glutLeaveMainLoop()
    elif tecla == b'x' or tecla == b'X':
        dx = 1.0
        dy = 0
        dz = 0   
    elif tecla == b'y' or tecla == b'Y':
        dx = 0
        dy = 1.0
        dz = 0   
    elif tecla == b'z' or tecla == b'Z':
        dx = 0
        dy = 0
        dz = 1.0

def teclaEspecialPressionada(tecla, x, y):
    global xrot, yrot, zrot, dx, dy, dz
    if tecla == GLUT_KEY_LEFT:
        print ("ESQUERDA")
        xrot -= dx                # X rotation
        yrot -= dy                 # Y rotation
        zrot -= dz                     
    elif tecla == GLUT_KEY_RIGHT:
        print ("DIREITA")
        xrot += dx                # X rotation
        yrot += dy                 # Y rotation
        zrot += dz                     
    elif tecla == GLUT_KEY_UP:
        print ("CIMA")
    elif tecla == GLUT_KEY_DOWN:
        print ("BAIXO")


#A main dispara as demais funções
def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)    
    glutInitWindowSize(640, 480)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("DADO")
    glutDisplayFunc(DrawGLScene)
    glutIdleFunc(DrawGLScene)
    glutReshapeFunc(ReSizeGLScene)
    glutKeyboardFunc(keyPressed)
    glutSpecialFunc(teclaEspecialPressionada)
    InitGL(640, 480)
    glutMainLoop()


main()
