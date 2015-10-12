import pygame
from pygame.locals import Color
__author__ = 'tri'


class Energy_bar(pygame.sprite.Sprite):
    """shows a bar with the energy of a Player sprite"""
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.player = player
        self.image = pygame.Surface((self.player.rect.width,7))
        self.image.set_colorkey((0,0,0)) # black transparent
        pygame.draw.rect(self.image, Color('blue'), (0, 0, self.player.rect.width, 7), 1)
        self.rect = self.image.get_rect()
        self.oldpercent = 0

    def update(self):
        self.percent = self.player.enegery / 100.0
        if self.percent != self.oldpercent:
            pygame.draw.rect(self.image, (0,0,0), (1,1,self.player.rect.width-2,5)) # fill black
            pygame.draw.rect(self.image, Color('blue'), (1,1,
                int(self.player.rect.width * self.percent),5),0) # fill green
        self.oldpercent = self.percent
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery - self.player.rect.height /2 - 10
        #check if player is still alive
        if not self.player.alive():
            self.kill() # kill the hitbar