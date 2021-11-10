import pygame
from src.statemachine import Statemachine

from src.states.startstate import Start
from src.states.playstate import PlayState

pygame.init()

# screen properties
screen_width = 800
screen_height = 600

# setting up the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Super Mario")

# clock for the game
clock = pygame.time.Clock()

# different states
states = {
    'start' : Start(),
    'play' : PlayState()
}
gstatemachine = Statemachine(states)
gstatemachine.change("start", screen=screen, gstatemachine=gstatemachine)
gstatemachine.render()

# game loop
running = True
while running:

    #event handling
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
    
    #update game logic
    screen.fill((0,0,0))
    gstatemachine.update(events)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
quit()