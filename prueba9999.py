from math import sqrt
pantalla=[800, 600]
r=10
origen=[40,40]
limites=[[origen[0],origen[1]-r],[origen[0]+r,origen[1]],[origen[0],origen[1]+r],[origen[0]-r,origen[1]]]

print(limites)

coordenadas=[]

for i in range(4):

    if i==0:
        x=limites[0][0]
        y=limites[0][1]
        while x < limites[1][0]:
            x+=1
            y+=1
            if(x>0 and x<pantalla[0] and y>25 and y<pantalla[1]):
                coordenadas.append([x,y])
            

    elif i==1:
        x=limites[1][0]
        y=limites[1][1]
        while x > limites[2][0]:
            x-=1
            y+=1
            if(x>0 and x<pantalla[0] and y>25 and y<pantalla[1]):
                coordenadas.append([x,y])
            

    elif i==2:
        x=limites[2][0]
        y=limites[2][1]
        while x > limites[3][0]:
            x-=1
            y-=1
            if(x>0 and x<pantalla[0] and y>25 and y<pantalla[1]):
                coordenadas.append([x,y])
            
    elif i==3:
        x=limites[3][0]
        y=limites[3][1]
        while x < limites[0][0]:
            x+=1
            y-=1
            if(x>0 and x<pantalla[0] and y>25 and y<pantalla[1]):
                coordenadas.append([x,y])
            
    else:
        print('Error, sector del plano no valido')

print(coordenadas)



print([41,32] in coordenadas)