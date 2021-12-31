import pygame
from random import randint

from pygame.constants import K_LEFT, K_RIGHT, K_SPACE, KEYDOWN, KEYUP
from src.objects import PLAYER
from src.spritesheet import Spritesheet, give_images
from src.states.basestate import Base
from src.functions import Write


class PlayState(Base):

    def __init__(self):
        super().__init__()

        self.all_sprites = []

    def enter(self, **param):

        self.screen = param['screen']
        self.screen_width = self.screen.get_width()
        self.screen_height = self.screen.get_height()
        self.gstatemachine = param['gstatemachine']

        self.spritesheet = Spritesheet("graphics/backgrounds.png")
        self.background = give_images(self.spritesheet, 0, 0, 256, 128, 3)

        self.aliens = give_images(Spritesheet(
            "graphics/blue_alien.png"), 0, 0, 16, 20, 11)

        self.player = PLAYER.copy()
        self.player['width'] = 16
        self.player['height'] = 20
        self.player['status'] = 0

        self.current_player = 0

        self.all_sprites.append(self.player)

        # scaling the images to get the full screen effect
        for i in range(len(self.background)):
            self.background[i] = pygame.transform.scale(
                self.background[i], (self.screen_width, self.screen_height))

        # rendering the current image
        self.current_image = randint(0, len(self.background)-1)

    def render(self):

        self.screen.blit(self.background[self.current_image], (0, 0))
        self.screen.blit(self.aliens[self.current_player],
                         (self.player['x'], self.player['y']))

    def update(self, param):
        # # applying gravity on all sprites
        # for sprites in self.all_sprites:
        #     if self.touches_ground(sprites):
        #         continue
        #     if sprites['gravity']:
        #         sprites['y'] += 3

        # # For player's movement animation
        # self.player['x'] += self.player['velocity']
        handleObject(self.player, self.screen, events=param)

        # key pressing events
        # for event in param:
        # When a key is pressed

        self.render()

    def leave(self):
        pass

# Functions to control different objects in the game


def handlePlayer(player, **args):

    # eventHandling
    for event in args['events']:
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                player['status'] = 'RUNNING'
                player['velocity'] = player['speed']
            if event.key == K_LEFT:
                player['status'] = 'RUNNING'
                player['velocity'] = -player['speed']

        # when a key is released
        if event.type == KEYUP:
            if event.key == K_RIGHT:
                player['status'] = 'STANDING'
                player['velocity'] = 0

    # applying gravity on player
    if player['gravity']:
        if player['y'] + player['height'] + 4 < args['s_height']:
            player['y'] += 3

    player['x'] += player['velocity']

    # applying status effects on player
    # if player['status'] == 'RUNNING':
        # 


def handleObject(object, screen=None, events=None):

    # SCREEN CONSTANTS
    s_width = screen.get_width()
    s_height = screen.get_height()

    if object['type'] == 'PLAYER':
        handlePlayer(object, s_width=s_width, s_height=s_height, events=events)
