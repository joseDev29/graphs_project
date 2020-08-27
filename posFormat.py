from Modelo.Grafo import *
from random import randint
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import json, pygame, sys
from copy import copy

abrir=0


class Mapeador():

    def __init__(self, pantalla, grafo):
        self.coordenadasVertices=[]
        self.pantalla= pantalla
        self.coordenadasNoDisponibles=[]
        self.grafo= grafo
        self.mapaPantalla=[]

    def getGrafo(self):
        return self.grafo

    def mapearGrafo(self):
        
        self.algo()
        for vertice in self.grafo.getVertices():

            myBool=True

            while myBool:

                posMap= randint(0,len(self.mapaPantalla)-1)
                coordenada= self.mapaPantalla[posMap][randint(0,len(self.mapaPantalla[posMap])-1)]
                
                if coordenada not in self.coordenadasNoDisponibles:
                    vertice.setCoordenadas(coordenada)
                    self.rellenarCoordenadas(coordenada)
                    self.coordenadasNoDisponibles.append(coordenada)
                    myBool=False
                    
    def generarCoordenadas(self, vertice):
        encontrado=True
        while encontrado:
            posMap= randint(0,len(self.mapaPantalla)-1)
            coordenada= self.mapaPantalla[posMap][randint(0,len(self.mapaPantalla[posMap])-1)]
                
            if coordenada not in self.coordenadasNoDisponibles:
                vertice.setCoordenadas(coordenada)
                self.rellenarCoordenadas(coordenada)
                self.coordenadasNoDisponibles.append(coordenada)
                encontrado=False
                       
    def getDatosVertices(self):
        datosVertices=[]
        for vertice in self.grafo:
            datosVertices.append(vertice.getDato())

    def rellenarCoordenadas(self, punto):
        espacio=80
        inicial=[(punto[0]-espacio), (punto[1]-espacio)]
        final=[(punto[0]+espacio), (punto[1]+espacio)]

        for i in range((final[1]-inicial[1])+1):
            y=inicial[1]+i
            for k in range((final[0]-inicial[0])+1):
                x=inicial[0]+k
                self.coordenadasNoDisponibles.append([x,y])
        
    def algo(self):
        
        inicial=[50,50]
        final=[150,150]
        while final[1] <= (self.pantalla[1]-50):
            
            while final[0] <= (self.pantalla[0]-50):

                self.rellenar(inicial, final)
                inicial[0]+=100
                final[0]+=100
            
            inicial[0]=50
            final[0]=150
            inicial[1]+=100
            final[1]+=100
        
    def rellenar(self, inicial, final):
        tmp=[]
        for i in range((final[1]-inicial[1])):
            y=inicial[1]+i

            for k in range((final[0]-inicial[0])):
                x=inicial[0]+k

                tmp.append([x,y])

        self.mapaPantalla.append(tmp)
        
    
    def verificarCoordenada(self, coordenada):
        boolean= False
        for cord in self.coordenadasNoDisponibles:
            if cord[0]==coordenada[0] and cord[1]==coordenada[1]:
                boolean= True
        return boolean

grafo= Grafo(); pantalla=[1000,600]; mapeador= Mapeador(pantalla, grafo)

