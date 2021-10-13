import pygame
from random import randint
from pygame.color import THECOLORS

class Block:
    """ The smallest unit of the screen """

    def __init__(self, x, y, background=None) -> None:
        """constructor"""

        self.background = background
        self.x = x
        self.y = y

        # dimensions
        self.width, self.height = 50, 40

        # giving the colors to background accorind to its speciality
        self.color = THECOLORS["white"]
        if self.background == "sky":
            self.color = THECOLORS['skyblue']
        elif self.background == "ground":
            self.color = THECOLORS['brown']
        elif self.background == "khai":
            self.color = THECOLORS['black']
        
        self.border_radius = (self.background == "ground") and 5    
    def render(self, screen,origin=(0,0)) -> None:

        # rendering a rectangle
        pygame.draw.rect(screen, # where
                        self.color,  # which color
                        [origin[0]+self.x, origin[1]+self.y, self.width, self.height], # dimensions and origin
                        border_radius=self.border_radius, # borderradius
                        )


class Theme:
    """
    This is the theme class.
    It will help keep track of the background theme like river, normal ground, jungle etc..
    """

    def __init__(self) -> None:
        
        # Dimensions of themeboard
        width , height = randint(2000, 5000), 520

        # dimension of each block 
        b_width, b_height = 50, 40

        # Number of rows and columns
        rows, columns = height // b_height, width // b_width

        # board containing all the blocks
        self.themeboard = []

        # origin of the board
        self.origin = (0, 0)

        for col in range(columns):

            #checks for the wall
            is_wall = randint(1, 10) == 1

            #checks for the khai
            is_khai = (not is_wall) and randint(1, 10) == 1

            for row in range(rows):

                # giving its background
                if is_wall:
                    if (row >= 5) :
                        background = "ground"
                    else:
                        background = "sky"
                elif is_khai:
                    if row >= 9:
                        background = "khai"
                    else: 
                        background = "sky"
                else:
                    if row >= 9:
                        background = "ground"
                    else: 
                        background = "sky"
                
                # making block object
                a, b = self.origin
                block = Block(x=a + col*b_width, y=b+row*b_height, background=background)

                # adding block to the themeboard
                self.themeboard.append(block)

    
    def render(self, screen) -> None:

        for block in self.themeboard:
            block.render(screen, self.origin)