import pygame

def Spritesheet(path) :
    """ This function returns a spritesheet on the given path """

    return pygame.image.load(path).convert()
