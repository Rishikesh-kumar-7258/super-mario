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

        

        # themboard
        self.current_board = Theme(region="normal")

        # is the player moving
        self.is_player_moving = False

        # gravity
        self.gravity = 1

    
    def render(self) -> None:
        
        # rendering themeboard
        if self.current_board.prev != None : self.current_board.prev.render(self.screen)
        self.current_board.render(self.screen)
        if self.current_board.next != None : self.current_board.next.render(self.screen)

        # rendering brick
        self.all_sprites.draw(self.screen)


    def update(self, param) -> None:

        # stopping player on the ground
        # if self.player.rect.y + self.player.rect.height + 5 >= 

        # updating the speed
        self.player_speedY += self.gravity

        # applying gravity to the player
        # self.player.rect.y += self.player_speedY

        # moving the player
        if self.is_player_moving:
            if self.current_board.prev != None : self.current_board.prev.move(self.player_speedX)
            self.current_board.move(self.player_speedX)
            if self.current_board.next != None : self.current_board.next.move(self.player_speedX)
        
        # updating current board to next board 
        if self.current_board.origin[0] + self.current_board.width <= self.gwidth // 2:
            self.current_board = self.current_board.next
        if self.current_board.origin[0] >= self.gwidth // 2:
            self.current_board = self.current_board.prev

        # Creating a new theme
        if self.current_board.origin[0] + self.current_board.width == self.gwidth:
            regions = ["jungle", "normal", "snow", "fire"]
            if self.current_board.next == None : self.current_board.next = Theme( region=regions[randint(0,len(regions)-1)],
                                        origin=(0, 0),
                                        )
            self.current_board.next.origin = (self.gwidth, 0)
            self.current_board.next.prev = self.current_board

        # event handling
        for event in param:
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    self.is_player_moving = True
                    self.player_speedX = self.player_speedX if self.player_speedX > 0 else self.player_speedX*-1
                if event.key == K_LEFT:
                    self.is_player_moving = True
                    self.player_speedX = self.player_speedX if self.player_speedX < 0 else self.player_speedX*-1
            
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

        # group containing the player
        self.player_group = pygame.sprite.GroupSingle()
        self.player = Player()
        self.player.rect.y = self.gheight - 160 - self.player.rect.height
        self.player.rect.x = 0
        self.player_speedX = 5
        self.player_speedY = 0
        self.player_group.add(self.player)
        self.all_sprites.add(self.player)