import pygame
from random import randint

def Write(text, x, y, color, font_size, screen, center=True):
    font = pygame.font.SysFont("Comic Sans MS", font_size)
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    if not center:
        text_rect.x = x
        text_rect.y = y

    screen.blit(text, text_rect)

def transition(initial, final, time):

    time *= 60
    step = (final - initial) / time
    current = initial

    while time > 0:
        current += step

        yield current

        time -= 1

    yield final

def screen_animation(i_c, f_c, time, screen):

    clock = pygame.time.Clock()
    time *= 60
    step = (f_c - i_c) //  time
    current = i_c

    running = True
    while running:
        current += step
        screen.fill((current, current, current))
        time -= 1
        if (time == 0):
            screen.fill((f_c, f_c, f_c))
            running = False
        pygame.display.flip()
        clock.tick(60)
    
def random_color():
    """ This function will return a random color """

    return (randint(0, 255), randint(0, 255), randint(0, 255))