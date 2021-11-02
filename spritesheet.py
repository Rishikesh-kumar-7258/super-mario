import pygame

class SpriteSheet:
    """
    Makes images using spritesheet
    """

    def __init__(self, filename) -> None:
        
        self.filename = filename
        self.sheet = pygame.image.load(filename).convert()
    
    def get_sprite(self, x, y, w, h) -> pygame.Surface:
        """"
        Gets the image from the spritesheet
        """

        sprite = pygame.Surface((w, h))
        sprite.blit(self.sheet, (0, 0), (x, y, w, h))
        sprite.set_colorkey((0, 0, 0))
        return sprite