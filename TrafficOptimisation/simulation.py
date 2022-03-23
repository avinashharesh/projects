import xdrlib
import pygame
import random
import time

#initialize pygame
pygame.init()

#create game screen
screen=pygame.display.set_mode((1400,800))
background=pygame.image.load('images/intersection2.png')

#player
car=pygame.image.load('images/right/car.png')
bus=pygame.image.load('images/right/bus.png')
bike=pygame.image.load('images/right/bike.png')
truck=pygame.image.load('images/right/truck.png')
green=pygame.image.load('images/signals/green.png')
red=pygame.image.load('images/signals/red.png')
yellow=pygame.image.load('images/signals/yellow.png')
Xl=30
Yl=400
Xr=1300
Yr=430
Xu=770
Yu=20
Xd=570
Yd=700

#currentsignals
signall=""
signalr=""
signalu=""
signald=""


def player(vehicle,x,y):
    screen.blit(vehicle,(x,y))



#generating vehciles
num1=random.randint(0,3)
if(num1==0):
    vehiclel=car
elif(num1==1):
    vehiclel=bus
elif(num1==2):
    vehiclel=bike
else:
    vehiclel=truck
num2=random.randint(0,3)
if(num2==0):
    vehicler=pygame.image.load('images/left/car.png')
elif(num2==1):
    vehicler=pygame.image.load('images/left/bus.png')
elif(num2==2):
    vehicler=pygame.image.load('images/left/bike.png')
else:
    vehicler=pygame.image.load('images/left/truck.png')
num3=random.randint(0,3)
if(num3==0):
    vehicleu=pygame.image.load('images/down/car.png')
elif(num3==1):
    vehicleu=pygame.image.load('images/down/bus.png')
elif(num3==2):
    vehicleu=pygame.image.load('images/down/bike.png')
else:
    vehicleu=pygame.image.load('images/down/truck.png')
num4=random.randint(0,3)
if(num4==0):
    vehicled=pygame.image.load('images/up/car.png')
elif(num4==1):
    vehicled=pygame.image.load('images/up/bus.png')
elif(num4==2):
    vehicled=pygame.image.load('images/up/bike.png')
else:
    vehicled=pygame.image.load('images/up/truck.png')


clock=pygame.time.Clock ()
counter=10
counter1=20
pygame.time.set_timer(pygame.USEREVENT,1000)
running=True
while running:
    if Xl<470 or signall=="green" or Xl>520:
        Xl+=1
    if Xr>820 or signalr=="green" or Xr<770:
        Xr-=1
    Yu+=1
    Yd-=1
    for event in pygame.event.get():
        if event.type==pygame.USEREVENT:
            counter-=1
            counter1-=1
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,0,0)) 
    screen.blit(background,(0,0))
    if counter1<=0:
        counter=10
        counter1=20
    if counter >=0:
        screen.blit(red,(500,250))
        signall="red"
    else:
        screen.blit(green,(500,250))
        signall="green"
    if counter>=0:
        screen.blit(green,(825,250))
        signalu="green"
    else:
        screen.blit(red,(825,250))
        signalu="red"
    if counter>=0:
        screen.blit(green,(500,525))
        signald="green"
    else:
        screen.blit(red,(500,525))
        signald="red"
    if counter >=0:
        screen.blit(red,(825,525))
        signalr="red"
    else:
        screen.blit(green,(825,525))
        signalr="green"
    
    player(vehiclel,Xl,Yl)
    player(vehicler,Xr,Yr)
    player(vehicleu,Xu,Yu)
    player(vehicled,Xd,Yd)
    clock.tick(60) 




    pygame.display.update()


