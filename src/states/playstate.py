import pygame
from random import randint

from pygame.constants import K_SPACE, KEYDOWN
from src.objects import PLAYER
from src.spritesheet import Spritesheet, give_images
from src.states.basestate import Base
from src.functions import Write

class PlayState(Base):

    def __init__(self):
        super().__init__()

    def enter(self, **param):
        
        self.screen = param['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = param['gstatemachine']

        self.spritesheet = Spritesheet("graphics/backgrounds.png")
        self.background = give_images(self.spritesheet, 0, 0, 256, 128, 3)

        self.aliens = give_images(Spritesheet("graphics/blue_alien.png"), 0, 0, 16, 20, 11)

        self.player = PLAYER.copy()
        self.player['x'] = 0
        self.player['y'] = 0
        self.player['width'] = 16
        self.player['height'] = 20
        self.player['status'] = 0

        self.current_player = 0

        # scaling the images to get the full screen effect
        for i in range(len(self.background)):
            self.background[i] = pygame.transform.scale(self.background[i], (self.screen_width, self.screen_height))

        # rendering the current image
        self.current_image = randint(0, len(self.background)-1)



    def render(self):
        
        self.screen.blit(self.background[self.current_image], (0, 0))
        self.screen.blit(self.aliens[self.current_player], (0,0))


    def update(self, param):
        for event in param:
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    self.current_player += 1
                    self.current_player %= 11
        self.render()

    def leave(self):
        pass