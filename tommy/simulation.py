# import xdrlib
import pygame
import random
import time

#initialize pygame
pygame.init()

#create game screen
screen=pygame.display.set_mode((1400,800))
background=pygame.image.load('images/mod_int.png')

#player
car=pygame.image.load('images/right/car.png')
bus=pygame.image.load('images/right/bus.png')
bike=pygame.image.load('images/right/bike.png')
truck=pygame.image.load('images/right/truck.png')
green=pygame.image.load('images/signals/green.png')
green1=pygame.image.load('images/signals/green1.png')
red=pygame.image.load('images/signals/red.png')
yellow=pygame.image.load('images/signals/yellow.png')
Xl=30
Yl=380
Xr=1300
Yr=450
Xu=700
Yu=-150
Xu1=758
Yu1=20
Xd=635
Yd=700
Xd1=575
Yd1=700
directionKey = {1:"right", 2:"left", 4:"up", 3:"down"}
vehicleClass = {0:"car", 1:"bike", 2:"bus", 3:"truck"}
#currentsignals
signall=""
signalr=""
signalu=""
signald=""

def player(vehicle,x,y):
    screen.blit(vehicle,(x,y))

directionKey = {1:"right", 2:"left", 3:"down", 4:"up"}
vehicleClass = {0:"car", 1:"bike", 2:"bus", 3:"truck"}


#generating vehicles
num1=random.randint(0,3)
k0 = 1
if(num1==0):
    path = "images/" + directionKey[k0] + "/" + vehicleClass[num1] + ".png"
    vehiclel=pygame.image.load(path)
elif(num1==1):
    path = "images/" + directionKey[k0] + "/" + vehicleClass[num1] + ".png"
    vehiclel=pygame.image.load(path)
elif(num1==2):
    path = "images/" + directionKey[k0] + "/" + vehicleClass[num1] + ".png"
    vehiclel=pygame.image.load(path)
else:
    path = "images/" + directionKey[k0] + "/" + vehicleClass[num1] + ".png"
    vehiclel=pygame.image.load(path)

    
num2=random.randint(0,3)

k1 = 2
if(num2==0):
    path = "images/" + directionKey[k1] + "/" + vehicleClass[num2] + ".png"
    vehicler=pygame.image.load(path)
elif(num2==1):
    path = "images/" + directionKey[k1] + "/" + vehicleClass[num2] + ".png"
    vehicler=pygame.image.load(path)
elif(num2==2):
    path = "images/" + directionKey[k1] + "/" + vehicleClass[num2] + ".png"
    vehicler=pygame.image.load(path)
else:
    path = "images/" + directionKey[k1] + "/" + vehicleClass[num2] + ".png"
    vehicler=pygame.image.load(path)
num3=random.randint(0,3)
k2=3
if(num3==0):
    path = "images/" + directionKey[k2] + "/" + vehicleClass[num3] + ".png"
    vehicleu=pygame.image.load(path)
elif(num3==1):
    path = "images/" + directionKey[k2] + "/" + vehicleClass[num3] + ".png"
    vehicleu=pygame.image.load(path)
elif(num3==2):
    path = "images/" + directionKey[k2] + "/" + vehicleClass[num3] + ".png"
    vehicleu=pygame.image.load(path)
else:
    path = "images/" + directionKey[k2] + "/" + vehicleClass[num3] + ".png"
    vehicleu=pygame.image.load(path)
num4=random.randint(0,3)
k3 = 4
if(num4==0):
    path = "images/" + directionKey[k3] + "/" + vehicleClass[num4] + ".png"
    vehicled=pygame.image.load(path)
elif(num4==1):
    path = "images/" + directionKey[k3] + "/" + vehicleClass[num4] + ".png"
    vehicled=pygame.image.load(path)
elif(num4==2):
    path = "images/" + directionKey[k3] + "/" + vehicleClass[num4] + ".png"
    vehicled=pygame.image.load(path)
