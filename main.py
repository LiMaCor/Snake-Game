import pygame, sys, random
from pygame.locals import *
from pygame.math import Vector2

class COIN():
    def __init__(self):
        self.randomize()
        
    def draw_coin(self):
        coin_rect = pygame.Rect(
            self.position.x * cell_size, 
            self.position.y * cell_size, 
            cell_size, 
            cell_size
        )
        
        pygame.draw.rect(screen, (247, 230, 72), coin_rect)
        
    def randomize(self):
        self.x = random.randint(0, cell_number - 1)
        self.y = random.randint(0, cell_number - 1)
        self.position = Vector2(self.x, self.y)

class PLAYER():
    def __init__(self):
        self.body = [
            Vector2(5, 10), 
            Vector2(4, 10), 
            Vector2(3, 10)
        ]
        self.direction = Vector2(1, 0)
        self.new_body_part = False
        
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
        if self.new_body_part:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
            
            self.new_body_part = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + self.direction)
            self.body = body_copy[:]
        
    def add_body(self):
        self.new_body_part = True

class MAIN():
    def __init__(self):
        self.player = PLAYER()
        self.coin = COIN()
        
    def update(self):
        self.player.move_player()
        self.check_collision()
        self.check_fail()
        
    def draw_elements(self):
        self.coin.draw_coin()
        self.player.draw_player()
        
    def check_collision(self):
        if self.coin.position == self.player.body[0]:
            self.coin.randomize()
            self.player.add_body()
            
    def check_fail(self):
        if not 0 <= self.player.body[0].x < cell_number or not 0 <= self.player.body[0].y < cell_number:
            self.game_over()
    
    def game_over(self):
        pygame.quit()
        sys.exit()

# General settings
cell_size = 40
cell_number = 24

window_size = (cell_number * cell_size, cell_number * cell_size)

pygame.init()

pygame.display.set_caption("Snake Game")

frames_per_second = pygame.time.Clock()

screen = pygame.display.set_mode(window_size)

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = MAIN()

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == SCREEN_UPDATE:
            main_game.update()
        if event.type == pygame.KEYDOWN:
            if event.key in [K_UP, K_w]:
                main_game.player.direction = Vector2(0, -1)
            if event.key in [K_DOWN, K_s]:
                main_game.player.direction = Vector2(0, 1)
            if event.key in [K_LEFT, K_a]:
                main_game.player.direction = Vector2(-1, 0)
            if event.key in [K_RIGHT, K_d]:
                main_game.player.direction = Vector2(1, 0)
    
    screen.fill((50, 50, 50))
    main_game.draw_elements()
    pygame.display.update()
    frames_per_second.tick(60)

pygame.quit()
sys.exit()