class Menu(Frame):
    def __init__(self,master=None):
        super().__init__(master,width=200,height=400)
        self.master=master
        self.pack()
        self.crear_botones()
        self.verticeDato = StringVar()
        self.verticeDato.set("")
        self.aristaOrigen = StringVar()
        self.aristaOrigen.set("")
        self.aristaPeso = StringVar()
        self.aristaPeso.set("")
        self.aristaDestino = StringVar()
        self.aristaDestino.set("")
        self.dirigido = StringVar()
        self.dirigido.set("")
        #self.transient(master)
    def crear_botones(self):
        #Se instancian los botones
        self.btnCargarGrafo=Button(self,text="Cargar Grafo",command=self.ventanaArchivo)
        self.btnObstruirCamino=Button(self,text='Obstruir camino',command=self.prueba)
        self.btnPrueba=Button(self,text="Agregar Vertice",command=self.dialogo)
        self.btnAgregarArista=Button(self, text='Agregar Arista',command=self.dialogo2)
        self.btnDijkstra=Button(self, text='Dijkstra',command=self.prueba)
        self.btnPrim=Button(self, text='Prim',command=self.recorridoPrim)
        self.btnBoruvka=Button(self, text='Boruvka',command=self.recorridoBoruvka)
        self.btnKruskal=Button(self, text='Kruskal',command=self.recorridoKruskal)
        #Se les da posición a los botones
        self.btnCargarGrafo.place(x=10,y=10,width=100,height=30)
        self.btnPrueba.place(x=10,y=50,width=100,height=30)
        self.btnObstruirCamino.place(x=10,y=100,width=100,height=30)
        self.btnAgregarArista.place(x=10,y=150,width=100,height=30)
        self.btnDijkstra.place(x=10,y=200,width=100,height=30)
        self.btnPrim.place(x=10,y=250,width=100,height=30)
        self.btnBoruvka.place(x=10,y=300,width=100,height=30)
        self.btnKruskal.place(x=10,y=350,width=100,height=30)
        
    
    def prueba(self):
        pass
    
    def recorridoPrim(self):
        coordenadasRecorrido('prim')
        
    def recorridoBoruvka(self):
        coordenadasRecorrido('boruvka')
    
    def recorridoKruskal(self):
        coordenadasRecorrido('kruskal')
        
    def ventanaArchivo(self):
        archivo = filedialog.askopenfilename(initialdir="/",title="Cargar Grafo", filetypes=(("json files","*.json"),("all files",".")))
        d=Dirigido(self,self.dirigido)
        self.wait_window(d.top)

        self.generarGrafo(archivo,self.dirigido)
        print(archivo)

    def dialogo(self):
        d = AgregarVertice(self, self.verticeDato, "Agregue el valor de su vertice", "Dame valor")
        self.wait_window(d.top)
        #self.valor.set(d.ejemplo)
    def dialogo2(self):
        d = AgregarArista(self, self.aristaOrigen,self.aristaDestino,self.aristaPeso,self.dirigido)
        self.wait_window(d.top)
        #self.valor.set(d.ejemplo)
    
    def generarGrafo(self,ruta,direccion):
        print('entre')
        print(grafo.getVertices())
        print(grafo.getAristas())
        grafo.setVertices([])
        grafo.setAristas([])
        grafo.setVisitados([])
        print("depués de")
        print(grafo.getVertices())
        print(grafo.getAristas())
        with open(ruta) as myJSON:
            myFile = json.load(myJSON)

        for vertice in myFile["vertices"]:
            grafo.IngresarVertice(vertice)

        for arista in myFile["aristas"]:
            if direccion.get()=="Dirigido":
                grafo.IngresarAristas(arista[0],arista[1],arista[2],True)
            else:
                grafo.IngresarAristas(arista[0],arista[1],arista[2],False)
        
        mapeador.mapearGrafo()
        print(grafo.getVertices())
        print(grafo.getAristas())
        
        
class Dirigido:
    def __init__(self,parent,dirigido):
        self.dirigido=dirigido
        
        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        
        self.top.geometry('300x300')
        self.top.title("Seleccione su tipo de grafo")
        
        labeltext1 = 'Dirigido/No Dirigido'
        label1=Label(self.top, text=labeltext1,width=20)
        label1.place(x=10,y=100)
        
        self.top.bind("<Return>", self.ok)
        
        self.dirigidoEntry = Entry(self.top, text=dirigido.get())

        self.dirigidoEntry.bind("<Return>", self.ok)
        self.dirigidoEntry.bind("<Escape>", self.cancel)
        
        self.dirigidoEntry.pack(padx=15)
        self.dirigidoEntry.place(x=20,y=120)
        self.dirigidoEntry.focus_set()
        
        b = Button(self.top, text="Seleccionar", command=self.ok)
        b.pack(pady=5)
        b.place(x=50,y=150)

    def ok(self, event=None):
        self.dirigido.set(self.dirigidoEntry.get())
        self.top.destroy()
 
    def cancel(self, event=None):
        self.top.destroy()
        

