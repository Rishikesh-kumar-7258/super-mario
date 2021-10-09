import pygame
from objects.bricks import Brick
from states.basestate import Base

class Play(Base):
    """
    This is the main game area. 
    All the game objects and controls are rendered here.
    """

    def __init__(self) -> None:
        # call the constructor method for the class it herited from in this case base class
        super().__init__()

        # group containing all the bricks only
        self.brick_group = pygame.sprite.Group()

        #group containing all sprites
        self.all_sprites = pygame.sprite.Group()

        #number of rows and columns on the game screen
        self.rows : int= 0
        self.cols : int= 0
        self.row_height = 40
        self.col_width = 50

    
    def render(self) -> None:
        
        # rendering brick
        self.all_sprites.draw(self.screen)

    def update(self, param) -> None:
        
        self.render()
    
    def enter(self, **params) -> None:

        # taking variables which was pass from the previous state, in this case startstate
        self.screen = params['screen']
        self.gwidth = params['gwidth']
        self.gheight = params['gheight']
        self.gstatemachine = params['gstatemachine']

        # actually giving the values to rows and columns
        self.rows = self.gheight // self.row_height
        self.cols = self.gwidth // self.col_width

        #drawing walls
        self.draw_wall("normal")

    def draw_wall(self, type) -> None:
        if type == 'normal':
            for col in range(self.cols):
                for row in range(self.rows + 1):
                    if row >= int(self.rows * 0.70):
                        brick = Brick()
                        brick.rect.x = col*self.col_width
                        brick.rect.y = row*self.row_height
                        self.all_sprites.add(brick)
                        self.brick_group.add(brick)