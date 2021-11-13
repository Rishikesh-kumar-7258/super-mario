from src.functions import random_color


BRICK = {
    'x' : 0,
    'y' : 0,
    'width' : 20,
    'height' : 20,
    'color' : random_color()
}

PLAYER = {
    """ 
    This will contain player information.
    status:
        0 - standing
        1 - running
        2 - jumping up
        3 - jumping down
        4 - climbing up
        5 - climbing down
    """
    'x' :0,
    'y' : 0,
    'status' : 0,
    'width' : 0,
    'height' : 0,
    'alive' : True
}