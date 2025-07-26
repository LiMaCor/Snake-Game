import pygame
from pygame.locals import *

# General settings
window_size = width, height = (1280, 720)

pygame.init()

pygame.display.set_caption("Snake Game")

screen = pygame.display.set_mode(window_size)
screen.fill((50, 50, 50))

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

pygame.quit()