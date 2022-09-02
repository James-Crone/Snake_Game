import pygame
import time
pygame.init()


# snake
x_change = 0
y_change = 0
Y = 400
X = 400 
snake_speed = 30 

# colors
CYAN = (0,255,255)
RED = (255,0,0)
WHITE = (255, 255, 255)

# Screen
WIDTH = 800
HEIGHT = 800
clock = pygame.time.Clock() 
system_font = pygame.font.SysFont(None, 50)

# Screen
pygame.display.set_caption("Snake Game :)") 
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))


# Displays text on screen
def Lost_Message(msg, color):
    message = system_font.render(msg, True, color)
    WINDOW.blit(message, (WIDTH/3, HEIGHT/2))


# main loop
Game_Over = False
while not Game_Over:
    # keeps window open
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

    # determins if the snake is out of bounds
    if X >= WIDTH or X <= 0 or Y >= HEIGHT or Y <= 0:
        Game_Over = True
        Lost_Message("You Lost", RED)
        pygame.display.update()
        time.sleep(1)
        
    # new x and y axis
    X += x_change
    Y += y_change

    WINDOW.fill(CYAN)
    pygame.draw.rect(WINDOW, RED, [X,Y,10,10])

    pygame.display.update()

    clock.tick(snake_speed)


pygame.display.update()
pygame.quit()
quit()