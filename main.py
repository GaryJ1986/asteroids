# this allows us to use code from
# the open-source pygame library
# throughout this file
import sys
import pygame

# import everything from a file
from constants import *

#import specific bits from a file
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (updateable, drawable, asteroids)
    AsteroidField.containers = (updateable)
    Shot.containers = (shots, updateable, drawable)
    asteroid_field = AsteroidField()

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 )
    
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updateable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collisions(player):
                print("Game over!")
                sys.exit()

        for shot in shots:
            if asteroid.collisions(shot):
                shot.kill()
                asteroid.kill()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)
        
        pygame.display.flip()

        # Frame Limiter
        dt = clock.tick(60) / 1000   
    
if __name__ == "__main__":
    main()