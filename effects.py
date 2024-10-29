import pygame
import random
from constants import *


def explosion(screen):
    screen.fill("red")
    # TODO add explosion sound
    # pygame.mixer.init()
    # explosion_sound = pygame.mixer.Sound("explosion.mp3")
    # explosion_sound.play()
    pygame.display.flip()


def display_game_over(screen, name=None):
    pygame.font.init()
    font = pygame.font.Font(None, 150)
    explosion(screen)

    if name == None:
        name = random.choice(["Buddy", "Pal", "Old Chum", "Person who clearly lost"])

    end_game_text = f"Game Over...{name}!"

    text_surface = font.render(end_game_text, True, (255, 255, 255)) 
    text_rect = text_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
    
    screen.blit(text_surface, text_rect)
    pygame.display.flip()
