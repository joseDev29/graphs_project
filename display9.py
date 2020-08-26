from Modelo.Grafo import *
from random import randint
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import json, pygame, sys

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
        for i in range(len(self.grafo.getVertices())):
            coordenadas= self.mapaPantalla[randint(0, len(self.mapaPantalla)-1)]
            if self.verificarCoordenada(coordenadas)==False:
                self.grafo.getVertices()[i].setCoordenadas(coordenadas)
                self.rellenarCoordenadas(coordenadas)
                self.coordenadasNoDisponibles.append(coordenadas)
            else:
                i=i-1
            
    def getDatosVertices(self):
        datosVertices=[]
        for vertice in self.grafo:
            datosVertices.append(vertice.getDato())

    def rellenarCoordenadas(self, punto):
        espacio=50
        inicial=[(punto[0]-espacio), (punto[1]-espacio)]
        final=[(punto[0]+espacio), (punto[1]+espacio)]

        for i in range((final[1]-inicial[1])+1):
            y=inicial[1]+i
            for k in range((final[0]-inicial[0])+1):
                x=inicial[0]+k
                self.coordenadasNoDisponibles.append([x,y])
        
    
    def mapearPantalla(self, pantalla):
        inicial=[50 , 50]
        final=[pantalla[0]-50 , pantalla[1]-50]
        
        for i in range((final[1]-inicial[1])+1):
            y=inicial[1]+i

            for k in range((final[0]-inicial[0])+1):
                x=inicial[0]+k

                self.mapaPantalla.append([x,y])
        print(self.mapaPantalla)

        return self.mapaPantalla
    
    def verificarCoordenada(self, coordenada):
        boolean= False
        for cord in self.coordenadasNoDisponibles:
            if cord[0]==coordenada[0] and cord[1]==coordenada[1]:
                boolean= True
        return boolean
    
"""class Menu():
    
    def __init__(self,master):
        self.frame=Frame(master)
        self.frame.pack(fill='both', expand="True")
        self.frame.config(width='200', height='300')
        self.frame.config(bg='gray')
        self.botones()

    def botones(self):
        boton1=Button(self.frame, text='Cargar Grafo',font=("Verdana",10), command=self.ventanaArchivo() ).place(x=10,y=10)
        boton2=Button(self.frame, text='Agregar vertice',font=("Verdana",10)).place(x=10,y=50)
        boton3=Button(self.frame, text='Obstruir camino',font=("Verdana",10)).place(x=10,y=100)
        boton4=Button(self.frame, text='Agregar Arista',font=("Verdana",10)).place(x=10,y=150)
        boton5=Button(self.frame, text='Dijkstra',font=("Verdana",10)).place(x=10,y=200)
        boton6=Button(self.frame, text='Minium Tree',font=("Verdana",10)).place(x=10,y=250)
    
    def ventanaArchivo(self):
        archivo = filedialog.askopenfilename(title="abrir", filetypes=(("json files","*.json")))"""


            
pantalla= [1000,600]
graficador= Mapeador(pantalla,grafo)
graficador.mapearPantalla(graficador.pantalla)
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

    for event in pygame.event.get():

        if event.type==pygame.MOUSEBUTTONDOWN:
            #print(event.pos)
            #NO OLVIDAR EL MACHETE
            if (event.pos[0]>=10 and event.pos[0]<=60) and (event.pos[1]>=10 and event.pos[1]<=27) :
                print("está dentro")
                """raiz= Tk()
                opciones= Menu(raiz)
                raiz.mainloop()"""
                
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
        pygame.draw.circle(screen,RED,vertice.getCoordenadas(),22)
        screen.blit(texto,[vertice.getCoordenadas()[0]-11, vertice.getCoordenadas()[1]-7])


    pygame.display.flip()
    clock.tick(60)