import xdrlib
import pygame
import random
import time

# initialize pygame
pygame.init()

# create game screen
screen = pygame.display.set_mode((1400, 800))
background = pygame.image.load('images/intersection2.png')

# player
car = pygame.image.load('images/up/car.png')
bus = pygame.image.load('images/down/bus.png')
bike = pygame.image.load('images/right/bike.png')
truck = pygame.image.load('images/right/truck.png')
green = pygame.image.load('images/signals/green.png')
red = pygame.image.load('images/signals/red.png')
yellow = pygame.image.load('images/signals/yellow.png')


# currentsignals
signall = ""
signalr = ""
signalu = ""
signald = ""


def player(vehicle, x, y):
    screen.blit(vehicle, (x, y))


# generating vehciles
def VehicleGenerate():
    dir = ''
    vehicle = ''
    x = 0
    y = 0
    num1 = random.randint(0, 3)
    if num1 == 0:
        dir = 'left'
    elif num1 == 1:
        dir = 'up'
    elif num1 == 2:
        dir = 'right'
    else:
        dir = 'down'
    if dir == 'left':
        num2 = random.randint(0, 3)
        if num2 == 0:
            vehicle = pygame.image.load('images/left/car.png')
        elif num2 == 1:
            vehicle = pygame.image.load('images/left/bike.png')
        elif num2 == 2:
            vehicle = pygame.image.load('images/left/bus.png')
        else:
            vehicle = pygame.image.load('images/left/truck.png')
        x = 30
        y = 385
    elif dir == 'up':
        num2 = random.randint(0, 3)
        if num2 == 0:
            vehicle = pygame.image.load('images/up/car.png')
        elif num2 == 1:
            vehicle = pygame.image.load('images/up/bike.png')
        elif num2 == 2:
            vehicle = pygame.image.load('images/up/bus.png')
        else:
            vehicle = pygame.image.load('images/up/truck.png')
        num3 = random.randint(0, 1)
        if num3 == 0:
            x = 765
            y = 20
        else:
            x = 700
            y = 20
    elif dir == 'right':
        num2 = random.randint(0, 3)
        if num2 == 0:
            vehicle = pygame.image.load('images/right/car.png')
        elif num2 == 1:
            vehicle = pygame.image.load('images/right/bike.png')
        elif num2 == 2:
            vehicle = pygame.image.load('images/right/bus.png')
        else:
            vehicle = pygame.image.load('images/right/truck.png')
        x = 1300
        y = 445
    else:
        num2 = random.randint(0, 3)
        if num2 == 0:
            vehicle = pygame.image.load('images/down/car.png')
        elif num2 == 1:
            vehicle = pygame.image.load('images/down/bike.png')
        elif num2 == 2:
            vehicle = pygame.image.load('images/down/bus.png')
        else:
            vehicle = pygame.image.load('images/down/truck.png')
        num3 = random.randint(0, 1)
        if num3 == 0:
            x = 570
            y = 700
        else:
            x = 640
            y = 700
    return vehicle, x, y, dir


clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
running = True
vehicles = []
xpos = []
ypos = []
dirs = []
vehiclegen = 4
counter = 10
sg = 'l'
flag = 0
vehiclecount = 0
while running:
    flag = 0
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            vehiclegen -= 1
            counter -= 1
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    if counter < 0:
        flag = 1
        if sg == 'l':
            sg = 'u'
        elif sg == 'u':
            sg = 'r'
        elif sg == 'r':
            sg = 'd'
        else:
            sg = 'l'
        counter = 10
    if counter >= 0 or flag == 1:
        if sg == 'l':
            signall='green'
            signalu='red'
            signalr='red'
            signald='red'
            screen.blit(green, (500, 250))
            screen.blit(red, (825, 250))
            screen.blit(red, (825, 525))
            screen.blit(red, (500, 525))
        elif sg == 'u':
            signall='red'
            signalu='green'
            signalr='red'
            signald='red'
            screen.blit(red, (500, 250))
            screen.blit(green, (825, 250))
            screen.blit(red, (825, 525))
            screen.blit(red, (500, 525))
        elif sg == 'r':
            signall='red'
            signalu='red'
            signalr='green'
            signald='red'
            screen.blit(red, (500, 250))
            screen.blit(red, (825, 250))
            screen.blit(green, (825, 525))
            screen.blit(red, (500, 525))
        else:
            signall='red'
            signalu='red'
            signalr='red'
            signald='green'
            screen.blit(red, (500, 250))
            screen.blit(red, (825, 250))
            screen.blit(red, (825, 525))
            screen.blit(green, (500, 525))

    v = ''
    x = 0
    y = 0
    dir = ''
    for i in range(vehiclecount):
        if dirs[i] == 'left':
            if signall=='green' or xpos[i]<=465 or xpos[i]>=535:
                xpos[i] += 1
        elif dirs[i] == 'up':
            if signalu=='green' or ypos[i]<=250 or ypos[i]>=300:
                ypos[i] += 1
        elif dirs[i] == 'right':
            if signalr=='green' or xpos[i]>=815 or xpos[i]<=745:
                xpos[i] -= 1
        else:
            if signald=='green' or ypos[i]>=535 or ypos[i]<=490:
                ypos[i] -= 1
    if vehiclegen <= 0:
        v, x, y, dir = VehicleGenerate()
        vehicles.append(v)
        xpos.append(x)
        ypos.append(y)
        dirs.append(dir)
        vehiclecount += 1
        vehiclegen = 4
    for i in range(vehiclecount):
        player(vehicles[i], xpos[i], ypos[i])
    clock.tick(60)

    pygame.display.update()