else:
    path = "images/" + directionKey[k3] + "/" + vehicleClass[num4] + ".png"
    vehicled=pygame.image.load(path)

newPath = "images/" + directionKey[k2] + "/" + vehicleClass[num1] + ".png"
vehicleLD = pygame.image.load(newPath)

newpath1 = "images/" + directionKey[k1] + "/" + vehicleClass[num3] + ".png"
vehicleDL = pygame.image.load(newpath1)

clock=pygame.time.Clock ()
counter=10
counter2=2
fl=1
fu=1
fr=1
fd=1
sg='l'
vehicle1=pygame.image.load('images/down/bus.png')
vehicle2=pygame.image.load('images/up/truck.png')
pygame.time.set_timer(pygame.USEREVENT,1000)
flag=0
running=True
while running:
    #or signall=='green' or Xl>600:
    if Xl<700:
        Xl+=1.5  
    else:
        vehiclel = vehicleLD
        Yl+=1      
    if Xr>820 or signalr=='green' or Xr<500:
        Xr-=1
    if Yu<250 or signalu=='green':
        Yu+=1 
           
    if Yu1<250 or signalu=='green':
        Yu1+=1      
    if Yd>540 or signald=='green':
        Yd-=1
    if Yd1>540 or signald=='green':
        Yd1-=1    
    for event in pygame.event.get():
        if event.type==pygame.USEREVENT:
            counter-=1
            counter2-=1
        if event.type==pygame.QUIT:
            running=False
    screen.fill((0,0,0)) 
    screen.blit(background,(0,0))
    if counter < 0:
        if sg == 'l':
            fl=0
            sg = 'u'
        elif sg == 'u':
            fu=0
            sg = 'r'
        elif sg == 'r':
            fr=0
            sg = 'd'
        else:
            fd=0
            sg = 'l'
        counter = 10
    if counter >= 0 or flag == 1:
        if sg == 'l':
            if fd==0:
                counter2=2
                fd=1
            if counter2>=0:
                signald='yellow'
            else:
                signald='red'
            signall='green'
            signalu='red'
            signalr='red'
            screen.blit(green1, (500, 250))
            screen.blit(red, (825, 250))
            screen.blit(red, (825, 525))
            if signald=='yellow':
                screen.blit(yellow, (500, 525))
            else:
                screen.blit(red,(500,525))
        elif sg == 'u':
            if fl==0:
                counter2=2
                fl=1
            if counter2>=0:
                signall='yellow'
            else:
                signall='red'
            signalu='green'
            signalr='red'
            signald='red'
            if signall=='yellow':
                screen.blit(yellow, (500, 250))
            else:
                screen.blit(red,(500,250))
            screen.blit(green1, (825, 250))
            screen.blit(red, (825, 525))
            screen.blit(red, (500, 525))
        elif sg == 'r':
            if fu==0:
                counter2=2
                fu=1
            if counter2>=0:
                signalu='yellow'
            else:
                signalu='red'
            signall='red'
            signalr='green'
            signald='red'
            screen.blit(red, (500, 250))
            if signalu=='yellow':
                screen.blit(yellow, (825, 250))
            else:
                screen.blit(red,(825,250))
            screen.blit(green1, (825, 525))
            screen.blit(red, (500, 525))
        else:
            if fr==0:
                counter2=2
                fr=1
            if counter2>=0:
                signalr='yellow'
            else:
                signalr='red'
            signall='red'
            signalu='red'
            signald='green'
            screen.blit(red, (500, 250))
            screen.blit(red, (825, 250))
            if signalr=='yellow':
                screen.blit(yellow, (825, 525))
            else:
                screen.blit(red,(825,525))
            screen.blit(green1, (500, 525))
    player(vehiclel,Xl,Yl)
    player(vehicler,Xr,Yr)
    player(vehicleu,Xu,Yu)
    player(vehicle1,Xu1,Yu1)
    player(vehicled,Xd,Yd)
    player(vehicle2,Xd1,Yd1)
    clock.tick(60) 
    pygame.display.update()
