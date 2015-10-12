from basic_creep import BasicCreep
from common.utils import Utils
import pygame
__author__ = 'tri'


class CreepF(BasicCreep):

    def __init__(self, x, y, direction):
        """
        Constructor
        :param x: position x in screen
        :param y: position y in screen
        :param direction: direction to move, 0 or 1
        :return:
        """
        BasicCreep.__init__(self)

        # Coefficients
        self.frame = 0
        self.frame_rate = 0.1
        self.move_speed_x = 1
        self.move_speed_y = 1
        self.direction = direction  # TODO Define enum
        if self.direction == 1:
            self.move_speed_x = -self.move_speed_x
        self.dis = 0
        self.dis_to_redirect = 200

        # Status
        self.down_able = True

        image_source = Utils.my_load_image('creep', 'creep2.png')
        self.images_forward = Utils.load_frame(image_source, 0, 0, 72.8, 60, 0, 5)
        self.images_forward_temp1 = Utils.load_frame(image_source, 0, 78, 72.8, 60, 0, 5)
        self.images_forward_temp2 = Utils.load_frame(image_source, 0, 141, 72.8, 60, 0, 4)
        for image in self.images_forward_temp1:
            self.images_forward.append(image)
        for image in self.images_forward_temp2:
            self.images_forward.append(image)

        for i in range(len(self.images_forward) - 1, -1, -1):
            self.images_forward.append(self.images_forward[i])

        self.images_back = []
        for image in self.images_forward:
            self.images_back.append(pygame.transform.flip(image, 1, 0))

        self.frame_length = len(self.images_forward)

        self.image = self.images_forward[0]

        self.rect = self.image.get_rect()   # Default position at (0,0)
        self.rect.move_ip(x, y)