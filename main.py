import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        pygame.display.flip() 


    
if __name__ == "__main__":
    main()

