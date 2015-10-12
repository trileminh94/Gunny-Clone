import pygame
from common.utils import Utils
from common.constant import Constant
__author__ = 'tri'


class Power_bar(pygame.sprite.Sprite):
    """shows a bar with the hitpoints of a Bird sprite"""
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        if (player.whichplayer == 1):
            self.rect = Constant.POWERBARRECT1
        else:
            self.rect = Constant.POWERBARRECT2
        self.player = player
        self.image = pygame.Surface((self.rect.width,self.rect.height))
        self.image.set_colorkey((0,0,0)) # black transparent
        pygame.draw.rect(self.image, Constant.POWERBARCOLOR, (0, 0, self.rect.width,self.rect.height),1)
        self.oldpercent = 0

    def update(self):
        self.percent = self.player.fireF
        if self.percent != self.oldpercent:
            pygame.draw.rect(self.image, (0,0,0), (1,1,self.rect.width - 2,self.rect.height - 2)) # fill black
            if self.player.whichplayer == 1:
                pygame.draw.rect(self.image, Constant.POWERBARCOLOR, (1, 1, int(self.percent * self.rect.width) , self.rect.height - 2),0) # fill green
            else:
                pygame.draw.rect(self.image, Constant.POWERBARCOLOR, (1 + self.rect.width - int(self.percent * self.rect.width) , 1, int(self.percent * self.rect.width) , self.rect.height - 2),0) # fill green
        self.oldpercent = self.percent
        #check if player is still alive
        if not self.player.alive():
            self.kill()