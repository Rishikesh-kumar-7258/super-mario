from src.functions import random_color


BRICK = {
    'x' : 0,
    'y' : 0,
    'width' : 20,
    'height' : 20,
    'color' : random_color()
}

""" 
    This will contain player information.
    status:
        standing
        running
        jumping up
        jumping down
        climbing up
        climbing down
"""
PLAYER = {
    
    'x' :0,
    'y' : 0,
    'status' : 'STANDING',
    'width' : 0,
    'height' : 0,
    'alive' : True,
    'gravity' : True,
    'speed' : 3,
    'velocity' : 0,
    'type' : 'PLAYER',
    'current_player' : 0,
}