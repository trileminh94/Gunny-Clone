import pygame
from common.constant import Constant
from common.utils import Utils
from sprites.explosion import Explosion
import math
from common.e_bullet_type import EBulletType
__author__ = 'tri'


class Bullet(pygame.sprite.Sprite):
    images = []

    def __init__(self, angle, power, play_rect, type):
        pygame.sprite.Sprite.__init__(self, self.containers)
        folder = 'dan'

        self.frame_rate = 1

        image_source = Utils.my_load_image(folder, type)

        self.images = []
        if type=='simple.png':
            self.images = Utils.load_frame(image_source, 0, 0, 30, 30, 0, 4)
        else:
            self.images = Utils.load_frame(image_source, 0, 0, 30, 28, 0, 4)

        self.frame_length = len(self.images)
        self.frame = 0
        self.image = self.images[int(round(self.frame))]
        self.rect = self.image.get_rect()

        self.speed_x = math.cos(math.radians(angle)) * power * 1 + 20
        self.speed_y = -math.sin(math.radians(angle)) * power * 1 + 50

        self.acceleration = Constant.GRAVITY
        self.t = 0
        self.start_x = play_rect.centerx
        self.start_y = play_rect.centery - 70

        self.rect.move_ip(self.start_x, self.start_y)

        self.x = self.start_x
        self.y = self.start_y
        self.energy_cost = 0

    def update(self):
        self.t += 1.0/Constant.FPS

        old_x = self.x
        old_y = self.y

        self.x = self.start_x + self.speed_x * self.t
        self.y = self.start_y + self.speed_y * self.t + self.acceleration/2.0 * self.t * self.t
        self.rect.move_ip(self.x - old_x, self.y - old_y)

        self.frame += self.frame_rate
        self.image = self.images[int(round(self.frame)) % self.frame_length]
        print int(round(self.frame)) % self.frame_length

        if not Constant.SCREENRECT.contains(self.rect):
            self.kill()