class AgregarVertice:
    def __init__(self, parent, valor, title, labeltext):
        self.valor = valor
        self.labeltext=''
        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        if len(title) > 0: self.top.title(title)
        if len(self.labeltext) == 0: self.labeltext = 'Valor'
        Label(self.top, text=self.labeltext).pack()
        self.top.bind("<Return>", self.verticeAgregado)
        self.e = Entry(self.top, text=valor.get())
        self.e.bind("<Return>", self.verticeAgregado)
        self.e.bind("<Escape>", self.cancel)
        self.e.pack(padx=15)
        self.e.focus_set()
        b = Button(self.top, text="AGREGAR", command=self.verticeAgregado)
        b.pack(pady=5)
 
    def verticeAgregado(self, event=None):
        self.valor.set(self.e.get())
        mapeador.getGrafo().IngresarVertice(self.valor.get())
        mapeador.generarCoordenadas(grafo.ObtenerVertice(self.valor.get()))
        self.top.destroy()
 
    def cancel(self, event=None):
        self.top.destroy()


class AgregarArista:
    def __init__(self, parent, origen,destino,peso,direccion):

        self.origen = origen
        self.destino=destino
        self.peso=peso
        self.direccion=direccion

        self.top = Toplevel(parent)
        self.top.transient(parent)
        self.top.grab_set()
        self.top.geometry('400x400')
        self.top.title("Agregue la Arista")

        labeltext1 = 'Origen'
        labeltext2 = 'Peso'
        labeltext3 = 'Destino'

        label1=Label(self.top, text=labeltext1,width=10)
        label2=Label(self.top, text=labeltext2,width=10)
        label3=Label(self.top, text=labeltext3,width=10) 

        label1.place(x=10,y=100)
        label2.place(x=10,y=120)
        label3.place(x=10,y=140)

        self.top.bind("<Return>", self.ok)

        self.origenEntry = Entry(self.top, text=origen.get())
        self.pesoEntry = Entry(self.top, text=peso.get())
        self.destinoEntry = Entry(self.top, text=destino.get())

        self.origenEntry.bind("<Return>", self.ok)
        self.pesoEntry.bind("<Return>", self.ok)
        self.destinoEntry.bind("<Return>", self.ok)

        self.origenEntry.bind("<Escape>", self.cancel)
        self.pesoEntry.bind("<Escape>", self.cancel)
        self.destinoEntry.bind("<Escape>", self.cancel)

        self.origenEntry.pack(padx=15)
        self.origenEntry.place(x=100,y=100)
        self.pesoEntry.pack(padx=15)
        self.pesoEntry.place(x=100,y=120)
        self.destinoEntry.pack(padx=15)
        self.destinoEntry.place(x=100,y=140)

        self.origenEntry.focus_set()
        self.destinoEntry.focus_set()
        self.pesoEntry.focus_set()

        b = Button(self.top, text="AGREGAR", command=self.ok)
        b.pack(pady=5)
        b.place(x=100,y=180)
 
    def ok(self, event=None):
        self.origen.set(self.origenEntry.get())
        self.peso.set(self.pesoEntry.get())
        self.destino.set(self.destinoEntry.get())
        grafo.IngresarAristas(self.origen.get(),self.destino.get(),int(self.peso.get()),grafo.getGrafoDirigido())
        self.top.destroy()
 
    def cancel(self, event=None):
        self.top.destroy()
   

pygame.init()

#Definir colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
SUPERBLUE= (40, 210, 250)
size=(pantalla[0],pantalla[1])
randomColor=[(64, 242, 29), (193, 255, 181), (181, 255, 241), (216, 111, 237), (237, 17, 42) ]
fuente=pygame.font.Font(None,30)



#Crear ventana
screen=pygame.display.set_mode(size)
fondo= pygame.image.load("Images/fondo.png")
nave= pygame.image.load("Images/navecita.png")
planet= pygame.image.load("Images/planet.png")
iconRow1= pygame.image.load("Images/row1.png").convert()
iconRow2= pygame.image.load("Images/row2.png").convert()
iconRow3= pygame.image.load("Images/row3.png").convert()
iconRow4= pygame.image.load("Images/row4.png").convert()
iconRow1.set_colorkey(WHITE)
iconRow2.set_colorkey(WHITE)
iconRow3.set_colorkey(WHITE)
iconRow4.set_colorkey(WHITE)
#Controlar los FPS
clock=pygame.time.Clock()

