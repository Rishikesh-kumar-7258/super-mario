import pygame
from pygame.constants import QUIT
from pygame.color import THECOLORS

# initializing pygame
pygame.init()

# width and height of the game window
window_width = 1000
window_height = 500

# making the screen
screen = pygame.display.set_mode((window_width, window_height))

# setting caption to the screen
pygame.display.set_caption("Super Mario")

# making a clock to manage the game loop
clock = pygame.time.Clock()

# this is our game loop
while 1:

    # this captures all the events in our game keypressed, moused and etc..
    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            exit()
    
    # filling the screen with skyblue color
    screen.fill(THECOLORS['skyblue'])

    # updating the display
    pygame.display.flip()

    # it gives our game a fps of 60
    clock.tick(60)