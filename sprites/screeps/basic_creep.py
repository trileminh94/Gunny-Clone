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

    def __init__(self):
        """
        Constructor
        :param x: position x in screen
        :param y: position y in screen
        :return: None
        """
        pygame.sprite.Sprite.__init__(self, self.containers)

        # # Coefficients
        # self.frame = 0
        # self.frame_rate = 0.3
        # self.move_speed_x = 1
        # self.move_speed_y = 1
        # self.direction = 0  # TODO Define enum
        # if self.direction == 0:
        #     self.move_speed_x = 0.3
        # else:
        #     self.move_speed_x = -0.3
        #
        # # Status
        # self.down_able = True
        #
        # image_source = None
        # self.images_forward = None
        # self.images_back = None
        # self.frame_length = 0
        #
        # self.image = None
        #
        # self.rect = None


    def update(self):

        self.frame += 0.1
        if self.direction == 0:
            self.image = self.images_forward[int(round(self.frame))%self.frame_length]
        else:
            self.image = self.images_back[int(round(self.frame))%self.frame_length]

        self.rect = self.rect.move(self.move_speed_x, 0)
        self.dis += self.move_speed_x

        if self.down_able:
                self.rect = self.rect.move(0, self.move_speed_y)

        #pygame.draw.rect(BasicCreep.screen, 0xffffff, self.rect, 3) # Just 4 test

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