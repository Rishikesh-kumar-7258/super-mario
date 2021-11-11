import pygame
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

    def render(self):
        
        Write("Playstate", self.screen_width // 2, self.screen_height // 2, (255, 255, 255), 100, self.screen)

    def update(self, param):
        self.render()

    def leave(self):
        pass