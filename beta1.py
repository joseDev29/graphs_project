from Modelo.Grafo import *
from random import randint
import json, pygame,sys

with open('Data/grafo1.json') as myJSON:
   myFile = json.load(myJSON)

grafo= Grafo()

for vertice in myFile["vertices"]:
    grafo.IngresarVertice(vertice)

for arista in myFile["aristas"]:
    grafo.IngresarAristas(arista[0],arista[1],arista[2])

#print(grafo)

class Mapeador():

    def __init__(self, unidadEspacio, pantalla, grafo):
        self.unidadEspacio= unidadEspacio
        self.coordenadasVertices=[]
        self.pantalla= pantalla
        self.coordenadasNoDisponibles=[]
        self.grafo= grafo


    def mapearGrafo(self):
        aristas= self.grafo.Prim()[1]
        coordenadas= [40,40]
        inicial= self.grafo.ObtenerVertice(aristas[0].getOrigen())
        print(inicial.getDato())
        inicial.setCoordenadas(coordenadas)
        self.coordenadasVertices.append(coordenadas)
        self.coordenadasNoDisponibles.append(coordenadas)
        verticesMarcados=[]
        verticesMarcados.append(inicial.getDato())

        for arista in aristas:
                    
            if len(verticesMarcados)<=0:
                print('aquiiiiiiiiii')
                distancia=arista.getPeso()*self.unidadEspacio
                verticeCoordenadas= self.mapearVertice(self.grafo.ObtenerVertice(arista.getOrigen()).getCoordenadas(), distancia, self.grafo.ObtenerVertice(arista.getDestino()))
                self.coordenadasVertices.append(verticeCoordenadas)
                self.coordenadasNoDisponibles.append(verticeCoordenadas)
            else:
                if arista.getOrigen() in verticesMarcados:

                    if arista.getDestino() not in verticesMarcados:

                        distancia=arista.getPeso()*self.unidadEspacio
                        verticeCoordenadas= self.mapearVertice(self.grafo.ObtenerVertice(arista.getOrigen()).getCoordenadas(), distancia, self.grafo.ObtenerVertice(arista.getDestino()))
                        self.coordenadasVertices.append(verticeCoordenadas)
                        self.coordenadasNoDisponibles.append(verticeCoordenadas)
                else:

                    for arista2 in aristas:

                        if arista.getOrigen() == arista2.getOrigen() and (arista2.getDestino() in verticesMarcados):
                            print('entre aqui1')
                            distancia=arista2.getPeso()*self.unidadEspacio
                            verticeCoordenadas= self.mapearVertice(self.grafo.ObtenerVertice(arista2.getDestino()).getCoordenadas(), distancia, self.grafo.ObtenerVertice(arista2.getOrigen()))
                            self.coordenadasVertices.append(verticeCoordenadas)
                            self.coordenadasNoDisponibles.append(verticeCoordenadas)

                        elif arista.getOrigen() == arista2.getDestino() and (arista2.getOrigen() in verticesMarcados):
                            print('entre aqui2')
                            distancia= arista2.getPeso()*self.unidadEspacio
                            verticeCoordenadas=self.mapearVertice(self.grafo.ObtenerVertice(arista2.getOrigen()).getCoordenadas(), distancia, self.grafo.ObtenerVertice(arista2.getDestino()))
                            self.coordenadasVertices.append(verticeCoordenadas)
                            self.coordenadasNoDisponibles.append(verticeCoordenadas)
                    

                    if arista.getDestino() not in verticesMarcados:

                        distancia=arista.getPeso()*self.unidadEspacio
                        verticeCoordenadas= self.mapearVertice(self.grafo.ObtenerVertice(arista.getOrigen()).getCoordenadas(), distancia, self.grafo.ObtenerVertice(arista.getDestino()))
                        self.coordenadasVertices.append(verticeCoordenadas)
                        self.coordenadasNoDisponibles.append(verticeCoordenadas)


    def mapearVertice(self, origen, distancia, vertice):
        posiblesPuntos=[]

        inicial=[distancia+20, (distancia+20)]
        final=[(self.pantalla[0]-(distancia+20)), (self.pantalla[1]-(distancia+20))]

        for i in range((final[1]-inicial[1])+1):
            y=inicial[1]+i

            for k in range((final[0]-inicial[0])+1):
                x=inicial[0]+k
                posiblesPuntos.append([x,y])
        
        origen=posiblesPuntos[randint(0,(len(posiblesPuntos)-1))]

        limites=[[origen[0], origen[1]-distancia],
                [origen[0]+distancia, origen[1]],
                [origen[0], origen[1]+distancia],
                [origen[0]-distancia, origen[1]]]
        print(limites)
        coordenadas=[]

        for i in range(4):

            if i==0:
                x=limites[0][0]
                y=limites[0][1]
                while x < limites[1][0]:
                    x+=1
                    y+=1
                    
                    coordenadas.append([x,y])
                    

            elif i==1:
                x=limites[1][0]
                y=limites[1][1]
                while x > limites[2][0]:
                    x-=1
                    y+=1
                    
                    coordenadas.append([x,y])
                    

            elif i==2:
                x=limites[2][0]
                y=limites[2][1]
                while x > limites[3][0]:
                    x-=1
                    y-=1
                    
                    coordenadas.append([x,y])
                    
            elif i==3:
                x=limites[3][0]
                y=limites[3][1]
                while x < limites[0][0]:
                    x+=1
                    y-=1
                    
                    coordenadas.append([x,y])
                    
            else:
                print('Error, sector del plano no valido')
        
        return self.ubicarVertice(coordenadas, vertice)
    

    def ubicarVertice(self, listaCoordenadas, vertice):
        coordenadas=[]
        for i in range(len(listaCoordenadas)):
            if listaCoordenadas[i] not in self.coordenadasNoDisponibles:
                vertice.setCoordenadas(listaCoordenadas[i])
                print(vertice.getDato())
                coordenadas=listaCoordenadas[i]
                self.coordenadasNoDisponibles.append(listaCoordenadas[i])
                self.rellenarCoordenadas(listaCoordenadas[i] )
                break
        return coordenadas
            

    def getDatosVertices(self):
        datosVertices=[]
        for vertice in self.grafo:
            datosVertices.append(vertice.getDato())

    
    def rellenarCoordenadas(self, punto):
        radio=5
        espacioMinimo=10
        inicial=[((punto[0]-radio)-espacioMinimo), ((punto[1]-radio)-espacioMinimo)]
        final=[((punto[0]+radio)+espacioMinimo), ((punto[1]+radio)+espacioMinimo)]
        for i in range((final[1]-inicial[1])+1):
            y=inicial[1]+i

            for k in range((final[0]-inicial[0])+1):
                x=inicial[0]+k
                if(x>0 and x<self.pantalla[0] and y>25 and y<self.pantalla[1]):
                   self.coordenadasNoDisponibles.append([x,y])
        #print(listaCoordenadas)

