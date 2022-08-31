import dis
from tkinter import EventType
import pygame

pygame.init()  #Initilizes the game

x_change,y_change,Y,X,CYAN,RED,WHITE,WIDTH,HEIGHT = 0,0,400,400,(0,255,255),(255,0,0),(255, 255, 255),800,800 #Declorations 
clock = pygame.time.Clock()

pygame.display.set_caption("Snake Game :)") #sets the title 
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) #Displays the window
WINDOW.fill(WHITE)#Sets display windows background color

Game_Over = False
while not Game_Over:#stops window from closing untill (X) is clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_Over = True

        if event.type == pygame.KEYDOWN:# Moves the snake
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
            X += x_change
            Y += y_change
        pygame.draw.rect(WINDOW, RED, [X,Y,10,10])#displays the snakew
        clock.tick(30)
        pygame.display.update()


