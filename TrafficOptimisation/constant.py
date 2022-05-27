import pygame
import random
import time
import timeit

# initialize pygame
pygame.init()
start = timeit.default_timer()
black = (0, 0, 0)
white = (255, 255, 255)
simtime = 0
font = pygame.font.Font(None, 30)
# create game screen
screen = pygame.display.set_mode((1400, 800))
background = pygame.image.load('images/intersection3.png')

# players
carl = pygame.image.load('images/left/car.png')
carll30 = pygame.image.load('images/left/carl30.png')
carll60 = pygame.image.load('images/left/carl60.png')
carll90 = pygame.image.load('images/left/carl90.png')
carlr30 = pygame.image.load('images/left/carr30.png')
carlr60 = pygame.image.load('images/left/carr60.png')
carlr90 = pygame.image.load('images/left/carr90.png')
carr = pygame.image.load('images/right/car.png')
carrl30 = pygame.image.load('images/right/carl30.png')
carrl60 = pygame.image.load('images/right/carl60.png')
carrl90 = pygame.image.load('images/right/carl90.png')
carrr30 = pygame.image.load('images/right/carr30.png')
carrr60 = pygame.image.load('images/right/carr60.png')
carrr90 = pygame.image.load('images/right/carr90.png')
caru = pygame.image.load('images/up/car.png')
carul30 = pygame.image.load('images/up/carl30.png')
carul60 = pygame.image.load('images/up/carl60.png')
carul90 = pygame.image.load('images/up/carl90.png')
carur30 = pygame.image.load('images/up/carr30.png')
carur60 = pygame.image.load('images/up/carr60.png')
carur90 = pygame.image.load('images/up/carr90.png')
card = pygame.image.load('images/down/car.png')
cardl30 = pygame.image.load('images/down/carl30.png')
cardl60 = pygame.image.load('images/down/carl60.png')
cardl90 = pygame.image.load('images/down/carl90.png')
cardr30 = pygame.image.load('images/down/carr30.png')
cardr60 = pygame.image.load('images/down/carr60.png')
cardr90 = pygame.image.load('images/down/carr90.png')
busl = pygame.image.load('images/left/bus.png')
busll30 = pygame.image.load('images/left/busl30.png')
busll60 = pygame.image.load('images/left/busl60.png')
busll90 = pygame.image.load('images/left/busl90.png')
buslr30 = pygame.image.load('images/left/busr30.png')
buslr60 = pygame.image.load('images/left/busr60.png')
buslr90 = pygame.image.load('images/left/busr90.png')
busr = pygame.image.load('images/right/bus.png')
busrl30 = pygame.image.load('images/right/busl30.png')
busrl60 = pygame.image.load('images/right/busl60.png')
busrl90 = pygame.image.load('images/right/busl90.png')
busrr30 = pygame.image.load('images/right/busr30.png')
busrr60 = pygame.image.load('images/right/busr60.png')
busrr90 = pygame.image.load('images/right/busr90.png')
busd = pygame.image.load('images/down/bus.png')
busdl30 = pygame.image.load('images/down/busl30.png')
busdl60 = pygame.image.load('images/down/busl60.png')
busdl90 = pygame.image.load('images/down/busl90.png')
busdr30 = pygame.image.load('images/down/busr30.png')
busdr60 = pygame.image.load('images/down/busr60.png')
busdr90 = pygame.image.load('images/down/busr90.png')
busu = pygame.image.load('images/up/bus.png')
busul30 = pygame.image.load('images/up/busl30.png')
busul60 = pygame.image.load('images/up/busl60.png')
busul90 = pygame.image.load('images/up/busl90.png')
busur30 = pygame.image.load('images/up/busr30.png')
busur60 = pygame.image.load('images/up/busr60.png')
busur90 = pygame.image.load('images/up/busr90.png')
truckl = pygame.image.load('images/left/truck.png')
truckll30 = pygame.image.load('images/left/truckl30.png')
truckll60 = pygame.image.load('images/left/truckl60.png')
truckll90 = pygame.image.load('images/left/truckl90.png')
trucklr30 = pygame.image.load('images/left/truckr30.png')
trucklr60 = pygame.image.load('images/left/truckr60.png')
trucklr90 = pygame.image.load('images/left/truckr90.png')
truckr = pygame.image.load('images/right/truck.png')
truckrl30 = pygame.image.load('images/right/truckl30.png')
truckrl60 = pygame.image.load('images/right/truckl60.png')
truckrl90 = pygame.image.load('images/right/truckl90.png')
truckrr30 = pygame.image.load('images/right/truckr30.png')
truckrr60 = pygame.image.load('images/right/truckr60.png')
truckrr90 = pygame.image.load('images/right/truckr90.png')
truckd = pygame.image.load('images/down/truck.png')
truckdl30 = pygame.image.load('images/down/truckl30.png')
truckdl60 = pygame.image.load('images/down/truckl60.png')
truckdl90 = pygame.image.load('images/down/truckl90.png')
truckdr30 = pygame.image.load('images/down/truckr30.png')
truckdr60 = pygame.image.load('images/down/truckr60.png')
truckdr90 = pygame.image.load('images/down/truckr90.png')
trucku = pygame.image.load('images/up/truck.png')
truckul30 = pygame.image.load('images/up/truckl30.png')
truckul60 = pygame.image.load('images/up/truckl60.png')
truckul90 = pygame.image.load('images/up/truckl90.png')
truckur30 = pygame.image.load('images/up/truckr30.png')
truckur60 = pygame.image.load('images/up/truckr60.png')
truckur90 = pygame.image.load('images/up/truckr90.png')
bikel = pygame.image.load('images/left/bike.png')
bikell30 = pygame.image.load('images/left/bikel30.png')
bikell60 = pygame.image.load('images/left/bikel60.png')
bikell90 = pygame.image.load('images/left/bikel90.png')
bikelr30 = pygame.image.load('images/left/biker30.png')
bikelr60 = pygame.image.load('images/left/biker60.png')
bikelr90 = pygame.image.load('images/left/biker90.png')
biker = pygame.image.load('images/right/bike.png')
bikerl30 = pygame.image.load('images/right/bikel30.png')
bikerl60 = pygame.image.load('images/right/bikel60.png')
bikerl90 = pygame.image.load('images/right/bikel90.png')
bikerr30 = pygame.image.load('images/right/biker30.png')
bikerr60 = pygame.image.load('images/right/biker60.png')
bikerr90 = pygame.image.load('images/right/biker90.png')
biked = pygame.image.load('images/down/bike.png')
bikedl30 = pygame.image.load('images/down/bikel30.png')
bikedl60 = pygame.image.load('images/down/bikel60.png')
bikedl90 = pygame.image.load('images/down/bikel90.png')
bikedr30 = pygame.image.load('images/down/biker30.png')
bikedr60 = pygame.image.load('images/down/biker60.png')
bikedr90 = pygame.image.load('images/down/biker90.png')
bikeu = pygame.image.load('images/up/bike.png')
bikeul30 = pygame.image.load('images/up/bikel30.png')
bikeul60 = pygame.image.load('images/up/bikel60.png')
bikeul90 = pygame.image.load('images/up/bikel90.png')
bikeur30 = pygame.image.load('images/up/biker30.png')
bikeur60 = pygame.image.load('images/up/biker60.png')
bikeur90 = pygame.image.load('images/up/biker90.png')
green = pygame.image.load('images/signals/green.png')
green2 = pygame.image.load('images/signals/green2.png')
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
    num1 = random.randint(0, 1001)
    ger = [150, 500, 650, 1000]
    if (num1 < ger[0]):
        dir = 'left'
    elif (num1 > ger[0] and num1 < ger[1]):
        dir = 'up'
    elif (num1 > ger[1] and num1 < ger[2]):
        dir = 'right'
    elif (num1 > ger[2] and num1 < ger[3]):
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
turned2 = []
ql = []
vehiclegen = 2
sg = 'lr'
sg2 = 'l'
a = 0
fl = 1
fu = 1
fr = 1
fd = 1
temp = 0
vehiclecount = 0
vehiclel = []
vehiclelcount = 0
vehiclercount = 0
vehicleucount = 0
vehicledcount = 0
vehicleLeft = 0
vehicleRight = 0
vehicleUp = 0
vehicleDown = 0
max = 30
rmax = 4
counter = max
counter2 = 2
counter3 = rmax
counter4 = rmax
c1 = 0
c2 = 0
while running:
    simtime += 0.01749
    flag = 0
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT:
            vehiclegen -= 1
            counter -= 1
            counter2 -= 1
            counter3 -= 1
        if event.type == pygame.QUIT:
            vehiclePassed = vehicleDown + vehicleRight + vehicleUp + vehicleLeft
            stop = timeit.default_timer()
            timeRun = stop - start
            timeRun = int(timeRun)
            print('Simulation time:', timeRun, "seconds")
            print('Total no of vehicles passed:', vehiclePassed)
            print('left-', vehiclelcount)
            print('down-', vehicledcount)
            print('right-', vehiclercount)
            print('up-', vehicleucount)
            running = False
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    simtimeText = font.render(
        ("Simulation Time: " + str(simtime)), True, black, white)
    screen.blit(simtimeText, (1160, 40))
    if counter < 0:
        if sg == 'lr':
            sg = 'ud'
            fl = 0
            if vehicledcount > vehicleucount:
                sg2 = 'd'
            else:
                sg2 = 'u'
            counter = max
            counter3 = rmax
            counter4 = rmax
        elif sg == 'ud':
            sg = 'lr'
            fd = 0
            if vehiclelcount > vehiclercount:
                sg2 = 'l'
            else:
                sg2 = 'r'
            counter = max
            counter3 = rmax
            counter4 = rmax
    if counter >= 0 or flag == 1:
        if sg == 'lr':
            if fd == 0:
                counter2 = 2
                fd = 1
            if counter2 >= 0:
                signald = 'yellow'
                signalu = 'yellow'
            else:
                signald = 'red'
                signalu = 'red'
            if signald == 'yellow' or signalu == 'yellow':
                screen.blit(yellow, (500, 525))
                screen.blit(yellow, (825, 250))
            else:
                screen.blit(red, (500, 525))
                screen.blit(red, (825, 250))
            fdb = 0
            for m in range(vehiclecount):
                if (ypos[m] in range(490, 310, -1) and dirs[m] == 'down' and turns[m] == 's') or (ypos[m] in range(310, 500) and dirs[m] == 'up' and turns[m] == 's') or (ypos[m] <= 490 and turned[m] == 0 and dirs[m] == 'down' and turns[m] == 'r') or (ypos[m] >= 310 and turned[m] == 0 and dirs[m] == 'up' and turns[m] == 'l') or (ypos[m] <= 490 and turned[m] == 0 and dirs[m] == 'down' and turns[m] == 'l') or (ypos[m] >= 310 and turned[m] == 0 and dirs[m] == 'up' and turns[m] == 'r'):
                    fdb = 1
                    break
            if fdb == 1:
                signall = 'red'
                signalr = 'red'
                screen.blit(red, (825, 525))
                screen.blit(red, (500, 250))
            else:
                if sg2 == 'l':
                    if counter3 > 0:
                        signall = 'green'
                        screen.blit(green, (500, 250))
                        signalr = 'red'
                        screen.blit(red, (825, 525))
                    if counter3 <= 0:
                        if counter <= counter4:
                            signalr = 'green'
                            screen.blit(green, (825, 525))
                            signall = 'red'
                            screen.blit(red, (500, 250))
                        else:
                            signall = 'green2'
                            screen.blit(green2, (500, 250))
                            signalr = 'green2'
                            screen.blit(green2, (825, 525))
                else:
                    if counter3 > 0:
                        signalr = 'green'
                        screen.blit(green, (825, 525))
                        signall = 'red'
                        screen.blit(red, (500, 250))
                    if counter3 <= 0:
                        if counter <= counter4:
                            signall = 'green'
                            screen.blit(green, (500, 250))
                            signalr = 'red'
                            screen.blit(red, (825, 525))
                        else:
                            frb = 0
                            for w in range(vehiclecount):
                                if (xpos[w] <= 780 and turned[w] == 0 and dirs[w] == 'right' and turns[w] == 'r'):
                                    frb = 1
                                    break
                            if frb == 0:
                                signalr = 'green2'
                                screen.blit(green2, (825, 525))
                                signall = 'green2'
                                screen.blit(green2, (500, 250))
                            else:
                                signalr = 'green'
                                screen.blit(green, (825, 525))
                                signall = 'red'
                                screen.blit(red, (500, 250))
        elif sg == 'ud':
            if fl == 0:
                counter2 = 2
                fl = 1
            if counter2 >= 0:
                signall = 'yellow'
                signalr = 'yellow'
            else:
                signall = 'red'
                signalr = 'red'
            if signall == 'yellow':
                screen.blit(yellow, (500, 250))
                screen.blit(yellow, (825, 525))
            else:
                screen.blit(red, (500, 250))
                screen.blit(red, (825, 525))
            flb = 0
            for w in range(vehiclecount):
                if (xpos[w] in range(495, 765) and dirs[w] == 'left' and turns[w] == 's') or (xpos[w] in range(780, 520, -1) and dirs[w] == 'right' and turns[w] == 's') or (xpos[w] >= 495 and turned[w] == 0 and dirs[w] == 'left' and turns[w] == 'l') or (xpos[w] <= 780 and turned[w] == 0 and dirs[w] == 'right' and turns[w] == 'l') or (xpos[w] >= 495 and turned[w] == 0 and dirs[w] == 'left' and turns[w] == 'r') or (xpos[w] <= 780 and turned[w] == 0 and dirs[w] == 'right' and turns[w] == 'r'):
                    flb = 1
                    break
            if flb == 1:
                signalu = 'red'
                signald = 'red'
                screen.blit(red, (500, 525))
                screen.blit(red, (825, 250))
            else:
                if sg2 == 'u':
                    if counter3 > 0:
                        signalu = 'green'
                        screen.blit(green, (825, 250))
                        signald = 'red'
                        screen.blit(red, (500, 525))
                    if counter3 <= 0:
                        if counter <= counter4:
                            signald = 'green'
                            screen.blit(green, (500, 525))
                            signalu = 'red'
                            screen.blit(red, (825, 250))
                        else:
                            signalu = 'green2'
                            screen.blit(green2, (825, 250))
                            signald = 'green2'
                            screen.blit(green2, (500, 525))
                else:
                    if counter3 > 0:
                        signald = 'green'
                        screen.blit(green, (500, 525))
                        signalu = 'red'
                        screen.blit(red, (825, 250))
                    if counter3 <= 0:
                        if counter <= counter4:
                            signalu = 'green'
                            screen.blit(green, (825, 250))
                            signald = 'red'
                            screen.blit(red, (500, 525))
                        else:
                            signald = 'green2'
                            screen.blit(green2, (500, 525))
                            signalu = 'green2'
                            screen.blit(green2, (825, 250))

    v = ''
    x = 0
    y = 0
    dir = ''
    for i in range(vehiclecount):
        if dirs[i] == 'left':
            if signall == 'green2' and turns[i] == 'r' and xpos[i] > 530 and turned2[i] == 0:
                turns[i] = 's'
            if(xpos[i] == 495):
                vehicleLeft += 1
            if xpos[i] == 11:
                vehiclelcount += 1
            if xpos[i] == 530:
                vehiclelcount -= 1
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
                                turned2[i] = 1
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
                        if xpos[i] >= 675 and xpos[i] <= 695:
                            if xpos[i] == 675:
                                if vehicles[i] == carl:
                                    vehicles[i] = carlr30
                                elif vehicles[i] == busl:
                                    vehicles[i] = buslr30
                                elif vehicles[i] == bikel:
                                    vehicles[i] = bikelr30
                                elif vehicles[i] == truckl:
                                    vehicles[i] = trucklr30
                                turned2[i] = 1
                            elif xpos[i] == 685:
                                if vehicles[i] == carlr30:
                                    vehicles[i] = carlr60
                                elif vehicles[i] == buslr30:
                                    vehicles[i] = buslr60
                                elif vehicles[i] == bikelr30:
                                    vehicles[i] = bikelr60
                                elif vehicles[i] == trucklr30:
                                    vehicles[i] = trucklr60
                            elif xpos[i] == 695:
                                if vehicles[i] == carlr60:
                                    vehicles[i] = carlr90
                                elif vehicles[i] == buslr60:
                                    vehicles[i] = buslr90
                                elif vehicles[i] == bikelr60:
                                    vehicles[i] = bikelr90
                                elif vehicles[i] == trucklr60:
                                    vehicles[i] = trucklr90
                            xpos[i] += 1
                            ypos[i] += 2
                        else:
                            if xpos[i] > 695:
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
                            turned2[i] = 1
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
                    if xpos[i] >= 675 and xpos[i] <= 695:
                        if xpos[i] == 675:
                            if vehicles[i] == carl:
                                vehicles[i] = carlr30
                            elif vehicles[i] == busl:
                                vehicles[i] = buslr30
                            elif vehicles[i] == bikel:
                                vehicles[i] = bikelr30
                            elif vehicles[i] == truckl:
                                vehicles[i] = trucklr30
                            turned2[i] = 1
                        elif xpos[i] == 685:
                            if vehicles[i] == carlr30:
                                vehicles[i] = carlr60
                            elif vehicles[i] == buslr30:
                                vehicles[i] = buslr60
                            elif vehicles[i] == bikelr30:
                                vehicles[i] = bikelr60
                            elif vehicles[i] == trucklr30:
                                vehicles[i] = trucklr60
                        elif xpos[i] == 695:
                            if vehicles[i] == carlr60:
                                vehicles[i] = carlr90
                            elif vehicles[i] == buslr60:
                                vehicles[i] = buslr90
                            elif vehicles[i] == bikelr60:
                                vehicles[i] = bikelr90
                            elif vehicles[i] == trucklr60:
                                vehicles[i] = trucklr90
                        xpos[i] += 1
                        ypos[i] += 2
                    else:
                        if xpos[i] > 695:
                            if ypos[i] >= 500:
                                turned[i] = 1
                            ypos[i] += 1
                        else:
                            xpos[i] += 1
        elif dirs[i] == 'up':
            if signalu == 'green2' and turns[i] == 'r' and ypos[i] > 320 and turned2[i] == 0:
                turns[i] = 's'
            if(ypos[i] == 299):
                vehicleUp += 1
            if ypos[i] == 6:
                vehicleucount += 1
            if ypos[i] == 320:
                vehicleucount -= 1
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
                                turned2[i] = 1
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
                        if ypos[i] >= 430 and ypos[i] <= 450:
                            if ypos[i] == 430:
                                if vehicles[i] == caru:
                                    vehicles[i] = carur30
                                elif vehicles[i] == busu:
                                    vehicles[i] = busur30
                                elif vehicles[i] == trucku:
                                    vehicles[i] = truckur30
                                elif vehicles[i] == bikeu:
                                    vehicles[i] = bikeur30
                                turned2[i] = 1
                            elif ypos[i] == 440:
                                if vehicles[i] == carur30:
                                    vehicles[i] = carur60
                                elif vehicles[i] == busur30:
                                    vehicles[i] = busur60
                                elif vehicles[i] == truckur30:
                                    vehicles[i] = truckur60
                                elif vehicles[i] == bikeur30:
                                    vehicles[i] = bikeur60
                            elif ypos[i] == 450:
                                if vehicles[i] == carur60:
                                    vehicles[i] = carur90
                                elif vehicles[i] == busur60:
                                    vehicles[i] = busur90
                                elif vehicles[i] == truckur60:
                                    vehicles[i] = truckur90
                                elif vehicles[i] == bikeur60:
                                    vehicles[i] = bikeur90
                            ypos[i] += 1
                            xpos[i] -= 2
                        else:
                            if ypos[i] > 450:
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
                            turned2[i] = 1
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
                    if ypos[i] >= 430 and ypos[i] <= 450:
                        if ypos[i] == 430:
                            if vehicles[i] == caru:
                                vehicles[i] = carur30
                            elif vehicles[i] == busu:
                                vehicles[i] = busur30
                            elif vehicles[i] == trucku:
                                vehicles[i] = truckur30
                            elif vehicles[i] == bikeu:
                                vehicles[i] = bikeur30
                            turned2[i] = 1
                        elif ypos[i] == 440:
                            if vehicles[i] == carur30:
                                vehicles[i] = carur60
                            elif vehicles[i] == busur30:
                                vehicles[i] = busur60
                            elif vehicles[i] == truckur30:
                                vehicles[i] = truckur60
                            elif vehicles[i] == bikeur30:
                                vehicles[i] = bikeur60
                        elif ypos[i] == 450:
                            if vehicles[i] == carur60:
                                vehicles[i] = carur90
                            elif vehicles[i] == busur60:
                                vehicles[i] = busur90
                            elif vehicles[i] == truckur60:
                                vehicles[i] = truckur90
                            elif vehicles[i] == bikeur60:
                                vehicles[i] = bikeur90
                        ypos[i] += 1
                        xpos[i] -= 2
                    else:
                        if ypos[i] > 450:
                            if xpos[i] <= 520:
                                turned[i] = 1
                            xpos[i] -= 1
                        else:
                            ypos[i] += 1
                else:
                    ypos[i] += 1
        elif dirs[i] == 'right':
            if signalr == 'green2' and turns[i] == 'r' and xpos[i] < 765 and turned2[i] == 0:
                turns[i] = 's'
            if(xpos[i] == 797):
                vehicleRight += 1
            if xpos[i] == 1349:
                vehiclercount += 1
            if xpos[i] == 765:
                vehiclercount -= 1
            if signalr == 'red' or signalr == 'yellow':
                if xpos[i] < 799:
                    if turns[i] == 'r':
                        if xpos[i] <= 660 and xpos[i] >= 640:
                            if xpos[i] == 660:
                                turned2[i] = 1
                                if vehicles[i] == carr:
                                    vehicles[i] = carrr30
                                elif vehicles[i] == busr:
                                    vehicles[i] = busrr30
                                elif vehicles[i] == truckr:
                                    vehicles[i] = truckrr30
                                elif vehicles[i] == biker:
                                    vehicles[i] = bikerr30
                            elif xpos[i] == 650:
                                if vehicles[i] == carrr30:
                                    vehicles[i] = carrr60
                                elif vehicles[i] == busrr30:
                                    vehicles[i] = busrr60
                                elif vehicles[i] == truckrr30:
                                    vehicles[i] = truckrr60
                                elif vehicles[i] == bikerr30:
                                    vehicles[i] = bikerr60
                            elif xpos[i] == 640:
                                if vehicles[i] == carrr60:
                                    vehicles[i] = carrr90
                                elif vehicles[i] == busrr60:
                                    vehicles[i] = busrr90
                                elif vehicles[i] == truckrr60:
                                    vehicles[i] = truckrr90
                                elif vehicles[i] == bikerr60:
                                    vehicles[i] = bikerr90
                            xpos[i] -= 1
                            ypos[i] -= 2
                        else:
                            if xpos[i] < 640:
                                if ypos[i] <= 310:
                                    turned[i] = 1
                                ypos[i] -= 1
                            else:
                                xpos[i] -= 1
                    elif turns[i] == 'l':
                        if xpos[i] <= 780 and xpos[i] >= 760:
                            if xpos[i] == 780:
                                turned2[i] = 1
                                if vehicles[i] == carr:
                                    vehicles[i] = carrl30
                                elif vehicles[i] == busr:
                                    vehicles[i] = busrl30
                                elif vehicles[i] == biker:
                                    vehicles[i] = bikerl30
                                elif vehicles[i] == truckr:
                                    vehicles[i] = truckrl30
                            elif xpos[i] == 770:
                                if vehicles[i] == carrl30:
                                    vehicles[i] = carrl60
                                elif vehicles[i] == busrl30:
                                    vehicles[i] = busrl60
                                elif vehicles[i] == bikerl30:
                                    vehicles[i] = bikerl60
                                elif vehicles[i] == truckrl30:
                                    vehicles[i] = truckrl60
                            elif xpos[i] == 760:
                                if vehicles[i] == carrl60:
                                    vehicles[i] = carrl90
                                elif vehicles[i] == busrl60:
                                    vehicles[i] = busrl90
                                elif vehicles[i] == bikerl60:
                                    vehicles[i] = bikerl90
                                elif vehicles[i] == truckrl60:
                                    vehicles[i] = truckrl90
                            xpos[i] -= 1
                            ypos[i] += 2
                        else:
                            if xpos[i] < 760:
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
                    if xpos[i] <= 660 and xpos[i] >= 640:
                        if xpos[i] == 660:
                            turned2[i] = 1
                            if vehicles[i] == carr:
                                vehicles[i] = carrr30
                            elif vehicles[i] == busr:
                                vehicles[i] = busrr30
                            elif vehicles[i] == truckr:
                                vehicles[i] = truckrr30
                            elif vehicles[i] == biker:
                                vehicles[i] = bikerr30
                        elif xpos[i] == 650:
                            if vehicles[i] == carrr30:
                                vehicles[i] = carrr60
                            elif vehicles[i] == busrr30:
                                vehicles[i] = busrr60
                            elif vehicles[i] == truckrr30:
                                vehicles[i] = truckrr60
                            elif vehicles[i] == bikerr30:
                                vehicles[i] = bikerr60
                        elif xpos[i] == 640:
                            if vehicles[i] == carrr60:
                                vehicles[i] = carrr90
                            elif vehicles[i] == busrr60:
                                vehicles[i] = busrr90
                            elif vehicles[i] == truckrr60:
                                vehicles[i] = truckrr90
                            elif vehicles[i] == bikerr60:
                                vehicles[i] = bikerr90
                        xpos[i] -= 1
                        ypos[i] -= 2
                    else:
                        if xpos[i] < 640:
                            if ypos[i] <= 310:
                                turned[i] = 1
                            ypos[i] -= 1
                        else:
                            xpos[i] -= 1
                else:
                    if xpos[i] <= 780 and xpos[i] >= 760:
                        if xpos[i] == 780:
                            turned2[i] = 1
                            if vehicles[i] == carr:
                                vehicles[i] = carrl30
                            elif vehicles[i] == busr:
                                vehicles[i] = busrl30
                            elif vehicles[i] == biker:
                                vehicles[i] = bikerl30
                            elif vehicles[i] == truckr:
                                vehicles[i] = truckrl30
                        elif xpos[i] == 770:
                            if vehicles[i] == carrl30:
                                vehicles[i] = carrl60
                            elif vehicles[i] == busrl30:
                                vehicles[i] = busrl60
                            elif vehicles[i] == bikerl30:
                                vehicles[i] = bikerl60
                            elif vehicles[i] == truckrl30:
                                vehicles[i] = truckrl60
                        elif xpos[i] == 760:
                            if vehicles[i] == carrl60:
                                vehicles[i] = carrl90
                            elif vehicles[i] == busrl60:
                                vehicles[i] = busrl90
                            elif vehicles[i] == bikerl60:
                                vehicles[i] = bikerl90
                            elif vehicles[i] == truckrl60:
                                vehicles[i] = truckrl90
                        xpos[i] -= 1
                        ypos[i] += 2
                    else:
                        if xpos[i] < 760:
                            if ypos[i] >= 500:
                                turned[i] = 1
                            ypos[i] += 1
                        else:
                            xpos[i] -= 1
        else:
            if signald == 'green2' and turns[i] == 'r' and ypos[i] < 490 and turned2[i] == 0:
                turns[i] = 's'
            if(ypos[i] == 517):
                vehicleDown += 1
            if ypos[i] == 759:
                vehicledcount += 1
            if ypos[i] == 490:
                vehicledcount -= 1
            if signald == 'red' or signald == 'yellow':
                if ypos[i] < 519:
                    if turns[i] == 'l':
                        if ypos[i] <= 470 and ypos[i] >= 450:
                            if ypos[i] == 470:
                                turned2[i] = 1
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
                        if ypos[i] <= 400 and ypos[i] >= 380:
                            if ypos[i] == 400:
                                turned2[i] = 1
                                if vehicles[i] == card:
                                    vehicles[i] = cardr30
                                elif vehicles[i] == busd:
                                    vehicles[i] = busdr30
                                elif vehicles[i] == truckd:
                                    vehicles[i] = truckdr30
                                elif vehicles[i] == biked:
                                    vehicles[i] = bikedr30
                            elif ypos[i] == 390:
                                if vehicles[i] == cardr30:
                                    vehicles[i] = cardr60
                                elif vehicles[i] == busdr30:
                                    vehicles[i] = busdr60
                                elif vehicles[i] == truckdr30:
                                    vehicles[i] = truckdr60
                                elif vehicles[i] == bikedr30:
                                    vehicles[i] = bikedr60
                            elif ypos[i] == 380:
                                if vehicles[i] == cardr60:
                                    vehicles[i] = cardr90
                                elif vehicles[i] == busdr60:
                                    vehicles[i] = busdr90
                                elif vehicles[i] == truckdr60:
                                    vehicles[i] = truckdr90
                                elif vehicles[i] == bikedr60:
                                    vehicles[i] = bikedr90
                            ypos[i] -= 1
                            xpos[i] += 2
                        else:
                            if ypos[i] < 380:
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
                            turned2[i] = 1
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
                    if ypos[i] <= 400 and ypos[i] >= 380:
                        if ypos[i] == 400:
                            turned2[i] = 1
                            if vehicles[i] == card:
                                vehicles[i] = cardr30
                            elif vehicles[i] == busd:
                                vehicles[i] = busdr30
                            elif vehicles[i] == truckd:
                                vehicles[i] = truckdr30
                            elif vehicles[i] == biked:
                                vehicles[i] = bikedr30
                        elif ypos[i] == 390:
                            if vehicles[i] == cardr30:
                                vehicles[i] = cardr60
                            elif vehicles[i] == busdr30:
                                vehicles[i] = busdr60
                            elif vehicles[i] == truckdr30:
                                vehicles[i] = truckdr60
                            elif vehicles[i] == bikedr30:
                                vehicles[i] = bikedr60
                        elif ypos[i] == 380:
                            if vehicles[i] == cardr60:
                                vehicles[i] = cardr90
                            elif vehicles[i] == busdr60:
                                vehicles[i] = busdr90
                            elif vehicles[i] == truckdr60:
                                vehicles[i] = truckdr90
                            elif vehicles[i] == bikedr60:
                                vehicles[i] = bikedr90
                        ypos[i] -= 1
                        xpos[i] += 2
                    else:
                        if ypos[i] < 380:
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
                turned2.append(0)
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
                turned2.append(0)
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
                turned2.append(0)
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
                turned2.append(0)
    for i in range(vehiclecount):
        player(vehicles[i], xpos[i], ypos[i])
    clock.tick(60)

    pygame.display.update()