import math
pantalla=[1000, 600]
unidadEspacio= 50#unidad=int(math.sqrt((pantalla[0]**2 + pantalla[1]**2)) / grafo.pesoTotal())
print(unidadEspacio)
graficador= Mapeador(unidadEspacio, pantalla, grafo)

graficador.mapearGrafo()
#print(graficador.pantalla)
print(graficador.coordenadasVertices)


pygame.init()

#Definir colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)

size=(graficador.pantalla[0],graficador.pantalla[1])

fuente=pygame.font.Font(None,30)

#Crear ventana
screen=pygame.display.set_mode(size)
#Controlar los FPS
clock=pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            #print(event.pos)
            #NO OLVIDAR EL MACHETE
            """if (event.pos[0]>=10 and event.pos[0]<=60) and (event.pos[1]>=10 and event.pos[1]<=27) :
                print("está dentro")
                raiz= Tk()
                frame1= Frame(raiz)
                frame1.pack(fill='both', expand="True")
                frame1.config(width='70', height='500')
                frame1.config(bg='limegreen')
                boton=Button(frame1, text='Saludar',font=("Verdana",13), command=saludar).place(x=60,y=100)
                raiz.mainloop()"""
        if event.type==pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)
    pygame.draw.rect(screen,BLACK,(8,8,54,21))
    pygame.draw.rect(screen,RED,(10,10,50,17))

    for vertice in grafo.getVertices():
        
        for adyacente in vertice.getListaAdyacentes():
            pygame.draw.line(screen, BLACK, (vertice.getCoordenadas()[0],vertice.getCoordenadas()[1]),(adyacente.getCoordenadas()[0],adyacente.getCoordenadas()[1]), 2)

        texto=fuente.render(vertice.getDato(),0,BLUE)
        pygame.draw.circle(screen,BLACK,vertice.getCoordenadas(),24)
        pygame.draw.circle(screen,RED,vertice.getCoordenadas(),22)
        screen.blit(texto,[vertice.getCoordenadas()[0]-11, vertice.getCoordenadas()[1]-7])


    pygame.display.flip()
    clock.tick(30)