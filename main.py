import pygame, sys, random
from pygame.locals import *

# General settings
cell_size = 40
cell_number = 24

window_size = (cell_number * cell_size, cell_number * cell_size)

pygame.init()

pygame.display.set_caption("Snake Game")

frames_per_second = pygame.time.Clock()

screen = pygame.display.set_mode(window_size)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    screen.fill((50, 50, 50))
    pygame.display.update()
    frames_per_second.tick(60)

pygame.quit()
sys.exit()