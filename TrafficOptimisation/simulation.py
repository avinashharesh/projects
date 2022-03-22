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

def player(vehicle,x,y):
    screen.blit(vehicle,(x,y))
clock=pygame.time.Clock()
start=5



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
    vehicleu=pygame.image.load('images/up/car.png')
elif(num3==1):
    vehicleu=pygame.image.load('images/up/bus.png')
elif(num3==2):
    vehicleu=pygame.image.load('images/up/bike.png')
else:
    vehicleu=pygame.image.load('images/up/truck.png')
num4=random.randint(0,3)
if(num4==0):
    vehicled=pygame.image.load('images/down/car.png')
elif(num4==1):
    vehicled=pygame.image.load('images/down/bus.png')
elif(num4==2):
    vehicled=pygame.image.load('images/down/bike.png')
else:
    vehicled=pygame.image.load('images/down/truck.png')



#game loop
running=True
while running:
    Xl+=1
    Xr-=1
    Yu+=1
    Yd-=1
    if(start<0):
        vehicler=bike
    start-=1
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,0,0)) 
    screen.blit(background,(0,0))
    screen.blit(red,(500,250))
    screen.blit(red,(825,250))
    screen.blit(red,(500,525))
    screen.blit(red,(825,525))
    player(vehiclel,Xl,Yl)
    player(vehicler,Xr,Yr)
    player(vehicleu,Xu,Yu)
    player(vehicled,Xd,Yd) 
    clock.tick(1000)



    pygame.display.update()


