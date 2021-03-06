from pygame import *
from pygame.locals import *
from math import *
import datetime

#----------------------------------------------------------------------

init()

screen = display.set_mode((800,600))
display.set_caption("Loading.....")

clock = time.Clock()

current=datetime.datetime.now()

hours = current.hour
if hours > 12:
    hours=hours-12
    
minutes = current.minute

seconds = current.second

running=True
while running:

    # events 

    for e in event.get():
        if e.type == QUIT:
            running = False

    # (variable) modifications

    seconds_ang = 270 + 6 * seconds

    seconds_dx = int(cos(radians(-seconds_ang))*200)
    seconds_dy = int(sin(radians(-seconds_ang))*200)

    minutes_ang = 270 + 6 * minutes

    minutes_dx = int(cos(radians(-minutes_ang))*200)
    minutes_dy = int(sin(radians(-minutes_ang))*200)

    hours_ang = 270 + 30 * hours

    hours_dx = int(cos(radians(-hours_ang))*150)
    hours_dy = int(sin(radians(-hours_ang))*150)

    seconds += 1

    if seconds == 60:
        seconds = 0
        minutes += 1

        if minutes == 60:
            minutes = 0
            hours += 1

            if hours == 12:
                hours = 0

    # draw

    screen.fill((0,0,0))
    draw.circle(screen, (255,255,255), (400,300), 200, 3)
    draw.line(screen,(0,255,255), (400,300), (400 + hours_dx, 300 - hours_dy), 5)
    draw.line(screen,(255,255,0), (400,300), (400 + minutes_dx, 300 - minutes_dy), 2)
    draw.line(screen,(255,0,255), (400,300), (400 + seconds_dx, 300 - seconds_dy), 1)

    display.set_caption(str(hours)+":"+str(minutes)+":"+str(seconds))

    # flip

    display.flip()

    # FPS (Frames Per Seconds)

    clock.tick(1)

quit()
