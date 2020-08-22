class Arista:
    
    def __init__(self,Origen,Destino,Peso):
        self.Origen=Origen
        self.Destino=Destino
        self.Peso=Peso
    
    def getOrigen(self):
        return self.Origen
    
    def getDestino(self):
        return self.Destino
    
    def getPeso(self):
        return self.Peso
    
    def setOrigen(self,Origen):
        self.Origen=Origen
    
    def setDestino(self,Destino):
        self.Destino=Destino
    
    def setPeso(self,Peso):
        self.Peso=Peso