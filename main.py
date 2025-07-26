import pygame
from pygame.locals import *
import random

# General settings
window_size = width, height = (1280, 720)
canvas_w = int(width / 1.2)
canvas_border_w = int(width / 80)
left_border_x_axis = width / 2 - canvas_w / 2
right_border_x_axis = width / 2 + canvas_w / 2

pygame.init()

pygame.display.set_caption("Snake Game")

screen = pygame.display.set_mode(window_size)
screen.fill((50, 50, 50))

# Graphics

# Canvas
pygame.draw.rect(
    screen, 
    (0, 0, 0), 
    (width / 2 - canvas_w / 2, 15, canvas_w, height - 30)
)

# Canvas borders

# Top
pygame.draw.rect(
    screen, 
    (255, 255, 255), 
    (left_border_x_axis, 15, canvas_w, 15)
)

# Bottom
pygame.draw.rect(
    screen, 
    (255, 255, 255), 
    (left_border_x_axis, height - 30, canvas_w, 15)
)

# Left
pygame.draw.rect(
    screen, 
    (255, 255, 255), 
    (left_border_x_axis, 15, canvas_border_w, height - 30)
)

# Right
pygame.draw.rect(
    screen, 
    (255, 255, 255), 
    (right_border_x_axis, 15, canvas_border_w, height - 30)
)

# Player and coin images

player = pygame.image.load("player.png")
player_location = player.get_rect()
player_location.center = right_border_x_axis - 120, height * 0.2

coin = pygame.image.load("coin.png")
coin_location = coin.get_rect()
coin_location.center = left_border_x_axis + 120, height * 0.4

pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
    # Drawing the entities in the map
    screen.blit(player, player_location)
    screen.blit(coin, coin_location)
    
    pygame.display.update()

pygame.quit()