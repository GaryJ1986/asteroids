# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame

# import everything from a file
from constants import *

#import specific bits from a file
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip()

        # Frame Limiter
        dt = clock.tick(60) / 1000   
    
if __name__ == "__main__":
    main()