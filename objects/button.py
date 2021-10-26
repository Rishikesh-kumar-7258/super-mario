import pygame
from pygame.color import THECOLORS
from utils.functions import Write

class Button:
    """
    This is the button class. All the button will be made form this class
    """

    def __init__(self, dimension:tuple = (120, 40), color=THECOLORS["white"], background=THECOLORS['black'], text:str="Click me", pos:tuple=(0, 0),center:bool=True) -> None:
        
        self.dimension = dimension
        self.color = color
        self.background = background
        self.text = text
        self.pos = pos

        # unpacking dimensions
        w, h= dimension
        x, y = pos

        self.surf = pygame.Surface([w, h])
        self.rect = self.surf.get_rect()
        self.surf.fill(self.background)

        if center:
            self.rect.center=(x,y)
        else:
            self.rect.x = x
            self.rect.y = y

    def render(self, screen=None) -> None:
        Write(  fontsize=int(0.65*self.rect.height),
                text=self.text,
                color=THECOLORS["goldenrod"],
                screen=self.surf,
                x=self.rect.width //2,
                y=self.rect.height // 2,
                center=True
                )
        
        screen.blit(self.surf, self.rect)

    def update(self) -> None:
        pass