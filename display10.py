from Modelo.Grafo import *
from random import randint
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
import json, pygame, sys
import os
abrir=0

with open('Data/grafo1.json') as myJSON:
   myFile = json.load(myJSON)

grafo= Grafo()

for vertice in myFile["vertices"]:
    grafo.IngresarVertice(vertice)

for arista in myFile["aristas"]:
    grafo.IngresarAristas(arista[0],arista[1],arista[2])

#print(grafo)
#-orden-#

"""class Game(object):
    
    def __init__(self):
        self.score=0
        self.game_over= False
        self.meteor_list=pygame.sprite.Group()
        self.all_sprites_list=pygame.sprite.Group()

        for vertice in grafo.ListaVertices():
            meteor=Meteor()
            meteor.rect.x=random.randrange(screen_width)
            meteor.rect.y=random.randrange(screen_height)
            self.meteor_list.add(meteor)
            self.all_sprites_list.add(meteor)

        self.player=Player()
        self.all_sprites_list.add(self.player)
    def process_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                return True
            if event.type==pygame.MOUSEBUTTONDOWN:
                if self.game_over:
                    self.__init__()
        return False
    def run_logic(self):
        if not self.game_over:
            self.all_sprites_list.update()
            meteor_hit_list=pygame.sprite.spritecollide(self.player, self.meteor_list, True)

            for meteor in meteor_hit_list:
                self.score+=1
                print(self.score)

            if len(self.meteor_list)==0:
                self.game_over= True

    def display_frame(self,screen):
        
        screen.fill(white)
        if self.game_over:
            font=pygame.font.SysFont("serif",25)
            text=font.render("Game Over, Click to Continue",True,black)
            center_x=(screen_width//2)-(text.get_width()//2)
            center_y=(screen_height//2)-(text.get_height()//2)
            screen.blit(text,[center_x,center_y])
        if not self.game_over:
            self.all_sprites_list.draw(screen)
        pygame.display.flip()


def main():
    pygame.init()
    screen=pygame.display.set_mode([screen_width,screen_height])
    done= False
    clock=pygame.time.Clock()
    game=Game()
    while not done:
        done=game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()

if __name__=="__main__":
    main()"""
#-orden-#
class Mapeador():

    def __init__(self, pantalla, grafo):
        
        self.coordenadasVertices=[]
        self.pantalla= pantalla
        self.coordenadasNoDisponibles=[]
        self.grafo= grafo
        self.mapaPantalla=[]

    def mapearGrafo(self):
        """for i in range(len(self.grafo.getVertices())):
            coordenadas= self.mapaPantalla[randint(0, len(self.mapaPantalla)-1)]
            if self.verificarCoordenada(coordenadas)==False:
                self.grafo.getVertices()[i].setCoordenadas(coordenadas)
                self.rellenarCoordenadas(coordenadas)
                self.coordenadasNoDisponibles.append(coordenadas)
            else:
                i=i-1"""
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
        
            
    """def mapearPantalla(self, pantalla):
        inicial=[50 , 50]
        final=[pantalla[0]-50 , pantalla[1]-50]
        
        for i in range((final[1]-inicial[1])):
            y=inicial[1]+i

            for k in range((final[0]-inicial[0])):
                x=inicial[0]+k

                self.mapaPantalla.append([x,y])
        
        print(len(self.mapaPantalla))
        print(self.mapaPantalla)
        return self.mapaPantalla"""

    def rellenar(self, inicial, final):
        tmp=[]
        for i in range((final[1]-inicial[1])):
            y=inicial[1]+i

            for k in range((final[0]-inicial[0])):
                x=inicial[0]+k

                tmp.append([x,y])

        self.mapaPantalla.append(tmp)
        
        
        
    
    """def mapearPantalla2(self):
        pantalla= self.pantalla
        inicial=[50,50]; final=[150,150]; limite=[950,550]

        while inicial[1]<limite[1]:

            while not (inicial[0] > final[0] or inicial[1] > final[1]):
                tmp=[]
                for i in range((final[1]-inicial[1])+1):
                    y=inicial[1]+i

                    for k in range((final[0]-inicial[0])+1):
                        x=inicial[0]+k
            
        print(len(self.mapaPantalla))"""
    
    def verificarCoordenada(self, coordenada):
        boolean= False
        for cord in self.coordenadasNoDisponibles:
            if cord[0]==coordenada[0] and cord[1]==coordenada[1]:
                boolean= True
        return boolean
    
