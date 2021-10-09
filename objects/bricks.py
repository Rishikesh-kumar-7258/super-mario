import pygame

class Brick(pygame.sprite.Sprite):
    """
    This is the brick class of you game.
    All the brick object will be made from this class.

    USAGE:
        brick = Brick()
    """

    def __init__(self) -> None:
        """
        constructor class
        """

        # calling init function for sprite class
        super().__init__()

        # Making brick 
        self.image = pygame.image.load("utils/images/brick.png")
        self.rect = self.image.get_rect()
        self.image.set_colorkey((255, 255, 255))

        # making mask for our brick
        self.mask = pygame.mask.from_surface(self.image)