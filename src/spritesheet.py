import pygame

def Spritesheet(path) :
    """ This function returns a spritesheet on the given path """

    return pygame.image.load(path).convert()

def give_images(spritesheet, x, y, width, height, count):
    """ This function will give a list of images """

    sheet_width = spritesheet.get_width()
    sheet_height = spritesheet.get_height()

    rows = sheet_height // height
    cols = sheet_width // width

    images = []
    for row in range(rows):
        for col in range(cols):
            surf = pygame.Surface([width, height])
            surf.blit(spritesheet, (0,0), (col*width, row*height, width, height))
            surf.set_colorkey((0,0, 0))
            images.append(surf)

    return images