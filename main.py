import pygame, sys, random
from pygame.locals import *
from pygame.math import Vector2

class COIN():
    def __init__(self):
        self.x = 5
        self.y = 3
        self.position = Vector2(self.x, self.y)
        
    def draw_coin(self):
        coin_rect = pygame.Rect(
            self.position.x, 
            self.position.y, 
            cell_size, 
            cell_size
        )
        
        pygame.draw.rect(screen, (247, 230, 72), coin_rect)

# General settings
cell_size = 40
cell_number = 24

window_size = (cell_number * cell_size, cell_number * cell_size)

pygame.init()

pygame.display.set_caption("Snake Game")

frames_per_second = pygame.time.Clock()

screen = pygame.display.set_mode(window_size)

coin = COIN()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    screen.fill((50, 50, 50))
    coin.draw_coin()
    pygame.display.update()
    frames_per_second.tick(60)

pygame.quit()
sys.exit()