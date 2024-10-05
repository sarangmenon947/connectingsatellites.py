import pgzrun
import random
from time import time

WIDTH = 800
HEIGHT = 600

satellites = []
numberofsatellites = 8
nextsatellite = 0
lines = []
start_time = 0
end_time = 0
total_time = 0

def createsatellites():
    global start_time
    for i in range(0, numberofsatellites):
        actorsatellite = Actor("satellite")
        actorsatellite.pos = random.randint(40, WIDTH-40), random.randint(40, HEIGHT-40)
        satellites.append(actorsatellite)

    start_time = time()

def draw():
    global actorsatellite, total_time
    screen.blit("space",(0,0))
    number = 1
    for i in satellites:
        screen.draw.text(str(number), (i.pos[0], i.pos[1]+20))
        i.draw()
        number = number + 1
    
    for i in lines:
        screen.draw.line(i[0], i[1], "white")
    
    if nextsatellite < numberofsatellites:
        total_time = time() - start_time
        screen.draw.text(str (round(total_time, 1)), (20,20), fontsize = 40)
    else:
        screen.draw.text(str (round(total_time, 1)), (20,20), fontsize = 40)

def update():
    pass

def on_mouse_down(pos):
    global nextsatellite, lines
    if nextsatellite < numberofsatellites:
        if satellites [nextsatellite].collidepoint(pos):
            if nextsatellite:
                lines.append((satellites[nextsatellite - 1].pos, satellites[nextsatellite].pos))
            nextsatellite = nextsatellite + 1
        else: 
            lines = []
            nextsatellite = 0

createsatellites()
pgzrun.go()
        
