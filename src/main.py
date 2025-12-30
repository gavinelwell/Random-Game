import pygame
import sys
from game import Game

def main():

    pygame.init()
    pygame.font.init()
    
    game_loop = Game()
    game_loop.run()

if __name__=="__main__":
    main()

    pygame.quit()
    sys.exit()