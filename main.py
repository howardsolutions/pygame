from constants import *

import pygame;
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    #  init the game
    pygame.init()
    
    clock = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    
    # Game groups 
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    while True:
        # check if the user has closed the window and exit the game loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Moving Around 
        updatable.update(dt)
        
        # fill the screen w black color
        screen.fill("black")
        
        # re-render the player on the screen each frame
        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
    
        # update aka refresh the screen
        pygame.display.flip()
        
        # limit the framerate to 60 FPS
        dt = clock.tick(60)  / 1000

if __name__ == "__main__":
    main()
