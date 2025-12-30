import pygame
from interfaces.score import Score

from screen import Screen
from elements.clickables import Target, Button


class States: # Game states
    START = 1
    PLAYING = 2
    END = 3


class Game:
    def __init__(self):

        # Visuals
        self.screen = Screen()
        self.border = (
            self.screen.border_th,
            self.screen.border_th + self.screen.res[0],
            self.screen.border_th,
            self.screen.border_th + self.screen.res[1])
        
        self.font_size = 40
        self.font = pygame.font.SysFont("arial", self.font_size)

        self.score = Score()

        # Clickable Entities
        self.target_rad = 100
        self.targets = [Target(
            pos=(self.screen.res[0]/2, self.screen.res[1]/2),
            dimensions=self.target_rad,
            color="red")]
        
        # Initialize variables
        self.running = False
        self.click = False
        self.mouse_pos = (0, 0)
        self.state = States.PLAYING


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

            match self.state:
                case States.START: self.handlestate_start()
                case States.PLAYING: self.handlestate_playing()
                case States.END: self.handlestate_end()
                case _: self.state = States.START

            pygame.display.update()
    

    def handlestate_start(self):
        if self.click: # Handle click. Are any START screen buttons pressed?
            pass
        pass


    def handlestate_playing(self):

        # Determine if the game is finished
        if self.score.hits == 10:
            self.state = States.END

        # Draw targets
        for target in self.targets:
            if self.click:
                if target.in_boundary(self.mouse_pos):
                    self.score.hit()
                    target.hit(self.border) # Replace a Target if it has been hit
                else: self.score.miss()
            pygame.draw.circle(self.screen.disp, target.color, target.pos, target.dimensions)


    def handlestate_end(self):
        self.screen.disp.blit(self.font.render("GAME OVER", False, "red"), (100, 100))
        self.screen.disp.blit(self.font.render(f"HITS: {self.score.hits}", False, "red"), (100, 100 + self.font_size + 10))
        self.screen.disp.blit(self.font.render(f"MISSES: {self.score.misses}", False, "red"), (100, 100 + 2 * (self.font_size + 10)))

        if self.click: # Handle click. Are any END screen buttons pressed?
            pass