import pygame
import sys
import eventhandlers
import math
import random

# Screen
screen_res = (1280, 720)
border_thickness = 10

# Variables
circle_rad = 100
circle_pos = (screen_res[0]/2, screen_res[1]/2) # Initial circle position, center of screen

# Screen borders, boundaries for circles to be placed on screen
border_x = (border_thickness + circle_rad, screen_res[0] - (border_thickness + circle_rad))
border_y = (border_thickness + circle_rad, screen_res[1] - (border_thickness + circle_rad))

# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(screen_res)

# Ingame variables
hits = 0
misses = 0
running = True

# Game loop
while running:
    
    events = pygame.event.get()

    for event in events:

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: #left click
                mouse_pos = pygame.mouse.get_pos()

                # Check if the circle was hit or missed
                # *If hit, place a new circle in a random location on the screen and add 1 to the hits counter
                # *If missed, add 1 to the misses counter and reduce the circle radius. If the misses counter gets to 3 strikes, terminate the program
                if eventhandlers.Check_circle_collision(mouse_pos, circle_pos[0], circle_pos[1], circle_rad):
                    circle_pos = (random.randint(border_x[0], border_x[1]), random.randint(border_y[0], border_y[1]))
                    hits += 1
                else:
                    misses += 1
                    circle_rad -= 25
                    if misses == 3:
                        running = False

    screen.fill('lightblue')
    pygame.draw.circle(screen, "red", circle_pos, circle_rad)

    pygame.display.update()

# Display score
print("hits: ", hits)
print("misses :", misses)

pygame.quit()
sys.exit()