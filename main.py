import pygame, sys, random
from pygame.locals import *
from pygame.math import Vector2

class COIN():
    def __init__(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)
        
    def draw_coin(self):
        coin_rect = pygame.Rect(
            self.position.x * cell_size, 
            self.position.y * cell_size, 
            cell_size, 
            cell_size
        )
        
        pygame.draw.rect(screen, (247, 230, 72), coin_rect)

class PLAYER():
    def __init__(self):
        self.body = [
            Vector2(5, 10), 
            Vector2(6, 10), 
            Vector2(7, 10)
        ]
        self.direction = Vector2(1, 0)
        
    def draw_player(self):
        for block in self.body:
            x_position = block.x * cell_size
            y_position = block.y * cell_size
            
            block_rect = pygame.Rect(
                x_position, 
                y_position, 
                cell_size, 
                cell_size
            )
            
            pygame.draw.rect(screen, (65, 179, 20), block_rect)
            
    def move_player(self):
        body_copy = self.body[:-1]
        body_copy.insert(0, body_copy[0] + self.direction)
        self.body = body_copy[:]

# General settings
cell_size = 40
cell_number = 24

window_size = (cell_number * cell_size, cell_number * cell_size)

pygame.init()

pygame.display.set_caption("Snake Game")

frames_per_second = pygame.time.Clock()

screen = pygame.display.set_mode(window_size)

coin = COIN()
player = PLAYER()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
    
    screen.fill((50, 50, 50))
    coin.draw_coin()
    player.draw_player()
    pygame.display.update()
    frames_per_second.tick(60)

pygame.quit()
sys.exit()