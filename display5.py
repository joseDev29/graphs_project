from Modelo.Grafo import *
from tkinter import *
from tkinter import ttk
from copy import copy
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



def obtenerFuncion(coordenadas, posX):
    x1=coordenadas[0]
    x2=coordenadas[2]
    y1=coordenadas[1]
    y2=coordenadas[3]

    funcion= (((y2-y1)//(x2-x1))*(posX-x1))+y1
    return funcion



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
    print(temp)
    listaPrim.append(temp)





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

#lineas
color = (40, 210, 250)
closed = False
pointlist = [(25, 25), (105, 185)]
width = 1

listaCoordenadas= []

for vertice in grafos[0].getVertices():
        x= random.randint(20,780)
        y= random.randint(20,480)
        listaCoordenadas.append([x,y, vertice.getDato()])

cm=100; ini=True; cont=0; posPrim=0


while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)

    for vertice in grafos[0].getVertices():
        for adyacente in vertice.getListaAdyacentes():
            pygame.draw.line(screen, color, (vertice.getCoordenadas()[0],vertice.getCoordenadas()[1]),(adyacente.getCoordenadas()[0],adyacente.getCoordenadas()[1]), width)

        texto=fuente.render(vertice.getDato(),0,BLUE)
        pygame.draw.circle(screen,BLACK,vertice.getCoordenadas(),24)
        pygame.draw.circle(screen,RED,vertice.getCoordenadas(),22)
        screen.blit(texto,[vertice.getCoordenadas()[0]-11, vertice.getCoordenadas()[1]-7])


    if cont<1:
        for arista in listaPrim:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            pygame.draw.line(screen,RED,(arista[0][0],arista[0][1]),(arista[1][0],arista[1][1]),1)
            pygame.display.flip()
            clock.tick(2)
        cont+=1
        for vertice in grafos[0].getVertices():
            texto=fuente.render(vertice.getDato(),0,BLUE)
            pygame.draw.circle(screen,BLACK,vertice.getCoordenadas(),24)
            pygame.draw.circle(screen,RED,vertice.getCoordenadas(),22)
            screen.blit(texto,[vertice.getCoordenadas()[0]-11, vertice.getCoordenadas()[1]-7])
    else:
        for arista in listaPrim:
            pygame.draw.line(screen,RED,(arista[0][0],arista[0][1]),(arista[1][0],arista[1][1]),1)
        for vertice in grafos[0].getVertices():
            texto=fuente.render(vertice.getDato(),0,BLUE)
            pygame.draw.circle(screen,BLACK,vertice.getCoordenadas(),24)
            pygame.draw.circle(screen,RED,vertice.getCoordenadas(),22)
            screen.blit(texto,[vertice.getCoordenadas()[0]-11, vertice.getCoordenadas()[1]-7])
        if posPrim<len(listaPrim):
            x1=copy(listaPrim[posPrim][0][0])
            y1=copy(listaPrim[posPrim][0][1])
            x2=copy(listaPrim[posPrim][1][0])
            y2=copy(listaPrim[posPrim][1][1])

            arista= listaPrim[posPrim]
            if ini:
                x=arista[0][0]
                y=arista[0][1]

            funcion= int((((y2-y1)/(x2-x1))*((x)-x1))+y1)
            ini=False
            print("Funcion: {0}".format(funcion))
            if x2==x1 and y2<y1:
                y-=1
                print('caso 1')
            elif x2>x1 and y2<y1:
                x+=1
                y-= y-funcion
                print('caso 2')
                if(x>=x2):
                    posPrim+=1
                    ini=True
            elif x2>x1 and y2==y1:
                x+=1
                print('caso 3')
            elif x2>x1 and y2>y1:
                x+=1
                y+= funcion-y
                print('caso 4')
                if(x>=x2):
                    posPrim+=1
                    ini=True
            elif x2==x1 and y2>y1:
                y+=1
                print('caso 5')
            elif x2<x1 and y2>y1:
                x-=1
                y+= funcion-y
                print('caso 6')
                if(x<=x2):
                    posPrim+=1
                    ini=True
            elif x2<x1 and y2==y1:
                x-=1
                print('caso 7')
            elif x2<x1 and y2<y1:
                x-=1
                y-= y-funcion
                print('caso 8')
                if(x<=x2):
                    posPrim+=1
                    ini=True
            else:
                print('nada')


            pygame.draw.circle(screen,BLACK,[x,y],10)




    pygame.display.flip()
    clock.tick(30)

"""for i in range(20):
        pygame.draw.circle(screen,BLACK,[cm,cm],10)
        cm+=10
        print('ya')"""