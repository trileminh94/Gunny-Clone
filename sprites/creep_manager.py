__author__ = 'tri'


import pygame
from sprites.screeps.creep_a import CreepA
from common.constant import Constant
from sprites.screeps.creep_b import CreepB
from sprites.screeps.creep_c import CreepC
from sprites.screeps.creep_d import CreepD
from sprites.screeps.creep_e import CreepE
from sprites.screeps.creep_f import CreepF
from sprites.screeps.creep_a_special import CreepASpecial
__author__ = 'tri'


class CreepManager(pygame.sprite.Sprite):
    pos1 = False
    pos2 = False
    pos3 = False
    creep_special1 = None
    def __init__(self):
        pass
    def init():
        CreepManager.pos1 = False
        CreepManager.pos2 = False
        CreepManager.pos3 = False
        CreepManager.creep_special1 = None
    init = staticmethod(init)

    def update(container, x_pos_player_world, y_pos_player_world, pos_player_screen):
        for creep in container.sprites():
            if isinstance(creep, CreepASpecial):
                if x_pos_player_world > 4705 and x_pos_player_world < 4860 and y_pos_player_world > 118:
                    creep.y = y_pos_player_world - 4
                    creep.x += creep.move_speed_x
                    print 'x=', creep.x
                else:
                    creep.y = creep.base_line
            creep.pos_creep_screen = creep.x - x_pos_player_world + pos_player_screen


    update = staticmethod(update)

    def create_creep(container, type, pos_x, pos_y, left_limit, right_limit, direction, speed):
        if type == 'A':
            creep = CreepA(pos_x, pos_y, left_limit, right_limit, direction, speed)
            creep.down_able = False
        elif type == 'B':
            creep = CreepB(pos_x, pos_y, left_limit, right_limit, direction, speed)
            creep.down_able = False
        elif type == 'C':
            creep = CreepC(pos_x, pos_y, left_limit, right_limit, direction, speed)
            creep.down_able = False
        elif type == 'D':
            creep = CreepD(pos_x, pos_y, left_limit, right_limit, direction, speed)
            creep.down_able = False
        elif type == 'E':
            creep = CreepE(pos_x, pos_y, left_limit, right_limit, direction, speed)
            creep.down_able = False
        elif type == 'F':
            creep = CreepF(pos_x, pos_y, left_limit, right_limit, direction, speed)
            creep.down_able = False
        elif type == 'A_SPECIAL':
            creep_special1 = CreepASpecial(pos_x, pos_y, left_limit, right_limit, direction, speed)
            creep_special1.down_able = False
    create_creep = staticmethod(create_creep)

    def create_creep_dynamic(x_pos_player_world, creeps_group):
        if not CreepManager.pos1 and x_pos_player_world > 700:
            CreepManager.create_creep(creeps_group, 'A', 611, 384-52, 576, 989, 0, 0.7)
            CreepManager.pos1 = True
        if CreepManager.pos1 and not CreepManager.pos2 and x_pos_player_world > 942:
            CreepManager.create_creep(creeps_group, 'E', 1500, 332, 576, 1500, 0, 4)
            CreepManager.pos2 = True
        if not CreepManager.pos3 and x_pos_player_world > 4300:
            CreepManager.create_creep(creeps_group, 'C', 5172, 320, 3272, 5176, 1, 10)
            CreepManager.pos3 = True

    create_creep_dynamic = staticmethod(create_creep_dynamic)






