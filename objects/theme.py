import pygame
from random import randint
from pygame.color import THECOLORS

class Block:
    """ The smallest unit of the screen """

    def __init__(self, x, y, background=None, region="normal") -> None:
        """constructor"""

        # passed parameters
        self.background = background
        self.x = x
        self.y = y
        self.region = region.lower()

        # dimensions
        self.width, self.height = 50, 40

        # giving the colors to background accorind to its speciality
        self.color = THECOLORS["white"] # default color

        if self.region == "normal":
            if self.background == "sky": self.color = THECOLORS["skyblue"]
            if self.background == 'ground' : self.color = THECOLORS['brown']
            if self.background == 'khai' : self.color = THECOLORS['black']
        
        elif self.region == "jungle":
            if self.background == "sky": self.color = THECOLORS["lightgreen"]
            if self.background == 'ground' : self.color = THECOLORS['darkgreen']
            if self.background == 'khai' : self.color = THECOLORS['black']
        
        elif self.region == "snow":
            if self.background == "sky": self.color = THECOLORS["skyblue"]
            if self.background == 'ground' : self.color = THECOLORS['white']
            if self.background == 'khai' : self.color = THECOLORS['black']
        
        elif self.region == "fire":
            if self.background == "sky": self.color = THECOLORS["indianred"]
            if self.background == 'ground' : self.color = THECOLORS['darkred']
            if self.background == 'khai' : self.color = THECOLORS['black']
        
        self.border_radius = (self.background == "ground") and 5 
    def render(self, screen) -> None:

        # rendering a rectangle
        pygame.draw.rect(screen, # where
                        self.color,  # which color
                        [self.x, self.y, self.width, self.height], # dimensions and origin
                        border_radius=self.border_radius, # borderradius
                        )


class Theme:
    """
    This is the theme class.
    It will help keep track of the background theme like river, normal ground, jungle etc..
    """

    def __init__(self, region="normal", origin=(0,0)) -> None:

        # region of the theme
        self.region = region
        
        # Dimensions of themeboard
        self.width , self.height = randint(2, 5) * 1000, 520

        # dimension of each block 
        b_width, b_height = 50, 40

        # Number of rows and columns
        rows, columns = self.height // b_height, self.width // b_width

        # board containing all the blocks
        self.themeboard = []

        # origin of the board
        self.origin = origin

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
                block = Block(  x = a + col*b_width,
                                y = b + row*b_height, 
                                background = background, 
                                region = self.region,
                                )

                # adding block to the themeboard
                self.themeboard.append(block)

        self.surf = pygame.Surface([self.width, self.height])
        for block in self.themeboard:
            block.render(self.surf)
    
    def render(self, screen) -> None:
        screen.blit(self.surf, self.origin)