import pygame
from common.constant import Constant
from common.utils import Utils
from sprites.live_bar import Live_bar
from sprites.power_bar import Power_bar
from sprites.energy_bar import Energy_bar

import math
from random import randint
from pygame.locals import *
__author__ = 'tri'


class BasicCreep(pygame.sprite.Sprite):
    screen = None   # TODO for testing

    def __init__(self, x, y):
        """
        Constructor
        :param x: position x in world
        :param y: position y in world
        :return: None
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.x = x
        self.y = y
        self.pos_creep_screen = 0   # position x of creep in screen, = creep-player + player-screen

    def update(self):

        self.frame += 0.1
        if self.direction == 0:
            self.image = self.images_forward[int(round(self.frame))%self.frame_length]
        else:
            self.image = self.images_back[int(round(self.frame))%self.frame_length]

        self.x += self.move_speed_x
        self.rect = self.rect.move(self.pos_creep_screen, 0)


        if self.down_able:
                self.rect = self.rect.move(0, self.move_speed_y)

        if math.fabs(self.dis) > self.dis_to_redirect:
            self.redirect()
            self.dis = 0

    def redirect(self):
        self.frame = 0
        self.move_speed_x = -self.move_speed_x
        if self.move_speed_x > 0:
            self.direction = 0
        else:
            self.direction = 1

    def set_down_able(self, isTrue):
        self.down_able = isTrue