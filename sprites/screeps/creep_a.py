from basic_creep import BasicCreep
from common.utils import Utils
import pygame
__author__ = 'tri'

# Bo xuong
class CreepA(BasicCreep):

    def __init__(self, x, y, direction, left, right):
        """
        Constructor
        :param x: position x in world
        :param y: position y in world
        :param direction: direction to move, 0 or 1
        :param left, right: limit position for moving of creep
        :return: None
        """
        BasicCreep.__init__(self, x, y, left, right)

        # Coefficients
        self.frame = 0
        self.frame_rate = 0.3
        self.move_speed_x = 1
        self.move_speed_y = 1
        self.direction = direction  # TODO Define enum
        if self.direction == 1:
            self.move_speed_x = -self.move_speed_x
        self.x = x
        self.y = y
        self.pos_creep_screen = 0
        self.dis_to_redirect = 300
        self.left = left
        self.right = right

        # Status
        self.down_able = True

        image_source = Utils.my_load_image('creep', 'creep1.png')
        self.images_forward = Utils.load_frame(image_source, 803, 215, 41, 55, 12, 4)

        self.images_back = []
        for image in self.images_forward:
            self.images_back.append(pygame.transform.flip(image, 1, 0))

        self.frame_length = len(self.images_forward)

        self.image = self.images_forward[0]

        self.rect = self.image.get_rect()   # Default position at (0,0)
        self.rect.move_ip(self.pos_creep_screen, 0)