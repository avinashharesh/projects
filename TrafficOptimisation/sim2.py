import pygame
import random
import time


# initialize pygame
pygame.init()

# create game screen
screen = pygame.display.set_mode((1400, 800))
background = pygame.image.load('images/intersection2.png')

# players
carl = pygame.image.load('images/left/car.png')
carll30 = pygame.image.load('images/left/carl30.png')
carll60 = pygame.image.load('images/left/carl60.png')
carll90 = pygame.image.load('images/left/carl90.png')
carr = pygame.image.load('images/right/car.png')
caru = pygame.image.load('images/up/car.png')
carul30 = pygame.image.load('images/up/carl30.png')
carul60 = pygame.image.load('images/up/carl60.png')
carul90 = pygame.image.load('images/up/carl90.png')
card = pygame.image.load('images/down/car.png')
cardl30 = pygame.image.load('images/down/carl30.png')
cardl60 = pygame.image.load('images/down/carl60.png')
cardl90 = pygame.image.load('images/down/carl90.png')
busl = pygame.image.load('images/left/bus.png')
busll30 = pygame.image.load('images/left/busl30.png')
busll60 = pygame.image.load('images/left/busl60.png')
busll90 = pygame.image.load('images/left/busl90.png')
busr = pygame.image.load('images/right/bus.png')
busd = pygame.image.load('images/down/bus.png')
busdl30 = pygame.image.load('images/down/busl30.png')
busdl60 = pygame.image.load('images/down/busl60.png')
busdl90 = pygame.image.load('images/down/busl90.png')
busu = pygame.image.load('images/up/bus.png')
busul30 = pygame.image.load('images/up/busl30.png')
busul60 = pygame.image.load('images/up/busl60.png')
busul90 = pygame.image.load('images/up/busl90.png')
truckl = pygame.image.load('images/left/truck.png')
truckll30 = pygame.image.load('images/left/truckl30.png')
truckll60 = pygame.image.load('images/left/truckl60.png')
truckll90 = pygame.image.load('images/left/truckl90.png')
truckr = pygame.image.load('images/right/truck.png')
truckd = pygame.image.load('images/down/truck.png')
truckdl30 = pygame.image.load('images/down/truckl30.png')
truckdl60 = pygame.image.load('images/down/truckl60.png')
truckdl90 = pygame.image.load('images/down/truckl90.png')
trucku = pygame.image.load('images/up/truck.png')
truckul30 = pygame.image.load('images/up/truckl30.png')
truckul60 = pygame.image.load('images/up/truckl60.png')
truckul90 = pygame.image.load('images/up/truckl90.png')
bikel = pygame.image.load('images/left/bike.png')
bikell30 = pygame.image.load('images/left/bikel30.png')
bikell60 = pygame.image.load('images/left/bikel60.png')
bikell90 = pygame.image.load('images/left/bikel90.png')
biker = pygame.image.load('images/right/bike.png')
biked = pygame.image.load('images/down/bike.png')
bikedl30 = pygame.image.load('images/down/bikel30.png')
bikedl60 = pygame.image.load('images/down/bikel60.png')
bikedl90 = pygame.image.load('images/down/bikel90.png')
bikeu = pygame.image.load('images/up/bike.png')
bikeul30 = pygame.image.load('images/up/bikel30.png')
bikeul60 = pygame.image.load('images/up/bikel60.png')
bikeul90 = pygame.image.load('images/up/bikel90.png')
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
    turn = ''
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
            vehicle = carl
        elif num2 == 1:
            vehicle = bikel
        elif num2 == 2:
            vehicle = busl
        else:
            vehicle = truckl
        x = 10
        y = 385
        num3 = random.randint(0, 6)
        if num3 == 0:
            turn = 'l'
        elif num3 == 1:
            turn = 'r'
        else:
            turn = 's'
    elif dir == 'up':
        num2 = random.randint(0, 3)
        if num2 == 0:
            vehicle = caru
        elif num2 == 1:
            vehicle = bikeu
        elif num2 == 2:
            vehicle = busu
        else:
            vehicle = trucku
        num3 = random.randint(0, 1)
        if num3 == 0:
            x = 765
            y = 5
            num4 = random.randint(0, 4)
            if num4 == 0:
                turn = 'l'
            else:
                turn = 's'
        else:
            x = 700
            y = 5
            num4 = random.randint(0, 4)
            if num4 == 0:
                turn = 'r'
            else:
                turn = 's'
    elif dir == 'right':
        num2 = random.randint(0, 3)
        if num2 == 0:
            vehicle = carr
        elif num2 == 1:
            vehicle = biker
        elif num2 == 2:
            vehicle = busr
        else:
            vehicle = truckr
        x = 1350
        y = 445
        num3 = random.randint(0, 6)
        if num3 == 0:
            turn = 'l'
        elif num3 == 1:
            turn = 'r'
        else:
            turn = 's'
    else:
        num2 = random.randint(0, 3)
        if num2 == 0:
            vehicle = card
        elif num2 == 1:
            vehicle = biked
        elif num2 == 2:
            vehicle = busd
        else:
            vehicle = truckd
        num3 = random.randint(0, 1)
        if num3 == 0:
            x = 570
            y = 760
            num4 = random.randint(0, 4)
            if num4 == 0:
                turn = 'l'
            else:
                turn = 's'
        else:
            x = 640
            y = 760
            num4 = random.randint(0, 4)
            if num4 == 0:
                turn = 'r'
            else:
                turn = 's'

    return vehicle, x, y, dir, turn


clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)
running = True
vehicles = []
xpos = []
ypos = []
dirs = []
turns = []
turned = []
ql = []
vehiclegen = 2
counter = 10
counter2 = 2
sg = 'l'
a = 0
fl = 1
fu = 1
fr = 1
fd = 1
temp = 0
vehiclecount = 0
vehiclel = []
vehiclelcount = 0
hell = 10
hev = 385
while running:
    flag = 0
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            vehiclegen -= 1
            counter -= 1
            counter2 -= 1
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    # screen.blit(car, (590, 310))
    # screen.blit(bus,(565-70*2,385))
    # screen.blit(bike, (495, 385))
    # screen.blit(car, (1350, 445))
    # screen.blit(car, (1280, 445))
    # screen.blit(car,(835,445))
    # screen.blit(car,(935,445))
    # screen.blit(car, (765, 250))
    # screen.blit(car, (765, 300))
    # screen.blit(car, (hell, hev))
    # if hell >= 100:
    #     car = rot_center(car, -90)
    #     hell += 1
    # hell += 1
    # if hev <= 430 and hev >= 410:
    #     if hev == 430:
    #         bike = pygame.transform.rotate(bike, 30)
    #     elif hev == 420:
    #         bike = pygame.transform.rotate(bike, 30)
    #     elif hev == 410:
    #         bike = pygame.transform.rotate(bike, 30)
    #     hev -= 1
    # else:
    #     if hev < 410:
    #         hell -= 1
    #     else:
    #         hev -= 1

    if counter < 0:
        if sg == 'l':
            fl = 0
            sg = 'u'
        elif sg == 'u':
            fu = 0
            sg = 'r'
        elif sg == 'r':
            fr = 0
            sg = 'd'
        else:
            fd = 0
            sg = 'l'
        counter = 10
    if counter >= 0 or flag == 1:
        if sg == 'l':
            if fd == 0:
                counter2 = 2
                fd = 1
            if counter2 >= 0:
                signald = 'yellow'
            else:
                signald = 'red'
            signall = 'green'
            signalu = 'red'
            signalr = 'red'
            screen.blit(red, (825, 250))
            screen.blit(red, (825, 525))
            if signald == 'yellow':
                screen.blit(yellow, (500, 525))
            else:
                screen.blit(red, (500, 525))
            fdb = 0
            for m in range(vehiclecount):
                if (ypos[m] in range(490, 310, -1) and dirs[m] == 'down' and turns[m] == 's') or (ypos[m] <= 490 and turned[m] == 0 and dirs[m] == 'down' and turns[m] == 'r') or (ypos[m] <= 490 and turned[m] == 0 and dirs[m] == 'down' and turns[m] == 'l'):
                    fdb = 1
                    break
            if fdb == 1:
                signall = 'red'
                screen.blit(red, (500, 250))
            else:
                signall = 'green'
                screen.blit(green, (500, 250))

        elif sg == 'u':
            if fl == 0:
                counter2 = 2
                fl = 1
            if counter2 >= 0:
                signall = 'yellow'
            else:
                signall = 'red'
            signalr = 'red'
            signald = 'red'
            if signall == 'yellow':
                screen.blit(yellow, (500, 250))
            else:
                screen.blit(red, (500, 250))
            flb = 0
            for w in range(vehiclecount):
                if (xpos[w] in range(495, 765) and dirs[w] == 'left' and turns[w] == 's') or (xpos[w] >= 495 and turned[w] == 0 and dirs[w] == 'left' and turns[w] == 'l') or (xpos[w] >= 495 and turned[w] == 0 and dirs[w] == 'left' and turns[w] == 'r'):
                    flb = 1
                    break
            if flb == 1:
                signalu = 'red'
                screen.blit(red, (825, 250))
            else:
                signalu = 'green'
                screen.blit(green, (825, 250))
            screen.blit(red, (825, 525))
            screen.blit(red, (500, 525))
        elif sg == 'r':
            if fu == 0:
                counter2 = 2
                fu = 1
            if counter2 >= 0:
                signalu = 'yellow'
            else:
                signalu = 'red'
            signall = 'red'
            signald = 'red'
            screen.blit(red, (500, 250))
            if signalu == 'yellow':
                screen.blit(yellow, (825, 250))
            else:
                screen.blit(red, (825, 250))
            fub = 0
            for y in range(vehiclecount):
                if (ypos[y] in range(310, 500) and dirs[y] == 'up' and turns[y] == 's') or (ypos[y] >= 310 and turned[y] == 0 and dirs[y] == 'up' and turns[y] == 'l') or (ypos[y] >= 310 and turned[y] == 0 and dirs[y] == 'up' and turns[y] == 'r'):
                    fub = 1
                    break
            if fub == 1:
                signalr = 'red'
                screen.blit(red, (825, 525))

            else:
                signalr = 'green'
                screen.blit(green, (825, 525))

            screen.blit(red, (500, 525))
        else:
            ls = 0
            if fr == 0:
                counter2 = 2
                fr = 1
            if counter2 >= 0:
                signalr = 'yellow'
            else:
                signalr = 'red'
            signall = 'red'
            signalu = 'red'
            signald = 'green'
            screen.blit(red, (500, 250))
            screen.blit(red, (825, 250))
            if signalr == 'yellow':
                screen.blit(yellow, (825, 525))
            else:
                screen.blit(red, (825, 525))
            frb = 0
            for z in range(vehiclecount):
                if (xpos[z] in range(780, 520, -1) and dirs[z] == 'right' and turns[z] == 's') or (xpos[z] <= 780 and turned[z] == 0 and dirs[z] == 'right' and turns[z] == 'l') or (xpos[z] <= 780 and turned[z] == 0 and dirs[z] == 'right' and turns[z] == 'r'):
                    frb = 1
                    break
            if frb == 1:
                signald = 'red'
                screen.blit(red, (500, 525))
            else:
                signald = 'green'
                screen.blit(green, (500, 525))
    v = ''
    x = 0
    y = 0
    dir = ''
    for i in range(vehiclecount):
        if dirs[i] == 'left':
            if signall == 'red' or signall == 'yellow':
                if xpos[i] > 496:
                    if turns[i] == 'l':
                        if xpos[i] >= 560 and xpos[i] <= 580:
                            if xpos[i] == 560:
                                if vehicles[i] == carl:
                                    vehicles[i] = carll30
                                elif vehicles[i] == busl:
                                    vehicles[i] = busll30
                                elif vehicles[i] == truckl:
                                    vehicles[i] = truckll30
                                elif vehicles[i] == bikel:
                                    vehicles[i] = bikell30
                            elif xpos[i] == 570:
                                if vehicles[i] == carll30:
                                    vehicles[i] = carll60
                                elif vehicles[i] == busll30:
                                    vehicles[i] = busll60
                                elif vehicles[i] == truckll30:
                                    vehicles[i] = truckll60
                                elif vehicles[i] == bikell30:
                                    vehicles[i] = bikell60
                            elif xpos[i] == 580:
                                if vehicles[i] == carll60:
                                    vehicles[i] = carll90
                                elif vehicles[i] == busll60:
                                    vehicles[i] = busll90
                                elif vehicles[i] == truckll60:
                                    vehicles[i] = truckll90
                                elif vehicles[i] == bikell60:
                                    vehicles[i] = bikell90
                            xpos[i] += 1
                            ypos[i] -= 2
                        else:
                            if xpos[i] > 580:
                                if ypos[i] <= 310:
                                    turned[i] = 1
                                ypos[i] -= 1
                            else:
                                xpos[i] += 1
                    elif turns[i] == 'r':
                        if xpos[i] >= 635 and xpos[i] <= 655:
                            pos1 = pygame.transform.rotate(vehicles[i], -30)
                            pos2 = pygame.transform.rotate(vehicles[i], -30)
                            pos3 = pygame.transform.rotate(vehicles[i], -30)
                            if xpos[i] == 635:
                                vehicles[i] = pos1
                            elif xpos[i] == 645:
                                vehicles[i] = pos2
                            elif xpos[i] == 655:
                                vehicles[i] = pos3
                            xpos[i] += 1
                        else:
                            if xpos[i] > 655:
                                if ypos[i] >= 500:
                                    turned[i] = 1
                                ypos[i] += 1
                            else:
                                xpos[i] += 1
                    else:
                        xpos[i] += 1
                else:
                    k = 0
                    for j in range(vehiclecount):
                        if xpos[j] in range(435-100*k, 495-100*k) and j != i and ypos[j] == 385:
                            k += 1
                    if xpos[i] >= 435-100*k and xpos[i] <= 495:
                        xpos[i] = xpos[i]
                    else:
                        xpos[i] += 1
            else:
                if turns[i] == 's':
                    xpos[i] += 1
                elif turns[i] == 'l':
                    if xpos[i] >= 560 and xpos[i] <= 580:
                        if xpos[i] == 560:
                            if vehicles[i] == carl:
                                vehicles[i] = carll30
                            elif vehicles[i] == busl:
                                vehicles[i] = busll30
                            elif vehicles[i] == truckl:
                                vehicles[i] = truckll30
                            elif vehicles[i] == bikel:
                                vehicles[i] = bikell30
                        elif xpos[i] == 570:
                            if vehicles[i] == carll30:
                                vehicles[i] = carll60
                            elif vehicles[i] == busll30:
                                vehicles[i] = busll60
                            elif vehicles[i] == truckll30:
                                vehicles[i] = truckll60
                            elif vehicles[i] == bikell30:
                                vehicles[i] = bikell60
                        elif xpos[i] == 580:
                            if vehicles[i] == carll60:
                                vehicles[i] = carll90
                            elif vehicles[i] == busll60:
                                vehicles[i] = busll90
                            elif vehicles[i] == truckll60:
                                vehicles[i] = truckll90
                            elif vehicles[i] == bikell60:
                                vehicles[i] = bikell90
                        xpos[i] += 1
                        ypos[i] -= 2
                    else:
                        if xpos[i] > 580:
                            if ypos[i] <= 310:
                                turned[i] = 1
                            ypos[i] -= 1
                        else:
                            xpos[i] += 1
                else:
                    if xpos[i] >= 635 and xpos[i] <= 655:
                        pos1 = pygame.transform.rotate(vehicles[i], -30)
                        pos2 = pygame.transform.rotate(vehicles[i], -30)
                        pos3 = pygame.transform.rotate(vehicles[i], -30)
                        if xpos[i] == 635:
                            vehicles[i] = pos1
                        elif xpos[i] == 645:
                            vehicles[i] = pos2
                        elif xpos[i] == 655:
                            vehicles[i] = pos3
                        xpos[i] += 1
                    else:
                        if xpos[i] > 655:
                            if ypos[i] >= 500:
                                turned[i] = 1
                            ypos[i] += 1
                        else:
                            xpos[i] += 1
        elif dirs[i] == 'up':
            if signalu == 'red' or signalu == 'yellow':
                if ypos[i] > 301:
                    if turns[i] == 'l':
                        if ypos[i] >= 360 and ypos[i] <= 380:
                            if ypos[i] == 360:
                                if vehicles[i] == caru:
                                    vehicles[i] = carul30
                                elif vehicles[i] == busu:
                                    vehicles[i] = busul30
                                elif vehicles[i] == trucku:
                                    vehicles[i] = truckul30
                                elif vehicles[i] == bikeu:
                                    vehicles[i] = bikeul30
                            elif ypos[i] == 370:
                                if vehicles[i] == carul30:
                                    vehicles[i] = carul60
                                elif vehicles[i] == busul30:
                                    vehicles[i] = busul60
                                elif vehicles[i] == truckul30:
                                    vehicles[i] = truckul60
                                elif vehicles[i] == bikeul30:
                                    vehicles[i] = bikeul60
                            elif ypos[i] == 380:
                                if vehicles[i] == carul60:
                                    vehicles[i] = carul90
                                elif vehicles[i] == busul60:
                                    vehicles[i] = busul90
                                elif vehicles[i] == truckul60:
                                    vehicles[i] = truckul90
                                elif vehicles[i] == bikeul60:
                                    vehicles[i] = bikeul90
                            ypos[i] += 1
                            xpos[i] += 2
                        else:
                            if ypos[i] > 380:
                                if xpos[i] >= 765:
                                    turned[i] = 1
                                xpos[i] += 1
                            else:
                                ypos[i] += 1
                    elif turns[i] == 'r':
                        if ypos[i] >= 390 and ypos[i] <= 410:
                            if ypos[i] == 390:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], -30)
                            elif ypos[i] == 400:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], -30)
                            elif ypos[i] == 410:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], -30)
                            ypos[i] += 1
                        else:
                            if ypos[i] > 410:
                                if xpos[i] <= 520:
                                    turned[i] = 1
                                xpos[i] -= 1
                            else:
                                ypos[i] += 1
                    else:
                        ypos[i] += 1
                else:
                    if xpos[i] == 765:
                        k3 = 0
                        for m in range(vehiclecount):
                            if ypos[m] in range(240-100*k3, 300-100*k3) and m != i and xpos[m] == 765:
                                k3 += 1
                        if ypos[i] >= 240-100*k3 and ypos[i] <= 300:
                            ypos[i] = ypos[i]
                        else:
                            ypos[i] += 1
                    else:
                        k4 = 0
                        for e in range(vehiclecount):
                            if ypos[e] in range(240-100*k4, 300-100*k4) and e != i and xpos[e] == 700:
                                k4 += 1
                        if ypos[i] >= 240-100*k4 and ypos[i] <= 300:
                            ypos[i] = ypos[i]
                        else:
                            ypos[i] += 1
            else:
                if turns[i] == 'l':
                    if ypos[i] >= 360 and ypos[i] <= 380:
                        if ypos[i] == 360:
                            if vehicles[i] == caru:
                                vehicles[i] = carul30
                            elif vehicles[i] == busu:
                                vehicles[i] = busul30
                            elif vehicles[i] == trucku:
                                vehicles[i] = truckul30
                            elif vehicles[i] == bikeu:
                                vehicles[i] = bikeul30
                        elif ypos[i] == 370:
                            if vehicles[i] == carul30:
                                vehicles[i] = carul60
                            elif vehicles[i] == busul30:
                                vehicles[i] = busul60
                            elif vehicles[i] == truckul30:
                                vehicles[i] = truckul60
                            elif vehicles[i] == bikeul30:
                                vehicles[i] = bikeul60
                        elif ypos[i] == 380:
                            if vehicles[i] == carul60:
                                vehicles[i] = carul90
                            elif vehicles[i] == busul60:
                                vehicles[i] = busul90
                            elif vehicles[i] == truckul60:
                                vehicles[i] = truckul90
                            elif vehicles[i] == bikeul60:
                                vehicles[i] = bikeul90
                        ypos[i] += 1
                        xpos[i] += 2
                    else:
                        if ypos[i] > 380:
                            if xpos[i] >= 765:
                                turned[i] = 1
                            xpos[i] += 1
                        else:
                            ypos[i] += 1
                elif turns[i] == 'r':
                    if ypos[i] >= 390 and ypos[i] <= 410:
                        if ypos[i] == 390:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], -30)
                        elif ypos[i] == 400:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], -30)
                        elif ypos[i] == 410:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], -30)
                        ypos[i] += 1
                    else:
                        if ypos[i] > 410:
                            if xpos[i] <= 520:
                                turned[i] = 1
                            xpos[i] -= 1
                        else:
                            ypos[i] += 1
                else:
                    ypos[i] += 1
        elif dirs[i] == 'right':
            if signalr == 'red' or signalr == 'yellow':
                if xpos[i] < 799:
                    if turns[i] == 'r':
                        if xpos[i] <= 610 and xpos[i] >= 590:
                            if xpos[i] == 610:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], -30)
                            elif xpos[i] == 600:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], -30)
                            elif xpos[i] == 590:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], -30)
                            xpos[i] -= 1
                        else:
                            if xpos[i] < 590:
                                if ypos[i] <= 310:
                                    turned[i] = 1
                                ypos[i] -= 1
                            else:
                                xpos[i] -= 1
                    elif turns[i] == 'l':
                        if xpos[i] <= 740 and xpos[i] >= 720:
                            if xpos[i] == 740:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], 30)
                            elif xpos[i] == 730:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], 30)
                            elif xpos[i] == 720:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], 30)
                            xpos[i] -= 1
                        else:
                            if xpos[i] < 720:
                                if ypos[i] >= 500:
                                    turned[i] = 1
                                ypos[i] += 1
                            else:
                                xpos[i] -= 1
                    else:
                        xpos[i] -= 1
                else:
                    k2 = 0
                    for l in range(vehiclecount):
                        if xpos[l] in range(860+100*k2, 800+100*k2, -1) and l != i and ypos[l] == 445:
                            k2 += 1
                    if xpos[i] <= 860+100*k2 and xpos[i] >= 800:
                        xpos[i] = xpos[i]
                    else:
                        xpos[i] -= 1
            else:
                if turns[i] == 's':
                    xpos[i] -= 1
                elif turns[i] == 'r':
                    if xpos[i] <= 610 and xpos[i] >= 590:
                        if xpos[i] == 610:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], -30)
                        elif xpos[i] == 600:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], -30)
                        elif xpos[i] == 590:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], -30)
                        xpos[i] -= 1
                    else:
                        if xpos[i] < 590:
                            if ypos[i] <= 310:
                                turned[i] = 1
                            ypos[i] -= 1
                        else:
                            xpos[i] -= 1
                else:
                    if xpos[i] <= 740 and xpos[i] >= 720:
                        if xpos[i] == 740:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], 30)
                        elif xpos[i] == 730:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], 30)
                        elif xpos[i] == 720:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], 30)
                        xpos[i] -= 1
                    else:
                        if xpos[i] < 720:
                            if ypos[i] >= 500:
                                turned[i] = 1
                            ypos[i] += 1
                        else:
                            xpos[i] -= 1
        else:
            if signald == 'red' or signald == 'yellow':
                if ypos[i] < 519:
                    if turns[i] == 'l':
                        if ypos[i] <= 470 and ypos[i] >= 450:
                            if ypos[i] == 470:
                                if vehicles[i] == card:
                                    vehicles[i] = cardl30
                                elif vehicles[i] == busd:
                                    vehicles[i] = busdl30
                                elif vehicles[i] == truckd:
                                    vehicles[i] = truckdl30
                                elif vehicles[i] == biked:
                                    vehicles[i] = bikedl30
                            elif ypos[i] == 460:
                                if vehicles[i] == cardl30:
                                    vehicles[i] = cardl60
                                elif vehicles[i] == busdl30:
                                    vehicles[i] = busdl60
                                elif vehicles[i] == truckdl30:
                                    vehicles[i] = truckdl60
                                elif vehicles[i] == bikedl30:
                                    vehicles[i] = bikedl60
                            elif ypos[i] == 450:
                                if vehicles[i] == cardl60:
                                    vehicles[i] = cardl90
                                elif vehicles[i] == busdl60:
                                    vehicles[i] = busdl90
                                elif vehicles[i] == truckdl60:
                                    vehicles[i] = truckdl90
                                elif vehicles[i] == bikedl60:
                                    vehicles[i] = bikedl90
                            ypos[i] -= 1
                            xpos[i] -= 2
                        else:
                            if ypos[i] < 450:
                                if xpos[i] <= 520:
                                    turned[i] = 1
                                xpos[i] -= 1
                            else:
                                ypos[i] -= 1
                    elif turns[i] == 'r':
                        if ypos[i] <= 360 and ypos[i] >= 340:
                            if ypos[i] == 360:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], -30)
                            elif ypos[i] == 350:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], -30)
                            elif ypos[i] == 340:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], -30)
                            ypos[i] -= 1
                        else:
                            if ypos[i] < 340:
                                if xpos[i] >= 765:
                                    turned[i] = 1
                                xpos[i] += 1
                            else:
                                ypos[i] -= 1
                    else:
                        ypos[i] -= 1
                else:
                    if xpos[i] == 640:
                        k5 = 0
                        for p in range(vehiclecount):
                            if ypos[p] in range(580+100*k5, 520+100*k5, -1) and p != i and xpos[p] == 640:
                                k5 += 1
                        if ypos[i] <= 580+100*k5 and ypos[i] >= 520:
                            ypos[i] = ypos[i]
                        else:
                            ypos[i] -= 1
                    else:
                        k6 = 0
                        for q in range(vehiclecount):
                            if ypos[q] in range(580+100*k6, 520+100*k6, -1) and q != i and xpos[q] == 570:
                                k6 += 1
                        if ypos[i] <= 580+100*k6 and ypos[i] >= 520:
                            ypos[i] = ypos[i]
                        else:
                            ypos[i] -= 1
            else:
                if turns[i] == 'l':
                    if ypos[i] <= 470 and ypos[i] >= 450:
                        if ypos[i] == 470:
                            if vehicles[i] == card:
                                vehicles[i] = cardl30
                            elif vehicles[i] == busd:
                                vehicles[i] = busdl30
                            elif vehicles[i] == truckd:
                                vehicles[i] = truckdl30
                            elif vehicles[i] == biked:
                                vehicles[i] = bikedl30
                        elif ypos[i] == 460:
                            if vehicles[i] == cardl30:
                                vehicles[i] = cardl60
                            elif vehicles[i] == busdl30:
                                vehicles[i] = busdl60
                            elif vehicles[i] == truckdl30:
                                vehicles[i] = truckdl60
                            elif vehicles[i] == bikedl30:
                                vehicles[i] = bikedl60
                        elif ypos[i] == 450:
                            if vehicles[i] == cardl60:
                                vehicles[i] = cardl90
                            elif vehicles[i] == busdl60:
                                vehicles[i] = busdl90
                            elif vehicles[i] == truckdl60:
                                vehicles[i] = truckdl90
                            elif vehicles[i] == bikedl60:
                                vehicles[i] = bikedl90
                        ypos[i] -= 1
                        xpos[i] -= 2
                    else:
                        if ypos[i] < 450:
                            if xpos[i] <= 520:
                                turned[i] = 1
                            xpos[i] -= 1
                        else:
                            ypos[i] -= 1
                elif turns[i] == 'r':
                    if ypos[i] <= 360 and ypos[i] >= 340:
                        if ypos[i] == 360:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], -30)
                        elif ypos[i] == 350:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], -30)
                        elif ypos[i] == 340:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], -30)
                        ypos[i] -= 1
                    else:
                        if ypos[i] < 340:
                            if xpos[i] >= 765:
                                turned[i] = 1
                            xpos[i] += 1
                        else:
                            ypos[i] -= 1
                else:
                    ypos[i] -= 1
    if vehiclegen <= 0:
        v, x, y, dir, turn = VehicleGenerate()
        if dir == 'left':
            fo = 0
            for o in range(vehiclecount):
                if xpos[o] in range(10, 80) and ypos[o] == 385:
                    fo = 1
                    break
            if fo == 0:
                vehicles.append(v)
                xpos.append(x)
                ypos.append(y)
                dirs.append(dir)
                vehiclecount += 1
                vehiclegen = 2
                turns.append(turn)
                turned.append(0)
        elif dir == 'right':
            fu = 0
            for u in range(vehiclecount):
                if xpos[u] in range(1350, 1280, -1) and ypos[u] == 445:
                    fu = 1
                    break
            if fu == 0:
                vehicles.append(v)
                xpos.append(x)
                ypos.append(y)
                dirs.append(dir)
                vehiclecount += 1
                vehiclegen = 2
                turns.append(turn)
                turned.append(0)
        elif dir == 'up':
            ft = 0
            for t in range(vehiclecount):
                if ypos[t] in range(5, 75) and (xpos[t] == 765 or xpos[t] == 700):
                    ft = 1
                    break
            if ft == 0:
                vehicles.append(v)
                xpos.append(x)
                ypos.append(y)
                dirs.append(dir)
                vehiclecount += 1
                vehiclegen = 2
                turns.append(turn)
                turned.append(0)
        else:
            fw = 0
            for w in range(vehiclecount):
                if ypos[w] in range(762, 680, -1) and (xpos[w] == 570 or xpos[w] == 640):
                    fw = 1
                    break
            if fw == 0:
                vehicles.append(v)
                xpos.append(x)
                ypos.append(y)
                dirs.append(dir)
                vehiclecount += 1
                vehiclegen = 2
                turns.append(turn)
                turned.append(0)
    for i in range(vehiclecount):
        player(vehicles[i], xpos[i], ypos[i])
    clock.tick(60)

    pygame.display.update()
