import pygame
import math

class UniversalContainer:

    x = int
    y = int

    width = int
    height = int

    headerY = int

    components = []

    #STATES
    selected = False
    resizeX = False
    resizeY = False

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.headerY = 10

    def min_size(self):
        maxX = 0
        maxY = 0
        for component in self.components:
            if (component.x+component.width) > maxX:
                maxX = component.x+component.width
            if (component.y+component.height) > maxX:
                maxY = component.y+component.height

        if self.width < maxX:
            self.width = maxX*1.2
        if self.height < maxY:
            self.height = maxY*1.2

    def resize(self, event):
        x, y = pygame.mouse.get_pos()
        if self.resizeX and event.type == pygame.MOUSEBUTTONUP:
            self.resizeX = False
        if self.resizeY and event.type == pygame.MOUSEBUTTONUP:
            self.resizeY = False

        if self.resizeX:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
            self.width = x-self.x
        if self.resizeY:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_SIZENS)
            self.height = y-self.y

        if (self.x+self.width-3 < x < self.x+self.width+3) and (self.y < y < self.y+self.height):
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_SIZEWE)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.resizeX = True
        elif (self.x < x < self.x+self.width) and (self.y+self.height-3 < y < self.y+self.height+3):
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_SIZENS)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.resizeY = True
        else:
            pygame.mouse.set_system_cursor(pygame.SYSTEM_CURSOR_ARROW)

    def render(self, screen, colour, font):
        pygame.draw.rect(screen, colour, (self.x, self.y, self.width, self.height), width=1)
        pygame.draw.rect(screen, colour, (self.x, self.y, self.width, -self.headerY), width=3)
        for component in self.components:
            component.render(screen, colour, font, self.x, self.y)
            pass

    def coords_in(self,coords):
        x, y = coords
        if (self.x < x < self.x+self.width) and (self.y < y < self.y+self.height):
            return True
        else:
            return False

    def coords_in_header(self, coords):
        x, y = coords
        if (self.x < x < self.x+self.width) and (self.y-self.headerY < y < self.y):
            return True
        else:
            return False

    def check_input(self, event):
        for component in self.components:
            component.check_input(event, self.x, self.y)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.coords_in_header(pygame.mouse.get_pos()):
                self.selected = True
        if event.type == pygame.MOUSEBUTTONUP:
            if self.selected:
                self.selected = False
        if self.selected:
            x, y = pygame.mouse.get_pos()
            self.x = x
            self.y = y
            if event.type == pygame.MOUSEBUTTONUP:
                self.selected = False
        self.resize(event)
        self.min_size()
        pass

class Label:
    x = int
    y = int

    width = 0
    height = 0

    text = ''

    def __init__(self, x, y, text=''):
        self.x = x
        self.y = y
        # self.height = height
        # self.width = width
        self.text = text

    def render(self, screen, colour, font, offsetX=0, offsetY=0):
        text = font.render(self.text, False, colour)
        self.width = text.get_width()
        screen.blit(text, (self.x+offsetX, self.y+offsetY))

    def check_input(self, event, offsetX=0, offsetY=0):
        pass

class Button:

    x = int
    y = int
    height = int
    width = int

    #TEXT PROPERTIES
    text = ''
    font_size = 12

    #STATES
    pressed = False

    def __init__(self, x, y, width, height, text=''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def render(self, screen, colour, font, offsetX=0, offsetY=0):
        text = font.render(self.text, False, colour)
        x, y = text.get_size()
        if self.text!='':
            self.width=x*1.5
        if self.pressed==False:
            pygame.draw.rect(screen, colour, (self.x+offsetX, self.y+offsetY, self.width, self.height), width=1)
        elif self.pressed:
            pygame.draw.rect(screen, colour, (self.x+offsetX, self.y+offsetY, self.width, self.height), width=4)
        screen.blit(text, (self.x+(self.width-x)/2+offsetX, self.y+offsetY))

    def coords_in(self,coords, offsetX=0, offsetY=0):
        x, y = coords
        if (self.x+offsetX < x < self.x+offsetX+self.width) and (self.y+offsetY < y < self.y+offsetY+self.height):
            return True
        else:
            return False

    def check_input(self, event, offsetX=0, offsetY=0):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.coords_in(pygame.mouse.get_pos(), offsetX, offsetY):
                self.pressed = True
        if event.type == pygame.MOUSEBUTTONUP:
            self.pressed = False
        if self.coords_in(pygame.mouse.get_pos(), offsetX, offsetY)==False:
            self.pressed = False

class Switch:

    x = int
    y = int
    height = int
    width = int

    #TEXT PROPERTIES
    text = ''
    font_size = 12

    #STATES
    pressed = False

    def __init__(self, x, y, width, height, text = ''):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def render(self, screen, colour, font, offsetX=0, offsetY=0):
        if self.text!='':
            self.width=len(self.text*self.font_size)/2
        if self.pressed==False:
            pygame.draw.rect(screen, colour, (self.x+offsetX, self.y+offsetY, self.width, self.height), width=1)
        elif self.pressed:
            pygame.draw.rect(screen, colour, (self.x+offsetX, self.y+offsetY, self.width, self.height), width=4)
        text = font.render(self.text, False, colour)
        screen.blit(text, (self.x+self.font_size/2+offsetX, self.y+offsetY))

    def coords_in(self,coords, offsetX=0, offsetY=0):
        x, y = coords
        if (self.x+offsetX < x < self.x+offsetX+self.width) and (self.y+offsetY < y < self.y+offsetY+self.height):
            return True
        else:
            return False

    def check_input(self, event, offsetX=0, offsetY=0):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.coords_in(pygame.mouse.get_pos(), offsetX, offsetY):
                if self.pressed:
                    self.pressed = False
                else:
                    self.pressed = True
