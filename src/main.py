import pygame
import sys
import eventhandlers
import math
import random

screen_res = (1280, 720)

circle_pos = (screen_res[0]/2, screen_res[1]/2)
circle_rad = 100

border_thickness = 10
border_x = (border_thickness + circle_rad, screen_res[0] - (border_thickness + circle_rad))
border_y = (border_thickness + circle_rad, screen_res[1] - (border_thickness + circle_rad))

pygame.init()
screen = pygame.display.set_mode((1280, 720))

def check_circle_collision() -> bool:
    mouse_pos = pygame.mouse.get_pos()

    if math.sqrt(math.pow(mouse_pos[0] - circle_pos[0], 2) + math.pow(mouse_pos[1] - circle_pos[1], 2)) <= circle_rad:
        return True
    else:
        return False

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #left click
                if check_circle_collision():
                    circle_pos = (random.randint(border_x[0], border_x[1]), random.randint(border_y[0], border_y[1]))

    screen.fill('lightblue')
    pygame.draw.circle(screen, "red", circle_pos, circle_rad)

    pygame.display.update()