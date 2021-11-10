import pygame

def Write(text, x, y, color, font_size, screen, center=True):
    font = pygame.font.SysFont("Comic Sans MS", font_size)
    text = font.render(text, True, color)
    text_rect = text.get_rect()
    text_rect.center = (x, y)
    if not center:
        text_rect.x = x
        text_rect.y = y
        
    screen.blit(text, text_rect)