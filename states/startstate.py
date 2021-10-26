import pygame
from pygame.color import THECOLORS
from states.basestate import Base
from utils.functions import Write
from objects.button import Button

class Start(Base):
    """
    This is the first screen which will be rendered to the user.
    """

    def __init__(self) -> None:
        super().__init__()

    def render(self) -> None:
        Write(  fontsize=124,
                text="Super Mario", 
                color=THECOLORS["goldenrod"],
                screen=self.screen,
                x = self.gwidth // 2,
                y = self.gheight // 2,
                center = True
                )
        
        self.startbtn.render(self.screen)

    def update(self, param) -> None:

        self.startbtn.update()
        self.render()

    def enter(self, **params) -> None:
        self.screen = params['screen']
        self.gwidth = params['gwidth']
        self.gheight = params['gheight']

        self.startbtn = Button( pos=(self.gwidth//2, 
                                self.gheight//2 + 100), 
                                text="Start", 
                                background=THECOLORS['darkgreen'],
                                )