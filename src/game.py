import pygame
import sys
import math
import random

from screen import Screen
from elements.clickables import Target, Button


class States: # Game states
    START = 1
    PLAYING = 2
    END = 3


class Game:
    def __init__(self):

        # Build screen
        self.screen = Screen()
        self.border = (
            self.screen.border_th,
            self.screen.border_th + self.screen.res[0],
            self.screen.border_th,
            self.screen.border_th + self.screen.res[1])

        # Initialize variables
        self.running = False
        self.click = False
        self.mouse_pos = (0, 0)

        # Initialize clickable entities
        self.target_rad = 100
        self.targets = (Target(
            pos=(self.screen.res[0]/2, self.screen.res[1]/2),
            dimensions=self.target_rad,
            color="red"))


    def refresh_vars(self):
        """
        Refreshes variables that are independent of game state
        """
        self.click = False
        self.mouse_pos = (0, 0)

        events = pygame.event.get()
        for event in events:
            
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.click = True
                    self.mouse_pos = pygame.mouse.get_pos()


    def run(self):

        self.running = True
        while self.running:
            self.refresh_vars()
            self.screen.disp.fill('lightblue')

            match state:
                case States.START:
                    if self.click: # Handle click. Are any START screen buttons pressed?
                        pass
                    # Draw START screen
                    break
                
                case States.PLAYING:
                    for target in self.targets:
                        if self.click and target.in_boundary(self.mouse_pos): target.hit(self.border) # Replace a Target if it has been hit
                        pygame.draw.circle(self.screen.disp, target.color, target.pos, target.dimensions) # Draw PLAYING screen
                    break
                
                case States.END:
                    if self.click: # Handle click. Are any END screen buttons pressed?
                        pass
                    # Draw END screen
                    break
                
                case _: # Assume state hasn't been initialized yet
                    state = States.START
                    break

            pygame.display.update()