from Modelo.Grafo import *
from tkinter import *
from tkinter import ttk
import pygame, sys, random, json


with open('Data/grafos.json') as myJSON:
   myFile = json.load(myJSON)


grafos= []

for grafo in myFile:

    g= Grafo()
        
    for vertice in grafo["vertices"]:
        g.IngresarVertice(vertice)

    for arista in grafo["aristas"]:
        g.IngresarAristas(arista[0],arista[1],arista[2])
    
    
    grafos.append(g)




for vertice in grafos[0].getVertices():
    x= random.randint(20,780)
    y= random.randint(20,480)

    vertice.setCoordenadas([x,y])
    
aristasPrim= grafos[0].Prim()[1]
listaPrim=[]
for arista in aristasPrim:
    temp=[]
    temp.append(grafos[0].ObtenerVertice(arista.getOrigen()).getCoordenadas())
    temp.append(grafos[0].ObtenerVertice(arista.getDestino()).getCoordenadas())
    listaPrim.append(temp)

cont=0
pygame.init()

#Definir colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

size=(800,500)

fuente=pygame.font.Font(None,30)

#Crear ventana
screen=pygame.display.set_mode(size)
#Controlar los FPS
clock=pygame.time.Clock()
#coordenadas donde se mueve
cord_x=400
cord_y=200
#lineas
color = (40, 210, 250)
closed = False
pointlist = [(25, 25), (105, 185)]
width = 1
#velocidad que se mueve
speed_x=3
speed_y=3
listaCoordenadas= []
coordenadasAristas= []
for vertice in grafos[0].getVertices():
        x= random.randint(20,780)
        y= random.randint(20,480)
        """pygame.draw.circle(screen,RED,(x,y),4)"""
        listaCoordenadas.append([x,y, vertice.getDato()])

while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
     #----LOGICA----
    """if (cord_x>720 or cord_x<0):
        speed_x*=-1
    if (cord_y>420 or cord_y<0):
        speed_y*=-1"""
    """cord_x+=speed_x
    cord_y+=speed_y"""
    #----LOGICA----
    #Color de fondo
    screen.fill(WHITE)
    #----ZONA DE DIBUJO-----

    for vertice in grafos[0].getVertices():
        for adyacente in vertice.getListaAdyacentes():
            pygame.draw.line(screen, color, (vertice.getCoordenadas()[0],vertice.getCoordenadas()[1]),(adyacente.getCoordenadas()[0],adyacente.getCoordenadas()[1]), width)
        
        texto=fuente.render(vertice.getDato(),0,BLUE)
        pygame.draw.circle(screen,RED,vertice.getCoordenadas(),25)
        screen.blit(texto,[vertice.getCoordenadas()[0]-11, vertice.getCoordenadas()[1]-7])
    
    """if cont<len(listaPrim):
        cont+=1
        for i in range(0, cont):
            arista= listaPrim[i]
            pygame.draw.line(screen,RED,(arista[0][0],arista[0][1]),(arista[1][0],arista[1][1]),width)
            pygame.display.flip()
            clock.tick(0.5)"""
    if cont<1:
        for arista in listaPrim:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            pygame.draw.line(screen,RED,(arista[0][0],arista[0][1]),(arista[1][0],arista[1][1]),width)
            cord_x=arista[0][0]
            cord_y=arista[0][1]
            while cord_x<arista[0][0] and cord_y<arista[1][1]:
                cord_x+=speed_x
                cord_y+=speed_y
                pygame.draw.rect(screen, GREEN,(cord_x,cord_y,50,50))
                pygame.display.flip()
                clock.tick(60)

            pygame.display.flip()
            clock.tick(1)
        cont+=1
    else:
        for arista in listaPrim:
            pygame.draw.line(screen,RED,(arista[0][0],arista[0][1]),(arista[1][0],arista[1][1]),width)
            
    
    """for x in range(100,700,100):
        pygame.draw.rect(screen, GREEN,(x,430,50,50))
        pygame.draw.rect(screen, GREEN,(x,230,50,50))"""
    #----ZONA DE DIBUJO-----
    #actualizar pantalla
    pygame.display.flip()
    clock.tick(60)


    