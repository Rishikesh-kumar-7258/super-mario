import pygame

class Player(pygame.sprite.Sprite):
    """
    This is player class. 
    Player object will be made from here
    """

    def __init__(self) -> None:
        """ constructor method """
        super().__init__()

        # loaded both images
        self.image1 = pygame.image.load("utils/images/player/stand")
        self.image2 = pygame.image.load("utils/images/player/run")

        # checks if the image is running
        self.running = False

        # counts the time for animation of running
        self.timepassed = 0

        # making image sprite
        self.image = self.image1
        self.rect = self.image.get_rect()
    
    def run(self) -> None:
        self.timepassed += 1

        if (self.timepassed >= 20) :
            self.image = self.image2 ^ self.image1
        
        self.rect = self.image.get_rect()