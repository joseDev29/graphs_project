from typing import List
from collections import deque
from Modelo.Vertice import *
from Modelo.Arista import *
import copy #para realizar copias de objetos

class Grafo():

    def __init__(self):
        self.ListaVertices=[]
        self.ListaAristas=[]
        self.ListaVisitados=[]

    def IngresarVertice(self,dato):
        if not self.Verificarvertice(dato):
            self.ListaVertices.append(Vertice(dato))

    def Verificarvertice(self,dato):
        for vertice in self.ListaVertices:
            if vertice.getDato()==dato:
                return True
        return False

    def ImprimirVertice(self):
        for vertice in self.ListaVertices:
            print("dato:{0} ".format(vertice.getDato()))
            print("Adyacencias {0}".format(vertice.getListaAdyacentes()))
    
    def ImprimirAristas(self):
        for Arista in self.ListaAristas:
            print("dato: {0}-{1}-{2}".format(Arista.getOrigen(),Arista.getDestino(),Arista.getPeso()))

    def IngresarAristas(self,Origen,Destino,Peso):
        if not self.VerificarArista(Origen,Destino):
            if self.ObtenerVertice(Origen)!=None and self.ObtenerVertice(Destino)!=None:
                self.ListaAristas.append(Arista(Origen,Destino,Peso))
                #actualizar las adyacencias
                self.ObtenerVertice(Origen).getListaAdyacentes().append(self.ObtenerVertice(Destino))
    

    def ObtenerVertice(self,nombre):
        for vertice in self.ListaVertices:
            if nombre==vertice.getDato():
                return vertice
        return None

    def VerificarArista(self,Origen,Destino):
        for i in range(len(self.ListaAristas)):
            if self.ListaAristas[i].getOrigen()==Origen and self.ListaAristas[i].getDestino()==Destino:
                return True
        return False
    
    def Profundidad(self,dato):
        if dato in self.ListaVisitados:
            return
        else:
            Vertice=self.ObtenerVertice(dato)
            if Vertice!=None:
                self.ListaVisitados.append(Vertice.getDato())
                for dato in Vertice.getListaAdyacentes():
                    self.Profundidad(dato)

    def getListaVisitados(self):
        return self.ListaVisitados
    
    def getVertices(self):
        return self.ListaVertices
    
    def getAristas(self):
        return self.ListaAristas
    def Amplitud(self,origen):
        VisitadosA=[]
        Cola=deque()
        Vertice=self.ObtenerVertice(origen)
        if Vertice!=None:
            VisitadosA.append(origen)
            Cola.append(Vertice)
        while Cola:
            elemento=Cola.popleft()
            for Adyacencia in elemento.getListaAdyacentes:
                if Adyacencia not in VisitadosA:
                    Vertice=self.ObtenerVertice(Adyacencia)
                    VisitadosA.append(Adyacencia)
                    Cola.append(Vertice)
        return VisitadosA

    def Prim(self):
        Vertice=self.ListaVertices[0]
        VerticesMarcados=[]
        aristasDisponibles=[]
        AristasMarcadas=[]
        VerticesMarcados.append(Vertice.getDato())
        while len(VerticesMarcados)!=len(self.ListaVertices):
            aristasDisponibles=self.aristasDisponibles(VerticesMarcados,AristasMarcadas)
            myBool=True
            while aristasDisponibles and myBool==True:
                if (aristasDisponibles[0].getOrigen() not in VerticesMarcados) or (aristasDisponibles[0].getDestino() not in VerticesMarcados):
                    AristasMarcadas.append(aristasDisponibles[0])
                    if aristasDisponibles[0].getOrigen() not in VerticesMarcados:
                        VerticesMarcados.append(aristasDisponibles[0].getOrigen())
                    if aristasDisponibles[0].getDestino() not in VerticesMarcados:
                        VerticesMarcados.append(aristasDisponibles[0].getDestino())
                    aristasDisponibles.pop(0)
                    myBool=False
                else:
                    aristasDisponibles.pop(0)
        for aris in AristasMarcadas:
            print("Vertice 1: {0}, Peso: {1}, Vertice 2: {2}".format(aris.getOrigen(),+aris.getPeso(),aris.getDestino()))   
        return VerticesMarcados, AristasMarcadas

    def aristasDisponibles(self,verticesMarcados,aristasMarcadas):
        listaDisponibles=[]
        for vertice in verticesMarcados:
            for arista in self.ListaAristas:
                if arista.getOrigen()==vertice or arista.getDestino()==vertice:
                    if (arista not in listaDisponibles) and (arista not in aristasMarcadas):
                        listaDisponibles.append(arista)
        temp=None
        for i in range (len(listaDisponibles)):
            for k in range (i+1, len(listaDisponibles)):
                if listaDisponibles[i].getPeso()>=listaDisponibles[k].getPeso():
                    temp=listaDisponibles[i]
                    listaDisponibles[i]=listaDisponibles[k]
                    listaDisponibles[k]=temp 
        return listaDisponibles

    def ordenarAristas(self,aristasentran):
        
        for i in range (len(aristasentran)):
            for k in range(i+1, len(aristasentran)):
                if aristasentran[i].getPeso()>=aristasentran[k].getPeso():
                    temp=aristasentran[i]
                    aristasentran[i]=aristasentran[k]
                    aristasentran[k]=temp
        return aristasentran

    def kruskal(self):
        aristasOrdenadas=self.ordenarAristas(self.ListaAristas)
        conjuntoVertices=set()
        conjuntoKruskal=[]
        ListaVerticesMarcados=[]
        while len(conjuntoVertices)!=len(self.ListaVertices):

            aristaMin=aristasOrdenadas[0]
            temporal={aristaMin.getOrigen(),aristaMin.getDestino()}

            for i in ListaVerticesMarcados:
                if len(temporal.intersection(ListaVerticesMarcados[i]))==0:
                    ListaVerticesMarcados.append(temporal)
                    
                elif len(temporal.intersection(ListaVerticesMarcados[i]))==1:
                    ListaVerticesMarcados[i]=ListaVerticesMarcados[i].union(temporal)       
            

            aristasOrdenadas.pop(0)

        for arista in conjuntoKruskal:
            print("{0}---{1}---{2}".format(arista.getOrigen(),arista.getPeso(),arista.getDestino()))


    def KruskalClass(self):
        copiaAristas=copy.copy(self.ListaAristas)
        aristasKruskal=[]
        ListaConjuntos=[]
        copiaAristas=self.ordenarAristas(copiaAristas)
        for Conjuntotemp in copiaAristas:
            self.OperacionConjuntos(ListaConjuntos,aristasKruskal,Conjuntotemp)

        for dato in aristasKruskal:
            print("Origen:{0} Destino: {1} Peso {2}".format(dato.getOrigen(),dato.getDestino(),dato.getPeso()))

    
    def OperacionConjuntos(self,ListaConjuntos,AristasKruskal,Conjuntotemp):
        encontrado1=-1
        encontrado2=-1
        if not ListaConjuntos:
            ListaConjuntos.append({Conjuntotemp.getOrigen(),Conjuntotemp.getDestino()})
            AristasKruskal.append(Conjuntotemp)
        else:
            for i in range (len(ListaConjuntos)):
                if Conjuntotemp.getOrigen() in ListaConjuntos[i] and Conjuntotemp.getDestino() in ListaConjuntos[i]:
                    return 
            
            for i in range(len(ListaConjuntos)):
                if Conjuntotemp.getOrigen() in ListaConjuntos[i]:
                    encontrado1=i
                if Conjuntotemp.getDestino() in ListaConjuntos[i]:
                    encontrado2=i
            
            if encontrado1!=-1 and encontrado2!=-1:
                if encontrado1!=-1!=encontrado2:
                    ListaConjuntos[encontrado1].update(ListaConjuntos[encontrado2])
                    ListaConjuntos[encontrado2].clear()

            if encontrado1!=-1 and encontrado2==-1:
                ListaConjuntos[encontrado1].update(Conjuntotemp.getOrigen())
                ListaConjuntos[encontrado1].update(Conjuntotemp.getDestino())
                
            
            if encontrado1==-1 and encontrado2!=-1:
                ListaConjuntos[encontrado2].update(Conjuntotemp.getOrigen())
                ListaConjuntos[encontrado2].update(Conjuntotemp.getDestino())

            if encontrado1==-1 and encontrado2==-1:
                ListaConjuntos.append({Conjuntotemp.getOrigen(),Conjuntotemp.getDestino()})

            AristasKruskal.append(Conjuntotemp)

    def boruvka(self):
        aristasBoruvka=[]
        for vertice in self.ListaVertices:
            aristastemp=[]
            for arista in self.ListaAristas:
                if vertice.getDato()==arista.getOrigen():
                    aristastemp.append(arista)
            if len(aristastemp)!=0:
                aristastemp=self.ordenarAristas(aristastemp)
                if (aristastemp[0] not in aristasBoruvka):
                    aristasBoruvka.append(aristastemp[0])
        
        for arista in aristasBoruvka:
            print("aristas:{0}---{1}---{2}".format(arista.getPeso(),arista.getOrigen(),arista.getDestino()))

    def Buscarmenor(self,Nodo,copiaAristas):
        temp=[]
        for adyacencia in Nodo.getListaAdyacentes():
            for Arista in copiaAristas:
                #busco las aristas de esa lista de adyacencia
               if Arista.getOrigen()==Nodo.getDato() and Arista.getDestino()==adyacencia:
                    temp.append(Arista)
        if temp:#si no esta vacia
            #una vez obtenga todas las aristas, saco la menor
            self.ordenarAristas(temp)  # ordeno las aristas
            #elimin ese destino porque ya lo voy a visitar
            #print("{0}-{1}:{2}".format(temp[0].getOrigen(), temp[0].getDestino(), temp[0].getPeso()))

            Nodo.getListaAdyacentes().remove(temp[0].getDestino())
            return temp[0]  # es la menor

        return None#es la menor

    def BoruvkaClase(self):
        copiaNodos = copy.copy(self.ListaVertices)  # copia de los nodos
        copiaAristas = copy.copy(self.ListaAristas)  # copia de las aristas
        AristasBorukvka = []
        ListaConjuntos = []
        bandera=True
        cantidad=0
        while(cantidad>1 or bandera):
            for Nodo in copiaNodos:
                self.OperacionesconjuntosB(Nodo, ListaConjuntos, AristasBorukvka,copiaAristas)
            bandera=False
            cantidad=self.Cantidadconjuntos(ListaConjuntos)
        for dato in AristasBorukvka:
            print("Origen: {0} destino: {1} peso: {2}".format(dato.getOrigen(), dato.getDestino(), dato.getPeso()))


    def Cantidadconjuntos(self,ListaConjuntos):
        cantidad=0
        for conjunto in ListaConjuntos:
            if len(conjunto)>0:
                cantidad=cantidad+1
        return cantidad

    def OperacionesconjuntosB(self,Nodo, ListaConjuntos, AristasBorukvka,copiaAristas):
        encontrado1=-1
        encontrado2=-1
        menor = self.Buscarmenor(Nodo, copiaAristas)
        if not menor==None:#si no esta vacio
            if not ListaConjuntos:#si esta vacia
                ListaConjuntos.append({menor.getOrigen(),menor.getDestino()})
                AristasBorukvka.append(menor)
            else:
                for i in range(len(ListaConjuntos)):
                    if  (menor.getOrigen()  in ListaConjuntos[i]) and (menor.getDestino() in ListaConjuntos[i]):
                        return False##Camino cicliclo

                for i in range(len(ListaConjuntos)):
                    if menor.getOrigen() in ListaConjuntos[i]:
                       encontrado1=i
                    if menor.getDestino() in ListaConjuntos[i]:
                       encontrado2=i

                if encontrado1!=-1 and encontrado2!=-1:
                    if encontrado1!=encontrado2:#si pertenecen a dos conjuntos diferentes
                        #debo unir los dos conjuntos
                        ListaConjuntos[encontrado1].update(ListaConjuntos[encontrado2])
                        ListaConjuntos[encontrado2].clear();#elimino el conjunto
                        AristasBorukvka.append(menor)

                if encontrado1!=-1 and encontrado2==-1:# si va unido por un conjunto
                    ListaConjuntos[encontrado1].update(menor.getOrigen())
                    ListaConjuntos[encontrado1].update(menor.getDestino())
                    AristasBorukvka.append(menor)

                if encontrado1 == -1 and encontrado2 != -1:# si va unido por un conjunto
                    ListaConjuntos[encontrado2].update(menor.getOrigen())
                    ListaConjuntos[encontrado2].update(menor.getDestino())
                    AristasBorukvka.append(menor)

                if encontrado1 == -1 and encontrado2 == -1:# si no existe en los conjuntos
                    ListaConjuntos.append({menor.getOrigen(), menor.getDestino()})
                    AristasBorukvka.append(menor)