import pygame, sys, tkinter
from pygame.locals import *

pygame.init()

venta=pygame.display.set_mode((400,300))
pygame.display.set_caption("hola mundo")

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
    
    
    pygame.display.update()