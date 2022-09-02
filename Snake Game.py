import pygame
import time
import random

pygame.init()

WIDTH = 800
HEIGHT = 800

CYAN = (0,255,255)
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
PURP = (138,43,226)

snake_speed = 30 

clock = pygame.time.Clock() 

system_font = pygame.font.SysFont(None, 30)

pygame.display.set_caption("Snake Game :)") 
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


def Lost_Message(msg, color):
    message = system_font.render(msg, True, color)
    WINDOW.blit(message, (WIDTH/3, HEIGHT/2))


def Game():
    Game_Over = False
    Game_Close = False

    x_change = 0
    y_change = 0
    Y = 400
    X = 400

    foodx = round(random.randrange(0, WIDTH - 12) / 10.0) * 10.0
    foody = round(random.randrange(0, WIDTH - 12) / 10.0) * 10.0
 
    while not Game_Over:

        while Game_Close == True:
            Lost_Message("Press Q to Quit or R to Restart Game", BLACK)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        Game_Over = True
                        Game_Close = False
                    if event.key == pygame.K_r:
                        Game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_Over = True
            
            # moves the snake
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    y_change = -10
                    x_change = 0
                elif event.key == pygame.K_a:
                    x_change = -10
                    y_change = 0
                elif event.key == pygame.K_s:
                    y_change = 10
                    x_change = 0
                elif event.key == pygame.K_d:
                    x_change = 10    
                    y_change = 0
    
        if X >= WIDTH or X <= 0 or Y >= HEIGHT or Y <= 0:
            Game_Close = True

        X += x_change
        Y += y_change
        WINDOW.fill(PURP)
        pygame.draw.rect(WINDOW, RED, [X,Y,12,12])
        pygame.draw.rect(WINDOW, GREEN, [foodx,foody,12,12])
        pygame.display.update()

        if X == foodx and Y == foody:
            Lost_Message("Chomp!", RED)
            pygame.display.update()
        clock.tick(snake_speed)
    
    pygame.quit()
    quit()

Game()