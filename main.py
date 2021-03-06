import pygame
import os
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
switch = ui.Switch(10, 90, 30, 20, 'switch')
timer_label = ui.Label(1500, 10)
slider = ui.Slider(10, 140, 150, 10)
slider_value = ui.Label(170, 140, '0')
graph = ui.Texture(10, 190, pygame.image.load('graph.png'))
input = ui.LineEdit(10, 160, 100, 20)

#ARRAYS
container.components = [label, button2, switch, slider, slider_value, input, graph]
ui_arr = [timer_label, button, container]

while True:  #main loop
    screen.fill(white)

    start = tm.time()

    slider_value.text = str(round(slider.value, 3))

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
