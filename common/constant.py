__author__ = 'tri'
from pygame.locals import *

class Constant:

    # Game constants
    MAX_SHOTS = 2      # most player bullets onscreen
    ALIEN_ODDS = 22     # chances a new alien appears
    BOMB_ODDS = 60    # chances a new bomb will drop
    ALIEN_RELOAD = 12     # frames between new aliens
    SCREENRECT = Rect(0, 0, 960, 640)
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
    TILE_WIDTH = 32
    TILE_HEIGHT = 32
    DOWNPERFRAME = 5
    JUMPPERFRAME = 5
    PLAYERWIDTH = 56
    PLAYERHEIGHT = 46
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
    PLAYER1JUMPKEY = K_j

    MAXPOWER = 800
    GRAVITY = 400
    POWERBARRECT1 = Rect(0, SCREENRECT.height - 25, 400, 20)
    POWERBARRECT2 = Rect(SCREENRECT.width - 400, SCREENRECT.height - 25, 400, 20)
    POWERBARCOLOR = (255, 51, 51)


    """ time for item """
    MONEY_TIME_TO_DIE = 100
    ITEM_TIME_TO_DIE = 1000
    ITEM_TIME_TO_LIVE = 200

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

    NUM_BULLET_TYPE = 2

    MAP =  ((0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,33,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,42,42,0,0,0,42,42,42,42,0,0,0,0,0,0,0,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,42,0,0,0,0,42,42,42,42,0,0,0,0,0,0,0,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,56,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,72,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,32,33,0,0,0,0,0,42,42,35,0,0,0,0,0,0,0,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,32,0,0,0,0,0,0,0,0,42,42,35,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,92,92,92,92,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,62,62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,33,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,92,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,2,2,7,0,69,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,82,81,87,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,62,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,67,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,32,0,0,0,0,0,0,31,32,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,79,80,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,6,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,32,32,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,32,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,31,0,0,0,0,0,0,0,0,92,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0),
(0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,86,89,90,55,0,0,0,0,87,54,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,24,32,32,25,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,12,12,13,0,0,0,0,0,0,0,0,69,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,28,28,69,70,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,32,32,32,0,0,0,0,0,0,0,52,0,0,0,0,0,0,52,52,0,0,31,32,32,33,92,92,92,92,92,92,92,92,92,92,0,0,0,92,92,92,92,92,0,0,0,92,92,92,92,0,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92),
(0,0,0,0,0,0,0,0,0,0,0,6,2,2,7,0,0,0,1,2,2,2,2,2,2,2,2,2,2,2,3,0,0,0,0,0,0,0,6,2,2,2,7,0,0,0,0,0,0,0,0,0,0,0,0,0,69,70,0,0,0,0,0,0,0,0,0,0,6,2,2,12,12,12,13,0,0,0,0,0,0,0,0,79,80,0,0,0,0,0,0,0,0,0,0,0,27,28,29,0,35,35,38,79,80,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,41,42,42,42,0,0,0,0,0,0,0,52,0,0,0,0,0,0,0,0,0,0,41,42,42,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,0,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92),
(86,56,0,0,0,0,0,0,0,87,0,0,0,0,0,0,0,0,11,12,12,12,12,12,12,12,12,12,12,12,13,0,0,0,81,86,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,79,80,0,0,0,0,0,0,0,0,0,0,0,0,11,12,12,12,12,2,2,2,3,0,0,0,0,89,90,86,87,0,0,0,0,19,28,28,20,0,37,38,39,81,82,0,38,89,90,86,87,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,31,32,33,0,0,0,0,0,0,0,0,24,32,32,32,25,0,32,32,32,32,32,0,0,0,32,32,32,42,42,42,42,0,0,0,0,0,0,0,52,0,0,0,0,0,0,0,0,0,0,41,42,42,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,0,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92),
(1,2,2,2,2,2,2,2,2,3,0,0,0,0,0,0,0,87,11,12,12,12,12,12,12,12,12,12,12,12,13,0,0,0,1,3,0,0,87,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,89,90,47,0,0,6,2,2,2,2,7,0,0,0,11,12,12,12,12,12,12,12,13,0,0,0,28,28,28,28,28,28,28,29,0,0,0,26,26,26,37,38,39,28,28,28,28,28,28,28,28,28,28,28,28,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,27,28,29,0,0,0,41,42,43,0,0,0,24,32,32,25,0,0,41,42,43,0,0,0,0,42,0,0,0,0,0,41,42,42,42,42,42,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,41,42,42,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,0,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92),
(11,12,12,12,12,12,12,12,12,12,2,2,2,2,2,2,2,2,12,12,12,12,12,12,12,12,12,12,12,12,13,0,0,0,11,12,2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,2,2,3,0,0,0,0,0,0,0,0,0,0,11,12,12,12,12,12,12,12,13,0,0,0,38,38,38,38,38,38,38,39,0,0,0,0,0,0,37,38,38,38,38,38,38,38,38,38,28,28,28,28,28,0,0,0,28,28,28,28,0,0,0,28,28,28,0,0,0,27,27,28,28,28,29,0,24,32,32,32,32,32,25,0,0,31,33,0,0,0,41,42,43,0,0,0,0,42,0,0,0,0,0,41,42,42,42,42,42,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,41,42,42,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,0,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92),
(11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13,0,0,0,11,12,12,12,12,12,8,8,8,0,0,0,18,18,18,18,0,0,0,18,18,18,11,12,12,13,0,0,0,0,0,0,0,0,0,0,11,12,12,12,12,12,12,12,13,0,0,0,38,38,38,38,38,38,38,39,0,0,0,0,0,0,37,38,38,38,38,38,38,38,38,38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,37,38,38,38,38,39,0,0,41,42,42,42,43,0,0,0,41,43,0,0,0,41,42,43,0,0,0,0,42,0,0,0,52,0,41,42,42,42,42,42,42,0,0,0,0,0,0,52,0,0,0,0,0,0,52,0,0,0,0,41,42,42,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,0,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92),
(11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13,0,0,0,11,12,12,12,12,12,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,11,27,27,13,0,0,0,0,0,0,0,0,0,0,11,12,12,12,12,12,12,12,13,0,0,0,38,38,38,38,38,38,38,39,0,0,0,0,0,0,37,38,38,38,38,38,38,38,38,38,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,37,38,38,38,38,39,0,0,41,42,42,42,43,0,0,0,41,43,0,0,0,41,0,43,0,0,0,0,42,0,0,0,0,0,41,42,42,42,42,41,42,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,41,42,42,43,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,92,0,0,0,0,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92),
(11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13,16,16,16,11,12,12,12,12,12,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,11,12,12,13,16,16,16,16,16,16,16,16,16,16,11,12,12,12,12,12,12,12,13,16,16,16,38,38,38,38,38,38,38,39,16,16,16,16,16,16,37,38,38,38,38,38,38,38,38,38,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,37,38,38,38,38,39,16,16,41,42,42,42,43,16,16,16,41,43,16,16,16,41,0,0,0,16,16,16,42,16,16,16,16,16,42,42,42,42,42,42,43,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,41,42,42,43,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,92,16,16,16,16,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92),
(11,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,13,17,17,17,11,12,12,12,12,12,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,11,12,12,13,17,17,17,17,17,17,17,17,17,17,11,12,12,7,12,12,12,12,13,17,17,17,38,38,38,38,38,38,38,39,17,17,17,17,17,17,37,38,38,38,38,38,38,38,38,38,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,37,38,38,38,38,39,17,17,41,42,42,42,43,17,17,17,41,43,17,17,17,41,42,43,17,17,17,17,42,17,17,17,17,17,42,42,42,42,42,42,42,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,41,42,42,43,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,92,17,17,17,17,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92,92))


    def __init__(self):
        pass
