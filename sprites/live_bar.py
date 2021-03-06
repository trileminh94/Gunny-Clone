import pygame
from pygame.locals import *
__author__ = 'tri'


class Live_bar(pygame.sprite.Sprite):
    """shows a bar with the hitpoints of a Player sprite"""
    def __init__(self, player, monster, isPlayer):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.isPlayer = isPlayer
        if self.isPlayer:
            self.player = player
            self.image = pygame.Surface((self.player.rect.width,7))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.rect(self.image, Color('green'), (0,0,self.player.rect.width,7),1)
        else:
            self.monster = monster
            self.image = pygame.Surface((self.monster.rect.width,7))
            self.image.set_colorkey((0,0,0)) # black transparent
            pygame.draw.rect(self.image, Color('green'), (0,0,self.monster.rect.width,7),1)
        self.rect = self.image.get_rect()
        self.oldpercent = 0

    def update(self):
        if self.isPlayer:
            self.percent = self.player.health / 100.0
            if self.percent != self.oldpercent:
                pygame.draw.rect(self.image, (0,0,0), (1,1,self.player.rect.width-2,5)) # fill black
                pygame.draw.rect(self.image, Color('green'), (1,1,
                    int(self.player.rect.width * self.percent),5),0) # fill green
            self.oldpercent = self.percent
            self.rect.centerx = self.player.rect.centerx
            self.rect.centery = self.player.rect.centery - self.player.rect.height /2 - 20
            #check if player is still alive
            if not self.player.alive():
                self.kill() # kill the hitbar
        else:
            self.percent = self.monster.energy / 100.0
            if self.percent != self.oldpercent:
                pygame.draw.rect(self.image, (0,0,0), (1,1,self.monster.rect.width-2,5)) # fill black
                pygame.draw.rect(self.image, Color('green'), (1,1,
                    int(self.monster.rect.width * self.percent),5),0) # fill green
            self.oldpercent = self.percent
            self.rect.centerx = self.monster.rect.centerx
            self.rect.centery = self.monster.rect.centery - self.monster.rect.height /2 - 20
            #check if player is still alive
            if not self.monster.alive():
                self.kill() # kill the hitbar