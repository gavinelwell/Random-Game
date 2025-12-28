import pygame
import screen
import sys
import math
import random


class States: # Game states
    START = 1
    PLAYING = 2
    END = 3


class Game():
    def __init__(self):

        # Build screen
        screen.build()

        # Initialize variables
        self.running = False
        self.click = False
        self.mouse_pos = (0, 0)


    def indep_refresh(self):
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


    def start(self):

        self.running = True
        while self.running:
            self.indep_refresh()

            match state:
                case States.START:
                    if self.click:
                        # Handle click. Are any START screen buttons pressed?
                        pass
                    # Draw START screen
                    break
                
                case States.PLAYING:
                    if self.click:
                        # Handle click. Are any PLAYING screen buttons pressed?
                        pass
                    # Draw PLAYING screen
                    break
                
                case States.END:
                    if self.click:
                        # Handle click. Are any END screen buttons pressed?
                        pass
                    # Draw END screen
                    break
                
                case _: # Assume state hasn't been initialized yet
                    state = States.START
                    break
            
            pass

        while running:
            events = pygame.event.get()
            screen.fill('lightblue')

            for event in events:
                
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.MOUSEBUTTONDOWN:

                    # Left click
                    if event.button == 1:
                        mouse_pos = pygame.mouse.get_pos()

                        # Check robot state
                        if robot_state == START:
                            pass

                        elif robot_state == PLAYING:

                            # If hit, place a new circle in a random location on the screen and add 1 to the hits counter
                            if eventhandlers.Check_circle_collision(mouse_pos, circle_pos[0], circle_pos[1], circle_rad):
                                circle_pos = (random.randint(border_x[0], border_x[1]), random.randint(border_y[0], border_y[1]))
                                hits += 1

                            # If missed, add 1 to the misses counter and reduce the circle radius. If the misses counter gets to 3 strikes, terminate the program
                            else:
                                misses += 1
                                circle_rad -= 25
                                if misses == 3:
                                    running = False

                        elif robot_state == END:
                            pass

            pygame.draw.circle(screen, "red", circle_pos, circle_rad)

            pygame.display.update()