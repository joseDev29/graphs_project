class Vertice:
    def __init__(self,dato):
        self.dato=dato
        self.ListaAdyacentes=[]
        self.coordenadas=[0,0]
        self.ListaIncidentes=[]

    def getDato(self):
        return self.dato
    
    def setDato(self,dato):
        self.dato=dato
    
    def getListaAdyacentes(self):
        return self.ListaAdyacentes

    def setListaAdyacentes(self,ListaAdyacentes):
        self.ListaAdyacentes=ListaAdyacentes
    
    def getCoordenadas(self):
        return self.coordenadas

    def setCoordenadas(self, valores):
        self.coordenadas= valores

    def setListaIncidentes(self, lista):
        self.ListaIncidentes = lista

    def getListaIncidentes(self):
        return self.ListaIncidentes