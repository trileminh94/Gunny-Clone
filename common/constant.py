__author__ = 'tri'
from pygame.locals import *

class Constant:

    # Game constants
    MAX_SHOTS = 2      # most player bullets onscreen
    ALIEN_ODDS = 22     # chances a new alien appears
    BOMB_ODDS = 60    # chances a new bomb will drop
    ALIEN_RELOAD = 12     # frames between new aliens
    SCREENRECT = Rect(0, 0, 1000, 600)
    MOVE_STATE = 1
    LIE_STATE = 2
    THROW_STATE = 3
    COMPLAINT_STATE = 4
    ANGRY_STATE = 5
    HEADACHE_STATE = 6
    BORING_STATE = 7
    FIRE_EYE_STATE = 8
    XFACE_STATE = 9
    CRYING_STATE = 10
    CRYING_CHONG_MAT = 11
    BOTAY_STATE = 12
    DIE_STATE = 13
    STEP_EMOTION = 0.08
    STEP_FLIP = 0.01
    FPS = 60

    HOME = 1
    GAME = 2
    GAMEOVER = 3

    RADIUS = 35
    PLAYER1FIREKEY = K_SPACE
    PLAYER1UPKEY   = K_w
    PLAYER1DOWNKey = K_s
    PLAYER1CHANGEBULLET = K_TAB
    PLAYER1LEFTKEY = K_a
    PLAYER1RIGHTKEY = K_d

    PLAYER2FIREKEY = K_l
    PLAYER2UPKEY   = K_UP
    PLAYER2DOWNKey = K_DOWN
    PLAYER2CHANGEBULLET = K_k
    PLAYER2LEFTKEY = K_LEFT
    PLAYER2RIGHTKEY = K_RIGHT

    MAXPOWER = 800
    GRAVITY = 200
    POWERBARRECT1 = Rect(0, SCREENRECT.height - 25, 400, 20)
    POWERBARRECT2 = Rect(SCREENRECT.width - 400, SCREENRECT.height - 25, 400, 20)
    POWERBARCOLOR = (255, 51, 51)


    """ time for item """
    MONEY_TIME_TO_DIE = 100
    ITEM_TIME_TO_DIE = 2000

    """Item state"""

    ITEM_STATE_LIVE =  True
    ITEM_STATE_DIE = False

    """All item """
    MONEY_ITEM = "money"
    MAGIC_BOX_ITEM = "magic_box"
    BUMERANGE_TREE_ITEM = "bumerange_tree"
    MONSTER_ITEM = "monster"
    BERRY_ITEM = "berry"


    """ item style """
    ADD = 1
    SUBTRACT = 2

    """ item feature """
    MONEY = 1
    BUMERANGE = 2
    LIFE = 3
    ENERGY = 4
    POWER = 5



    def __init__(self):
        pass