ini=True; cont=1; posPrim=0; animar=True

def coordenadasRecorrido(tipo):
    lista=[]
    if tipo == 'prim':
        for arista in grafo.Prim()[1]:
            temp=[]
            temp.append(grafo.ObtenerVertice(arista.getOrigen()).getCoordenadas())
            temp.append(grafo.ObtenerVertice(arista.getDestino()).getCoordenadas())
            print(temp)
            lista.append(temp)
        raiz.destroy()
        dibujarRecorrido(lista, True)
    elif tipo == 'kruskal':
        print(grafo.KruskalClass())
        for arista in grafo.KruskalClass():
            temp=[]
            temp.append(grafo.ObtenerVertice(arista.getOrigen()).getCoordenadas())
            temp.append(grafo.ObtenerVertice(arista.getDestino()).getCoordenadas())
            print(temp)
            lista.append(temp)
        raiz.destroy()
        dibujarRecorrido(lista, True)
    elif tipo == 'boruvka':
        print(grafo.boruvka())
        for arista in grafo.boruvka():
            temp=[]
            temp.append(grafo.ObtenerVertice(arista.getOrigen()).getCoordenadas())
            temp.append(grafo.ObtenerVertice(arista.getDestino()).getCoordenadas())
            print(temp)
            lista.append(temp)
        raiz.destroy()
        dibujarRecorrido(lista, True)

def dibujarVertices(grafo):
    for vertice in grafo.getVertices():
        texto=fuente.render(vertice.getDato(),0,WHITE)
        cordtmp= (vertice.getCoordenadas()[0]-22, vertice.getCoordenadas()[1]-22)
        screen.blit(planet, cordtmp)
        screen.blit(texto,[vertice.getCoordenadas()[0]-10, vertice.getCoordenadas()[1]-10])
        if len(vertice.getListaAdyacentes()) <= 0:
            screen.blit(fuente.render('Pozo',0,WHITE),[vertice.getCoordenadas()[0]-10, vertice.getCoordenadas()[1]])

def dibujarAristas(grafo):
    for vertice in grafo.getVertices():
        for adyacente in vertice.getListaAdyacentes():
            pygame.draw.line(screen, (230, 181, 255), (vertice.getCoordenadas()[0],vertice.getCoordenadas()[1]),(adyacente.getCoordenadas()[0],adyacente.getCoordenadas()[1]), 1)
    
    if grafo.grafodirigido:
        
        for arista in grafo.getAristas():
            x1=grafo.ObtenerVertice(arista.getOrigen()).getCoordenadas()[0]
            y1=grafo.ObtenerVertice(arista.getOrigen()).getCoordenadas()[1]
            x2=grafo.ObtenerVertice(arista.getDestino()).getCoordenadas()[0]
            y2=grafo.ObtenerVertice(arista.getDestino()).getCoordenadas()[1]
            if grafo.grafodirigido:
                if x2==x1 and y2<y1:
                    pygame.draw.circle(screen,RED,(x2, y2+12),10)
                elif x2>x1 and y2<y1:
                    pygame.draw.circle(screen,RED,(x2-12, y2+11),10)
                elif x2>x1 and y2==y1:
                    
                    pygame.draw.circle(screen,RED,(x2+12, y2),10)
                elif x2>x1 and y2>y1:
                    
                    pygame.draw.circle(screen,RED,(x2-12, y2-12),10)
                elif x2==x1 and y2>y1:
                    pygame.draw.circle(screen,RED,(x2, y2-12),10)
                elif x2<x1 and y2>y1:
                    
                    pygame.draw.circle(screen,RED,(x2+12, y2-12),10)
                elif x2<x1 and y2==y1:
                    
                    pygame.draw.circle(screen,RED,(x2+12, y2),10)
                elif x2<x1 and y2<y1:
                    pygame.draw.circle(screen,RED,(x2+12, y2-12),10)
                else:
                    print('nada')
                        
