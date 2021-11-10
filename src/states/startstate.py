import pygame
from pygame.color import THECOLORS
from pygame.constants import K_RETURN, KEYDOWN
from src.functions import Write
from src.states.basestate import Base


class Start(Base):

    def __init__(self):
        super().__init__()

    def enter(self, **param):
        self.screen=param['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = param['gstatemachine']

    def render(self):
        Write("Super Mario", self.screen_width//2, self.screen_height//2, THECOLORS['goldenrod'], 100, self.screen)
        Write("press Enter to play", self.screen_width//2, self.screen_height//2 + 100, THECOLORS['white'], 32, self.screen)

    def update(self, param):

        for event in param:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.gstatemachine.change('play', screen=self.screen, gstatemachine=self.gstatemachine)

        self.render()
    
    def leave(self):
        pass