import pygame,sys,random
from tkinter import *
from tkinter import ttk
from functools import partial
pygame.init()
fuente=pygame.font.Font(None,48)
cont2=0
cont=0
class vaina():
    def __init__(self):
        self.cosa= False
        self.x=0
        self.y=0
        self.const=0
    def saludar(self):
        print("holafuncions")
        self.cosa=True
        self.x=random.randint(0,800)
        self.y=random.randint(0,600)
        self.const+=1
        raiz.destroy()
        
v= vaina()
    
black=(0,0,0)
white=(255,255,255)
screen_size=(800,600)
texto=fuente.render("Hola",0,white)

player_width=15
player_height=90
player1_score=0
player2_score=0
screen=pygame.display.set_mode(screen_size)
clock=pygame.time.Clock()
#coordenadas y velocidad de jugador 1
player1_x_coor=50
player1_y_coor=300-45
player1_y_speed=0
#coordenadas y velocidad de jugador 2
player2_x_coor=700
player2_y_coor=300-45
player2_y_speed=0
#coordenadas de la pelota
pelota_x=400
pelota_y=300
pelota_speed_x=5
pelota_speed_y=5

game_over=False

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            #jugador 1
            if event.key==pygame.K_w:
                player1_y_speed=-6
            if event.key==pygame.K_s:
                player1_y_speed=6
            #jugador 2
            if event.key==pygame.K_UP:
                player2_y_speed=-6
            if event.key==pygame.K_DOWN:
                player2_y_speed=6

        if event.type==pygame.KEYUP:
            #jugador 1
            if event.key==pygame.K_w:
                player1_y_speed=0
            if event.key==pygame.K_s:
                player1_y_speed=0
            #jugador 2
            if event.key==pygame.K_UP:
                player2_y_speed=0
            if event.key==pygame.K_DOWN:
                player2_y_speed=0

        

    #fondo pantalla
    screen.fill(black)
    # Modifica las coordenadas para dar movimiento a los objetos
    player1_y_coor+=player1_y_speed
    player2_y_coor+=player2_y_speed

    #reinicio de posicion al salir de pantalla
    if pelota_y>590 or pelota_y<10:
        pelota_speed_y*=-1
    #coordenadas x
    if pelota_x>800:
        player1_score+=1
        print(player1_score)
        pelota_x=400
        pelota_y=300
        pelota_speed_x*=-1
        pelota_speed_y*=-1
    if pelota_x<0:
        player2_score+=1
        print(player2_score)
        
        
        pelota_x=400
        pelota_y=300
        pelota_speed_x*=-1
        pelota_speed_y*=-1

    if (0<player2_score<2 and cont==0)or(2<player2_score<4 and v.const==1):
        cont+=1
        raiz= Tk()
        frame1= Frame(raiz)
        frame1.pack(fill='both', expand="True")
        frame1.config(bg='limegreen')
        frame1.config(width='300', height='200')
        
        boton=ttk.Button(raiz, text='Saludar', command=v.saludar).pack(side=BOTTOM)
        print(boton)
        print(cont)
        
        raiz.mainloop()
        print(raiz.after_cancel(frame1))
    if v.cosa:
        screen.blit(texto,(v.x,v.y))
    #coordenadas y
    if player1_y_coor<0:
        player1_y_coor=0
    elif player1_y_coor>510:
        player1_y_coor=510
    if player2_y_coor<0:
        player2_y_coor=0
    elif player2_y_coor>510:
        player2_y_coor=510


    #--------Zona de dibujo------
    jugador1=pygame.draw.rect(screen,white,(player1_x_coor,player1_y_coor,player_width,player_height))
    jugador2=pygame.draw.rect(screen,white,(player2_x_coor,player2_y_coor,player_width,player_height))
    pelota=pygame.draw.circle(screen,white,(pelota_x,pelota_y),10)
    #--------Zona de dibujo------
    #colisiones
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pelota_speed_x*=-1
    pelota_x+=pelota_speed_x
    pelota_y+=pelota_speed_y
    pygame.display.flip()
    clock.tick(60)

pygame.quit()