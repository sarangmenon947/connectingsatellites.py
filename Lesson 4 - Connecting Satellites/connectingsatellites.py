import pgzrun
import random

WIDTH = 800
HEIGHT = 600

satellites = []
numberofsatellites = 8

def createsatellites():
    for i in range(0, numberofsatellites):
        actorsatellite = Actor("satellite")
        actorsatellite.pos = random.randint(40, WIDTH-40), random.randint(40, HEIGHT-40)
        satellites.append(actorsatellite)

def draw():
    global actorsatellite
    screen.blit("space",(0,0))
    number = 1
    for i in satellites:
        screen.draw.text(str(number), (i.pos[0], i.pos[1]+20))
        i.draw()
        number = number + 1





createsatellites()
pgzrun.go()
        