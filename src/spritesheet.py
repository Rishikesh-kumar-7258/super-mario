import pygame

def Spritesheet(path) :
    """ This function returns a spritesheet on the given path """

    return pygame.image.load(path)

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

            if (len(images) == count):
                break

    return images

# Images
BACKGROUND_SPRITESHEET = Spritesheet("graphics/backgrounds.png")
BACKGROUND_IMAGES = give_images(BACKGROUND_SPRITESHEET, 0, 0, 256, 128, 3)

ALIEN_IMAGES = give_images(Spritesheet("graphics/blue_alien.png"), 0, 0, 16, 20, 11)
ALIEN_RUNNING = ALIEN_IMAGES[1:3] + [pygame.transform.flip(img, True, False) for img in ALIEN_IMAGES[1:3]]
ALIEN_JUMPING = ALIEN_IMAGES[3:5] + [pygame.transform.flip(img, True, False) for img in ALIEN_IMAGES[3:5]]
ALIEN_CLIMBING = ALIEN_IMAGES[5:7] + [pygame.transform.flip(img, True, False) for img in ALIEN_IMAGES[5:7]]