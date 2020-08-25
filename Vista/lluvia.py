import pygame,sys,random

pygame.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)
BLUE = (0,0,255)
size=(800,500)
screen=pygame.display.set_mode(size)
clock=pygame.time.Clock()
coor_list=[]
for i in range(10):
        x=random.randint(0,800)
        y=random.randint(0,500)
        pygame.draw.circle(screen,RED,(x,0),5)
        coor_list.append([x,y])
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
    screen.fill(WHITE)
    for coord in coor_list:
        x=coord[0]
        y=coord[1]
        pygame.draw.circle(screen,RED,(x,y),1)
        coord[1]+=1
        
    
pygame.display.flip()
clock.tick(60)