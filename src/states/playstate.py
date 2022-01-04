import pygame
from random import randint

from pygame.constants import K_LEFT, K_RIGHT, K_SPACE, KEYDOWN, KEYUP
from src.spritesheet import ALIEN_IMAGES, BACKGROUND_IMAGES, ALIEN_RUNNING, ALIEN_JUMPING, ALIEN_CLIMBING
from src.objects import PLAYER
from src.states.basestate import Base
from src.functions import Write

ANIMATE = pygame.USEREVENT + 1

class PlayState(Base):

    def __init__(self):
        super().__init__()

        self.all_sprites = []

        

    def enter(self, **param):

        self.screen = param['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = param['gstatemachine']

        self.player = PLAYER.copy()
        self.player['width'] = 32
        self.player['height'] = 40

        self.all_sprites.append(self.player)

        pygame.time.set_timer(ANIMATE, 100)

        # scaling the images to get the full screen effect
        for i in range(len(BACKGROUND_IMAGES)):
            BACKGROUND_IMAGES[i] = pygame.transform.scale(
                BACKGROUND_IMAGES[i], (self.screen_width, self.screen_height))

        # rendering the current image
        self.current_image = randint(0, len(BACKGROUND_IMAGES)-1)

    def render(self):

        self.screen.blit(BACKGROUND_IMAGES[self.current_image], (0, 0))
        if self.player['status'] == 'RUNNING':
            self.screen.blit(pygame.transform.scale(ALIEN_RUNNING[self.player['current_player']], (32, 40)),
                         (self.player['x'], self.player['y']))
        elif self.player['status'] == 'JUMPING':
            self.screen.blit(pygame.transform.scale(ALIEN_JUMPING[self.player['current_player']], (32, 40)),
                         (self.player['x'], self.player['y']))
        elif self.player['status'] == 'CLIMBING':
            self.screen.blit(pygame.transform.scale(ALIEN_CLIMBING[self.player['current_player']], (32, 40)),
                         (self.player['x'], self.player['y']))
        else :
            self.screen.blit(pygame.transform.scale(ALIEN_IMAGES[self.player['current_player']], (32, 40)),
                         (self.player['x'], self.player['y']))

    def update(self, param):
        
        handleObject(self.player, self.screen, events=param)

        self.render()

    def leave(self):
        pass

# Functions to control different objects in the game


def handlePlayer(player,**args):

    # eventHandling
    for event in args['events']:
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player['status'] = 'RUNNING'
                player['velocity'] = player['speed']
                player['current_player'] = 0
            if event.key == K_LEFT:
                player['status'] = 'RUNNING'
                player['velocity'] = -player['speed']
                player['current_player'] = 2

        # when a key is released
        if event.type == KEYUP:
            player['current_player'] = 0
            if event.key == K_RIGHT:
                player['status'] = 'STANDING'
                player['velocity'] = 0
            if event.key == K_LEFT:
                player['status'] = 'STANDING'
                player['velocity'] = 0

        # ANIMATE custom made event
        if event.type == ANIMATE:
            if player['status'] == 'RUNNING':
                player['current_player'] = player['current_player'] + 1
                if player['current_player'] > 2:
                    player['current_player'] = 1
            else:
                player['current_player'] = 0

    # applying gravity on player
    if player['gravity']:
        if player['y'] + player['height'] + 4 < args['s_height']:
            player['y'] += 3

    player['x'] += player['velocity']



def handleObject(object, screen=None, events=None):

    # SCREEN CONSTANTS
    s_width = screen.get_width()
    s_height = screen.get_height()

    if object['type'] == 'PLAYER':
        handlePlayer(object, s_width=s_width, s_height=s_height, events=events)