class Menu(Frame):
    def __init__(self,master=None):
        super().__init__(master,width=200,height=300)
        self.master=master
        self.pack()
        self.crear_botones()
        #self.transient(master)
    def crear_botones(self):
        #Se instancian los botones
        self.btnCargarGrafo=Button(self,text="Cargar Grafo",command=self.ventanaArchivo)
        self.btnObstruirCamino=Button(self,text='Obstruir camino',command=self.prueba)
        self.btnPrueba=Button(self,text="Agregar Vertice",command=self.hija)
        self.btnAgregarArista=Button(self, text='Agregar Arista',command=self.prueba)
        self.btnDijkstra=Button(self, text='Dijkstra',command=self.prueba)
        self.btnMiniumTree=Button(self, text='Minium Tree',command=self.prueba)
        #Se les da posición a los botones
        self.btnCargarGrafo.place(x=10,y=10,width=100,height=30)
        self.btnPrueba.place(x=10,y=50,width=100,height=30)
        self.btnObstruirCamino.place(x=10,y=100,width=100,height=30)
        self.btnAgregarArista.place(x=10,y=150,width=100,height=30)
        self.btnDijkstra.place(x=10,y=200,width=100,height=30)
        self.btnMiniumTree.place(x=10,y=250,width=100,height=30)
        
    
    def prueba(self):
        print("hola")

    def ventanaArchivo(self):
        archivo = filedialog.askopenfilename(initialdir="/",title="Cargar Grafo", filetypes=(("json files","*.json"),("all files",".")))
        print(archivo)

    def hija(self):
        t1 = Toplevel(self,bg="blue")
 
    ## Establece el tamaño para la ventana.
        t1.geometry('400x200+20+20')
    
        ## Provoca que la ventana tome el focus
        t1.focus_set()
    
        ## Deshabilita todas las otras ventanas hasta que
        ## esta ventana sea destruida.
        t1.grab_set()
    
        ## Indica que la ventana es de tipo transient, lo que significa
        ## que la ventana aparece al frente del padre.
        t1.transient(master=self)
    
        ## Crea un widget Label en la ventana
        Label(t1, text='Ventana hija',bg="blue").pack(padx=10, pady=10)
    
        ## Crea un widget que permite cerrar la ventana,
        ## para ello indica que el comando a ejecutar es el
        ## metodo destroy de la misma ventana.
        Button(t1,text="Cerrar",bg="green", command=t1.destroy).pack()
    
        ## Crea un entry.
        e=Entry(t1,bg="lightyellow")
    
        ## Establece el focus en el entry.
        e.focus()
        e.pack()
    
        Button(t1,text="Saludar",bg="green", command=self.prueba(e)).pack()
        ## Pausa el mainloop de la ventana de donde se hizo la invocación.
        t1.wait_window(t1)
    def saludar2(self,entrada):
        print(entrada)

            
pantalla= [1000,600]
graficador= Mapeador(pantalla,grafo)
graficador.algo()
graficador.mapearGrafo()


pygame.init()

#Definir colores
BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
SUPERBLUE= (40, 210, 250)
size=(graficador.pantalla[0],graficador.pantalla[1])

fuente=pygame.font.Font(None,30)

#Crear ventana
screen=pygame.display.set_mode(size)
#Controlar los FPS
clock=pygame.time.Clock()

while True:
    abrir=0
    for event in pygame.event.get():

        if event.type==pygame.MOUSEBUTTONDOWN:
            #print(event.pos)
            #NO OLVIDAR EL MACHETE
            if (event.pos[0]>=10 and event.pos[0]<=60) and (event.pos[1]>=10 and event.pos[1]<=27) and abrir==0 :
                raiz=Tk()
                opciones= Menu(raiz)
                opciones.mainloop()
        abrir=1
        if event.type==pygame.QUIT:
            sys.exit()

    screen.fill(WHITE)
    pygame.draw.rect(screen,BLACK,(8,8,54,21))
    pygame.draw.rect(screen,RED,(10,10,50,17))

    for vertice in grafo.getVertices():

        for adyacente in vertice.getListaAdyacentes():
            pygame.draw.line(screen, SUPERBLUE, (vertice.getCoordenadas()[0],vertice.getCoordenadas()[1]),(adyacente.getCoordenadas()[0],adyacente.getCoordenadas()[1]), 1)
    
    for vertice in grafo.getVertices():
        texto=fuente.render(vertice.getDato(),0,BLUE)
        pygame.draw.circle(screen,BLACK,vertice.getCoordenadas(),24)
        #print('coordenadas de {0} : {1}'.format(vertice.getDato(), vertice.getCoordenadas()))
        pygame.draw.circle(screen,RED,vertice.getCoordenadas(),22)
        screen.blit(texto,[vertice.getCoordenadas()[0]-11, vertice.getCoordenadas()[1]-7])


    pygame.display.flip()
    clock.tick(60)