def dibujarRecorrido(aristas, animacion):
    #raiz.destroy()
    dibujarAristas(grafo)
    dibujarVertices(grafo)
    if animacion:
        for arista in aristas:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
            pygame.draw.line(screen,(95, 34, 227),(arista[0][0],arista[0][1]),(arista[1][0],arista[1][1]),2)
            pygame.display.flip()
            clock.tick(1)
        dibujarVertices(grafo)
        animarRecorrido(grafo, aristas, nave, fondo)
    elif not animacion:
        for arista in aristas:
            pygame.draw.line(screen,(95, 34, 227),(arista[0][0],arista[0][1]),(arista[1][0],arista[1][1]),2)
        dibujarVertices(grafo)
    
def animarRecorrido(grafo, aristas, elementoAnimado, fondo):
    animacion=True; posicionador=0; inicioArista=True
    
    while animacion:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        x1=copy(aristas[posicionador][0][0])
        y1=copy(aristas[posicionador][0][1])
        x2=copy(aristas[posicionador][1][0])
        y2=copy(aristas[posicionador][1][1])

        arista= aristas[posicionador]

        if inicioArista:
            x=arista[0][0]
            y=arista[0][1]

        funcion= int((((y2-y1)/(x2-x1))*((x)-x1))+y1)

        inicioArista=False
        if posicionador < len(aristas):

            if x2==x1 and y2<y1:
                y-=3
                
            elif x2>x1 and y2<y1:
                x+=3
                y-= y-funcion
                
                if(x>=x2):
                    posicionador+=1
                    inicioArista=True
            elif x2>x1 and y2==y1:
                x+=3
                
            elif x2>x1 and y2>y1:
                x+=3
                y+= funcion-y
                
                if(x>=x2):
                    posicionador+=1
                    inicioArista=True
            elif x2==x1 and y2>y1:
                y+=3
                
            elif x2<x1 and y2>y1:
                x-=3
                y+= funcion-y
                
                if(x<=x2):
                    posicionador+=1
                    inicioArista=True
            elif x2<x1 and y2==y1:
                x-=3
                
            elif x2<x1 and y2<y1:
                x-=3
                y-= y-funcion
                
                if(x<=x2):
                    posicionador+=1
                    inicioArista=True
            else:
                print('nada')

            elementoCoordenadas=((x-30, y-30))
            screen.blit(fondo, (0,0))
            dibujarAristas(grafo)
            dibujarRecorrido(aristas, False)
            dibujarVertices(grafo)
            screen.blit(elementoAnimado, elementoCoordenadas)

        if(posicionador>=len(aristas)):
                animacion=False

        pygame.display.update()
        pygame.time.Clock().tick(60)

def dibujarBoton():
    menuIcon= pygame.image.load("Images/menuicon.png")
    pygame.draw.rect(screen,(109, 43, 255),(8,8,54,21))
    pygame.draw.rect(screen,(203, 183, 247),(10,10,50,17))
    screen.blit(menuIcon, (18,4))


conexo="yo"
while True:
    abrir=0 
    grafo.setPozos(0) 
    grafo.setFuentes(0)

    screen.blit(fondo, (0,0))
    dibujarBoton()
    screen.blit(fuente.render(conexo,0,WHITE),[450, 10])
    for event in pygame.event.get():
        if event.type==pygame.MOUSEBUTTONDOWN:
            #print(event.pos)
            #NO OLVIDAR EL MACHETE
            if (event.pos[0]>=10 and event.pos[0]<=60) and (event.pos[1]>=10 and event.pos[1]<=27 and abrir==0) :
                print("Menu abre")
                raiz= Tk()
                opciones= Menu(raiz)
                raiz.mainloop()
    
        abrir=1
        if event.type==pygame.QUIT:
            sys.exit()
    if len(grafo.getVertices()) >0 :
        
        dibujarAristas(grafo)
        dibujarVertices(grafo)
    #conexo=grafo.esconexo()

    pygame.display.flip()
    clock.tick(20)