import pygame

def Write(fontsize=24, text="Namastey!", color=(0,0,0), background=None, screen=None, x=0, y=0, center:bool=False) -> None:
    """
    This function will render text on screen.

    @parameters
        fontsize : default 24
        text     : default Namastey!
        color    : default white
        background: default None
        screen   : default None -- pass where you want the text to be rendered
        x        : position in x-cordinate - Default 0
        y        : position in y-cordinate - Default 0
        center   : a boolean value which determines if the text is to be centered at (x, y)
                    default False
    USAGE:
        from utils.functions import Write
        Write(parameters)
    """

    # making our font object with the help of SysFont meaning font present in system
    # if passed None it takes default system font
    # also font is specified here
    # In this object you can also pass bold=True and italics=True if you need it
    font = pygame.font.SysFont(None, fontsize)

    # making text object from font object 
    # The True stands for antialiased and if passed False it will stand for aliased
    # if True text will be smooth
    txt = font.render(text, True, color, background)

    # making a rectangle object form the text 
    # means the area of the text
    textRect = txt.get_rect()
    if center:
        textRect.center = (x,y)
    else:
        textRect.x = x
        textRect.y = y

    # finally showing the font on the screen
    screen.blit(txt, textRect)