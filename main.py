import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    
    drawable_group = pygame.sprite.Group()
    updatable_group = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    asteroid_field_group = pygame.sprite.Group()



    Asteroid.containers = (asteroid_group, updatable_group, drawable_group)
    AsteroidField.containers = updatable_group
    asteroid_field = AsteroidField()
    
    Player.containers = (updatable_group, drawable_group)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updatable_obj in updatable_group:
            updatable_obj.update(dt)


        screen.fill("black")

        # drawable_group.draw(screen) 
        for drawable_obj in drawable_group:
            drawable_obj.draw(screen)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()

