import pygame
from random import randint

class Theme:
    """
    This is the theme class.
    It will help keep track of the background theme like river, normal ground, jungle etc..
    """

    def __init__(self) -> None:
        
        # Dimensions of themeboard
        width , height = 1000, 520

        # dimension of each block 
        b_width, b_height = 50, 40

        # Number of rows and columns
        rows, columns = height // b_height, width // b_width

        # start of different things
        st_ground = 10
        st_wall = 6

        self.themeboard = []

        for col in range(columns):

            #checks for the wall
            is_wall = randint(1, 10) <= 2

            #checks for the khai
            is_khai = (not is_wall) and randint(1, 10) <= 2

            for row in range(rows):
                pass


    
    def render(self, screen) -> None:

        pass