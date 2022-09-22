import pygame
import time
import random

pygame.init()

#Constants and variables declarations 
WIDTH = 800
HEIGHT = 800

CYAN = (0,255,255)
RED = (255,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
BLACK = (0,0,0)
PURP = (138,43,226)

snake_speed = 15
ten = 10

clock = pygame.time.Clock()

system_font = pygame.font.SysFont(None, 30)


#sets screen name and size
pygame.display.set_caption("Snake Game :)")
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


#prints message in the middle of the screen
def Lost_Message(msg, color):
    message = system_font.render(msg, True, color)
    WINDOW.blit(message, (WIDTH/3, HEIGHT/2))

# snake function so we can call on it in game loop to update snake size
def snake(snake_list):
    for x in snake_list:
        pygame.draw.rect(WINDOW, RED, [x[0], x[1], ten, ten])
    
# main game function
def Game():
    Game_Over = False
    Game_Close = False

    x_change = 0
    y_change = 0
    Y = 400
    X = 400
    snake_list = []
    snake_length = 1

    #inputs food triangle at random location
    foodx = round(random.randrange(0, WIDTH - 10) / 10.0) * 10.0
    foody = round(random.randrange(0, WIDTH - 10) / 10.0) * 10.0
 
    #keeps game running
    while not Game_Over:

        #prints quit or restart options when game ends
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

        #quits if X is clicked
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Game_Over = True

            # gets users input key
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

        #checks if snake is out of bounds
        if X >= WIDTH or X <= 0 or Y >= HEIGHT or Y <= 0:
            Game_Close = True

        #sets new snake and food location
        X += x_change
        Y += y_change
        WINDOW.fill(PURP)
        pygame.draw.rect(WINDOW, GREEN, [foodx,foody,10,10])

        snake_head = []
        snake_head.append(X)
        snake_head.append(Y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        snake(snake_list)
        pygame.display.update()


        #prints chomp if snake eats food, Adds a body part and adds another random food location
        if X == foodx and Y == foody:
            Lost_Message("Chomp!", RED)
            foodx = round(random.randrange(0, WIDTH - 10) / 10.0) * 10.0
            foody = round(random.randrange(0, WIDTH - 10) / 10.0) * 10.0
            snake_length += 1

        #every 1 second 15 frames will pass
        clock.tick(snake_speed)

    pygame.quit()
    quit()

Game()
