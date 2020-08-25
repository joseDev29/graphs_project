from Modelo.Grafo import *
from tkinter import *
from tkinter import ttk
import pygame, sys, random, json

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
    listaPrim.append(temp)


x1=listaPrim[0][0][0]
y1=listaPrim[0][0][1]
x2=listaPrim[0][1][0]
y2=listaPrim[0][1][1]
print(listaPrim[0])
print(x1)
print(y1)
print(x2)
print(y2)


funcion= (((y2-y1)//(x2-x1))*((x1)-x1))+y1
print("-------------")
print(funcion)