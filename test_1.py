import pygame
import random

display_width = 800
display_height = 600
radius = 10
white = (255, 255, 255)
black = (0, 0, 0)

pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))

def stars(x, y, color):
    pygame.draw.circle(gameDisplay, color, [x, y], radius)

def game_loop():
    circle_x = random.randint(radius, display_width - radius)
    circle_y = -radius
    while True:
        circle_y += 5
        if circle_y > display_height + radius:
            circle_y = 0 - radius
            circle_x = random.randint(0, display_width)
        gameDisplay.fill(black)
        stars(circle_x, circle_y, white)
        pygame.display.update()

game_loop()