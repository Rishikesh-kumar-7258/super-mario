from random import randint
import pygame
from pygame.constants import K_LEFT, K_RIGHT, KEYDOWN, KEYUP
from objects.bricks import Brick
from objects.theme import Theme
from states.basestate import Base
from objects.player import Player

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

        # group containing the player
        self.player_group = pygame.sprite.GroupSingle()
        self.player = Player()
        self.player_speed = 5
        self.player_group.add(self.player)
        self.all_sprites.add(self.player)

        # themboard
        self.boards = []
        self.current_board = Theme(region="normal")
        self.boards.append(self.current_board)

        # is the player moving
        self.is_player_moving = False

    
    def render(self) -> None:
        
        # rendering themeboard
        for board in self.boards:
            board.render(self.screen)

        # rendering brick
        self.all_sprites.draw(self.screen)


    def update(self, param) -> None:

        if self.is_player_moving:
            # self.player.rect.x += self.player_speed
            for board in self.boards:
                x,y = board.origin
                board.origin = (x-self.player_speed, y)
        
        if self.current_board.origin[0] + self.current_board.width == self.gwidth:
            regions = ["jungle", "normal", "snow", "fire"]
            self.current_board = Theme( region=regions[randint(0,len(regions)-1)],
                                        origin=(self.current_board.origin[0] + self.current_board.width, 0),
                                        )
            self.boards.append(self.current_board)

        # event handling
        for event in param:
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.is_player_moving = True
                    self.player_speed = self.player_speed if self.player_speed > 0 else self.player_speed*-1
                if event.key == K_LEFT:
                    self.is_player_moving = True
                    self.player_speed = self.player_speed if self.player_speed < 0 else self.player_speed*-1
            
            if event.type == KEYUP:
                if event.key == K_LEFT or event.key == K_RIGHT:
                    self.is_player_moving = False
        
        self.render()
    
    def enter(self, **params) -> None:

        # taking variables which was pass from the previous state, in this case startstate
        self.screen = params['screen']
        self.gwidth = params['gwidth']
        self.gheight = params['gheight']
        self.gstatemachine = params['gstatemachine']