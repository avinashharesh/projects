import pygame
import random
import time


# initialize pygame
pygame.init()

# create game screen
screen = pygame.display.set_mode((1400, 800))
background = pygame.image.load('images/intersection2.png')

# player
car = pygame.image.load('images/down/car.png')
bus = pygame.image.load('images/down/bus.png')
bike = pygame.image.load('images/down/bike.png')
truck = pygame.image.load('images/down/truck.png')
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
            vehicle = pygame.image.load('images/left/car.png')
        elif num2 == 1:
            vehicle = pygame.image.load('images/left/bike.png')
        elif num2 == 2:
            vehicle = pygame.image.load('images/left/bus.png')
        else:
            vehicle = pygame.image.load('images/left/truck.png')
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
            y = 5
            num4 = random.randint(0, 2)
            if num4 == 0:
                turn = 'l'
            else:
                turn = 's'
        else:
            x = 700
            y = 5
            num4 = random.randint(0, 2)
            if num4 == 0:
                turn = 'r'
            else:
                turn = 's'
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
            y = 750
            num4 = random.randint(0, 3)
            if num4 == 0:
                turn = 'l'
            else:
                turn = 's'
        else:
            x = 640
            y = 750
            num4 = random.randint(0, 3)
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
hell = 570
hev = 750
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
    # screen.blit(car, (570, 520))
    # screen.blit(bus,(565-70*2,385))
    # screen.blit(bike, (495, 385))
    # screen.blit(car, (1350, 445))
    # screen.blit(car, (1280, 445))
    # screen.blit(car,(835,445))
    # screen.blit(car,(935,445))
    # screen.blit(car, (765, 250))
    # screen.blit(car, (765, 300))
    # screen.blit(bike, (hell, hev))
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
                if ypos[m] in range(490, 310, -1) and dirs[m] == 'down' and turns[m] == 's':
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
                if xpos[w] in range(495, 765) and dirs[w] == 'left' and turns[w] == 's':
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
                if ypos[y] in range(310, 500) and dirs[y] == 'up' and turns[y] == 's':
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
                if xpos[z] in range(780, 520, -1) and dirs[z] == 'right' and turns[z] == 's':
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
                        if xpos[i] >= 570 and xpos[i] <= 590:
                            if xpos[i] == 570:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], 30)
                            elif xpos[i] == 580:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], 30)
                            elif xpos[i] == 590:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], 30)
                            xpos[i] += 1
                        else:
                            if xpos[i] > 590:
                                ypos[i] -= 1
                            else:
                                xpos[i] += 1
                    elif turns[i] == 'r':
                        if xpos[i] >= 645 and xpos[i] <= 665:
                            if xpos[i] == 645:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], -30)
                            elif xpos[i] == 655:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], -30)
                            elif xpos[i] == 665:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], -30)
                        else:
                            if xpos[i] > 665:
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
                    if xpos[i] >= 570 and xpos[i] <= 590:
                        if xpos[i] == 570:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], 30)
                        elif xpos[i] == 580:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], 30)
                        elif xpos[i] == 590:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], 30)
                        xpos[i] += 1
                    else:
                        if xpos[i] > 590:
                            ypos[i] -= 1
                        else:
                            xpos[i] += 1
                else:
                    if xpos[i] >= 645 and xpos[i] <= 665:
                        if xpos[i] == 645:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], -30)
                        elif xpos[i] == 655:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], -30)
                        elif xpos[i] == 665:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], -30)
                        xpos[i] += 1
                    else:
                        if xpos[i] > 665:
                            ypos[i] += 1
                        else:
                            xpos[i] += 1
        elif dirs[i] == 'up':
            if signalu == 'red' or signalu == 'yellow':
                if ypos[i] > 301:
                    if turns[i] == 'l':
                        if ypos[i] >= 320 and ypos[i] <= 340:
                            if ypos[i] == 320:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], 30)
                            elif ypos[i] == 330:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], 30)
                            elif ypos[i] == 340:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], 30)
                            ypos[i] += 1
                        else:
                            if ypos[i] > 340:
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
                    if ypos[i] >= 320 and ypos[i] <= 340:
                        if ypos[i] == 320:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], 30)
                        elif ypos[i] == 330:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], 30)
                        elif ypos[i] == 340:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], 30)
                        ypos[i] += 1
                    else:
                        if ypos[i] > 340:
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
                            ypos[i] += 1
                        else:
                            xpos[i] -= 1
        else:
            if signald == 'red' or signald == 'yellow':
                if ypos[i] < 519:
                    if turns[i] == 'l':
                        if ypos[i] <= 430 and ypos[i] >= 410:
                            if ypos[i] == 430:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], 30)
                            elif ypos[i] == 420:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], 30)
                            elif ypos[i] == 410:
                                vehicles[i] = pygame.transform.rotate(
                                    vehicles[i], 30)
                            ypos[i] -= 1
                        else:
                            if ypos[i] < 410:
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
                    if ypos[i] <= 430 and ypos[i] >= 410:
                        if ypos[i] == 430:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], 30)
                        elif ypos[i] == 420:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], 30)
                        elif ypos[i] == 410:
                            vehicles[i] = pygame.transform.rotate(
                                vehicles[i], 30)
                        ypos[i] -= 1
                    else:
                        if ypos[i] < 410:
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
        else:
            fw = 0
            for w in range(vehiclecount):
                if ypos[w] in range(750, 680, -1) and (xpos[w] == 570 or xpos[w] == 640):
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
    for i in range(vehiclecount):
        player(vehicles[i], xpos[i], ypos[i])
    clock.tick(60)

    pygame.display.update()
