import pygame

def Spritesheet(path) :
    """ This function returns a spritesheet on the given path """

    return pygame.image.load(path).convert()

def give_images(spritesheet, x, y, width, height, count):
    """ This function will give a list of images """

    sheet_width = spritesheet.get_width()
    sheet_height = spritesheet.get_height()

    images = []
    for i in range(count):
        surf = pygame.Surface([width, height])
        surf.blit(surf, (0, 0), (x + i*width, y, width, height))
        images.append(surf)

    return images