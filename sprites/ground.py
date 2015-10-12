import pygame
from common.utils import Utils
from common.constant import Constant
__author__ = 'tri'


class Ground(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)

        image_resource = Utils.my_load_image('nhan vat 2', 'dead.png')
        self.image = image_resource.subsurface(100, 550, 1200, 200)

        self.rect = self.image.get_rect(midbottom=Constant.SCREENRECT.midbottom)
        self.mask = pygame.mask.from_surface(self.image)
