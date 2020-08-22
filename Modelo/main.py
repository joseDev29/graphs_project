from Arista import *; from Grafo import *; from Vertice import *
import json

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
print("g0")
grafos[0].Prim()

print("g1")

g1= Grafo()

g1.IngresarVertice("G")
g1.IngresarVertice("E")
g1.IngresarVertice("B")
g1.IngresarVertice("C")
g1.IngresarVertice("D")
g1.IngresarVertice("A")
g1.IngresarVertice("F")

g1.IngresarAristas("A","B",7)
g1.IngresarAristas("A","D",5)
g1.IngresarAristas("B","D",9)
g1.IngresarAristas("B","C",8)
g1.IngresarAristas("B","E",7)
g1.IngresarAristas("D","E",15)
g1.IngresarAristas("D","F",6)
g1.IngresarAristas("F","E",8)
g1.IngresarAristas("F","G",11)
g1.IngresarAristas("E","G",9)
g1.IngresarAristas("C","E",5)

print(g1.Prim())


print("")
g2= Grafo()

g2.IngresarVertice("C")
g2.IngresarVertice("A")
g2.IngresarVertice("B")
g2.IngresarVertice("F")
g2.IngresarVertice("D")
g2.IngresarVertice("H")
g2.IngresarVertice("E")
g2.IngresarVertice("G")

g2.IngresarAristas("A","B",2)
g2.IngresarAristas("A","E",7)
g2.IngresarAristas("E","B",2)
g2.IngresarAristas("E","F",11)
g2.IngresarAristas("F","B",12)
g2.IngresarAristas("F","G",3)
g2.IngresarAristas("B","G",10)
g2.IngresarAristas("B","C",7)
g2.IngresarAristas("G","C",9)
g2.IngresarAristas("G","H",13)
g2.IngresarAristas("C","H",8)
g2.IngresarAristas("C","D",3)
g2.IngresarAristas("H","D",4)
print(g2.Prim())
print("")
g3=Grafo()
g3.IngresarVertice("B")
g3.IngresarVertice("A")
g3.IngresarVertice("D")
g3.IngresarVertice("C")
g3.IngresarVertice("F")
g3.IngresarVertice("E")
g3.IngresarVertice("H")
g3.IngresarVertice("G")
g3.IngresarVertice("I")
g3.IngresarVertice("J")

g3.IngresarAristas("A","B",3)
g3.IngresarAristas("A","C",9)
g3.IngresarAristas("A","E",6)
g3.IngresarAristas("B","D",2)
g3.IngresarAristas("B","E",4)
g3.IngresarAristas("B","C",9)
g3.IngresarAristas("B","F",9)
g3.IngresarAristas("D","E",2)
g3.IngresarAristas("D","F",8)
g3.IngresarAristas("D","G",9)
g3.IngresarAristas("E","G",9)
g3.IngresarAristas("F","J",10)
g3.IngresarAristas("F","I",9)
g3.IngresarAristas("F","G",7)
g3.IngresarAristas("F","C",8)
g3.IngresarAristas("C","J",18)
g3.IngresarAristas("G","H",4)
g3.IngresarAristas("G","I",5)
g3.IngresarAristas("H","I",1)
g3.IngresarAristas("H","J",4)
g3.IngresarAristas("I","J",3)

print(g3.Prim())

print("Kruskal")
g2.KruskalClass()

print("boruvka")
g1.boruvka()
print("aaa")
g1.BoruvkaClase()
print("2")
g2.boruvka()
print("aaa")
g2.BoruvkaClase()
print("3")
g3.boruvka()
print("aaa")
g3.BoruvkaClase()


print('Helooow')