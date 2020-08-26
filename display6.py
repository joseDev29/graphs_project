from Modelo.Grafo import *
from tkinter import *
from tkinter import ttk
from copy import copy
import pygame, sys, random, json, math


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

myGraph= grafos[0]
unidad=int(math.sqrt((800**2 + 500**2))/myGraph.pesoTotal())
print(unidad)
aristas= myGraph.getAristas()
vertices=[]
coordenadasMarcadas=[]
for arista in aristas:

    peso= arista.getPeso()*unidad

    if len(vertices)<=0:
        origen= myGraph.ObtenerVertice(arista.getOrigen()).setCoordenadas([40,40])
        vertices.append(arista.getOrigen().getDato())
    else:
        print('nada')
        

class Mapeador():
    def __init__(self, unidadEspacio, pantalla):
        self.unidadEspacio= unidadEspacio
        self.coordenadasVertices=[]
        self.pantalla=[]
        self.coordenadasNoDisponibles=[]


    
    def mapearVertice(self, origen, distancia):

        limites=[[origen[0], origen[1]-distancia],
                [origen[0]+distancia, origen[1]],
                [origen[0], origen[1]+distancia],
                [origen[0]-distancia, origen[1]]]

        coordenadas=[]

        for i in range(4):

            if i==0:
                x=limites[0][0]
                y=limites[0][1]
                while x < limites[1][0]:
                    x+=1
                    y+=1
                    if(x>0 and x<self.pantalla[0] and y>25 and y<self.pantalla[1]):
                        coordenadas.append([x,y])
                    

            elif i==1:
                x=limites[1][0]
                y=limites[1][1]
                while x > limites[2][0]:
                    x-=1
                    y+=1
                    if(x>0 and x<self.pantalla[0] and y>25 and y<self.pantalla[1]):
                        coordenadas.append([x,y])
                    

            elif i==2:
                x=limites[2][0]
                y=limites[2][1]
                while x > limites[3][0]:
                    x-=1
                    y-=1
                    if(x>0 and x<self.pantalla[0] and y>25 and y<self.pantalla[1]):
                        coordenadas.append([x,y])
                    
            elif i==3:
                x=limites[3][0]
                y=limites[3][1]
                while x < limites[0][0]:
                    x+=1
                    y-=1
                    if(x>0 and x<self.pantalla[0] and y>25 and y<self.pantalla[1]):
                        coordenadas.append([x,y])
                    
            else:
                print('Error, sector del plano no valido')
    
    def ubicarVertice(self, listaCoordenadas, vertice):

        for i in range(len(listaCoordenadas)):
            if listaCoordenadas[i] not in self.coordenadasNoDisponibles:
                vertice.setCoordenadas(listaCoordenadas[i])
            

        
        


def rellenarCoordenadas(inicial, final, listaCoordenadas):
    for i in range((final[1]-inicial[1])+1):
        y=inicial[1]+i

        for k in range((final[0]-inicial[0])+1):
            x=inicial[0]+k

            listaCoordenadas.append([x,y])
    print(len(listaCoordenadas))

rellenarCoordenadas([35,35], [780,580], [])
            





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
        if event.type==pygame.MOUSEBUTTONDOWN:
            #print(event.pos)
            #NO OLVIDAR EL MACHETE
            if (event.pos[0]>=10 and event.pos[0]<=60) and (event.pos[1]>=10 and event.pos[1]<=27) :
                print("está dentro")
                raiz= Tk()
                frame1= Frame(raiz)
                frame1.pack(fill='both', expand="True")
                frame1.config(width='70', height='500')
                frame1.config(bg='limegreen')
                boton=Button(frame1, text='Saludar',font=("Verdana",13), command=saludar).place(x=60,y=100)
                raiz.mainloop()
        if event.type==pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)
    pygame.draw.rect(screen,BLACK,(8,8,54,21))
    pygame.draw.rect(screen,RED,(10,10,50,17))

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
            
            if x2==x1 and y2<y1:
                y-=3
                
            elif x2>x1 and y2<y1:
                x+=3
                y-= y-funcion
                
                if(x>=x2):
                    posPrim+=1
                    ini=True
            elif x2>x1 and y2==y1:
                x+=3
                
            elif x2>x1 and y2>y1:
                x+=3
                y+= funcion-y
                
                if(x>=x2):
                    posPrim+=1
                    ini=True
            elif x2==x1 and y2>y1:
                y+=3
                
            elif x2<x1 and y2>y1:
                x-=3
                y+= funcion-y
                
                if(x<=x2):
                    posPrim+=1
                    ini=True
            elif x2<x1 and y2==y1:
                x-=3
                
            elif x2<x1 and y2<y1:
                x-=3
                y-= y-funcion
                
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