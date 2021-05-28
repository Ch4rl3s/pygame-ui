import pygame
import sys
import math
import time as tm
import classes as ui

mainClock = pygame.time.Clock()

screen_size = [1600,900]

black = (0, 0, 0, 255)
white = (255, 255, 255)
yellow = (255, 255, 0, 255)
blue = (0,0,255,255)
green = (0, 255 , 0)
red = (255 , 0, 0)
grey = (10,10,10,255)

pygame.init()

myfont = pygame.font.SysFont('timesnewroman',  12)

pygame.display.set_caption('pygame UI')
screen = pygame.display.set_mode((screen_size[0], screen_size[1]))
screen.fill(white)

#STATES
mouse_down = False

#OBJECTS
container = ui.UniversalContainer(600, 100, 200, 300)
label = ui.Label(10, 10, 'label')
button = ui.Button(10, 30, 30, 20)
button2 = ui.Button(10, 60, 30, 20, 'press me')
switch = ui.Switch(10, 90, 30, 20)
timer_label = ui.Label(1500, 10)

#ARRAYS
container.components = [label, button2, switch]
ui_arr = [timer_label, button, container]

while True:  #main loop
    screen.fill(white)

    start = tm.time()

    end = tm.time()
    timer_label.text = f"{round((end - start), 5)}"

    for element in ui_arr:
        element.render(screen, black, myfont)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        for element in ui_arr:
            element.check_input(event)

    pygame.display.update()
    mainClock.tick(360)
