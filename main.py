import pygame
from pygame.constants import QUIT
from pygame.color import THECOLORS

pygame.init()


window_width = 1000
window_height = 500

screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Super Mario")

clock = pygame.time.Clock()

while 1:

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()
    
    screen.fill(THECOLORS['skyblue'])
    pygame.display.flip()
    clock.tick(60)