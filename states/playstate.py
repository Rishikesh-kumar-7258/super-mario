import pygame
from states.basestate import Base

class Play(Base):
    """
    This is the main game area. 
    All the game objects and controls are rendered here.
    """

    def __init__(self) -> None:
        """ Constructor method """

        # call the constructor method for the class it herited from in this case base class
        super().__init__()
    
    def render(self) -> None:
        pass