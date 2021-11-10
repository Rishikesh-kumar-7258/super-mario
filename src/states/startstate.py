import pygame
from pygame.color import THECOLORS
from pygame.constants import K_RETURN, KEYDOWN
from src.functions import Write, transition
from src.states.basestate import Base


class Start(Base):

    def __init__(self):
        super().__init__()

    def enter(self, **param):
        self.screen=param['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = param['gstatemachine']

        self.font_animation = {
            "big" : transition(0, 100, 0.2),
            "small" : transition(0, 32, 0.2)
        }

        self.curr_font_size = {
            'big' : 0,
            'small' : 0
        }

    def render(self):
        Write("Super Mario", self.screen_width//2, self.screen_height//2, THECOLORS['goldenrod'], int(self.curr_font_size['big']), self.screen)
        Write("press Enter to play", self.screen_width//2, self.screen_height//2 + 100, THECOLORS['white'], int(self.curr_font_size['small']), self.screen)

    def update(self, param):

        try:
            self.curr_font_size['big'] = next(self.font_animation['big'])
            self.curr_font_size['small'] = next(self.font_animation['small'])
        except StopIteration:
            self.curr_font_size['big'] = 100
            self.curr_font_size['small'] = 32

        # event handling
        for event in param:
            if event.type == KEYDOWN:
                if event.key == K_RETURN:
                    self.gstatemachine.change('play', screen=self.screen, gstatemachine=self.gstatemachine)

        self.render()
    
    def leave(self):
        pass