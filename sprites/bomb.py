import pygame
from common.constant import Constant
from common.utils import Utils
from sprites.explosion import Explosion
import math
__author__ = 'tri'


class Bomb(pygame.sprite.Sprite):
    images = []

    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        folder = 'dan'
        self.player = player
        self.type_of_bullet = self.player.typeOfBullet
        player.enegery -= 25
        if self.type_of_bullet == 1:
            bullet_type = 'abc'
            x = 0
            y = 0
            width = 50
            height = 50
            self.power = 25
        else:
            bullet_type = 'bumerange'
            x = 0
            y = 0
            width = 50
            height = 50
            self.power = 15
            self.collide = 3

        image_source = Utils.my_load_image(folder,bullet_type+".png")
        j = 0
        self.image_frame = []
        while j < 8:
            if j < 4:
                self.image_frame.append(image_source.subsurface(j*width, y, width, height))
            else:
                self.image_frame.append(pygame.transform.flip(image_source.subsurface((j-4)*width, y, width, height),1,0))
            j+=1
        if player.direction > 0:
            self.frame = 0
        elif player.direction < 0:
            self.frame = 4
        self.image = self.image_frame[int(round(self.frame))]
        self.rect = self.image.get_rect(midbottom= (player.rect.centerx, player.rect.centery))
        self.origtop = self.rect.top
        self.speed_x = math.cos(math.radians(player.angle)) * player.power
        self.speed_y = -math.sin(math.radians(player.angle)) * player.power
        self.acceleration = Constant.GRAVITY
        self.t = 0
        self.startx = self.player.rect.centerx
        self.starty = self.player.rect.centery
        self.x = self.startx
        self.y = self.starty
        self.wallcollison = 0
    def update(self):
        self.t += 1.0/Constant.FPS
        #Detect collision
        if not self.type_of_bullet == 1:
            if self.rect.top <= 0:
                if self.collide == 1:
                    Utils.load_sound('boom.wav').play()
                    Explosion(self)
                    self.kill()
                else:
                    self.collide -= 1
                    self.startx = self.x
                    self.starty = self.y
                    self.speed_y = - (self.speed_y + self.acceleration *self.t)
                    self.rect.move_ip(0, 0 - self.rect.top + 1)
                    self.t = 0
                return
            elif self.rect.right >= Constant.SCREENRECT.right:
                if self.collide == 1:
                    Utils.load_sound('boom.wav').play()
                    Explosion(self)
                    self.kill()
                else:
                    self.collide -= 1
                    self.startx = self.x
                    self.starty = self.y
                    self.speed_x = -self.speed_x
                    self.speed_y += self.acceleration * self.t
                    self.rect.move_ip(Constant.SCREENRECT.right - self.rect.right - 1, 0)
                    self.t = 0
                return
            elif self.rect.left <= Constant.SCREENRECT.left:
                if self.collide == 1:
                    Utils.load_sound('boom.wav').play()
                    Explosion(self)
                    self.kill()
                else:
                    self.collide -= 1
                    self.startx = self.x
                    self.starty = self.y
                    self.speed_x = -self.speed_x
                    self.speed_y += self.acceleration * self.t
                    self.rect.move_ip(Constant.SCREENRECT.left - self.rect.left + 1, 0)
                    self.t = 0
                return
            elif self.rect.bottom >= 400: #400 la toa do truc y cua nen`
                if self.collide == 1:
                    Utils.load_sound('boom.wav').play()
                    Explosion(self)
                    self.kill()
                else:
                    self.collide -= 1
                    self.startx = self.x
                    self.starty = self.y
                    self.speed_y = - (self.speed_y + self.acceleration *self.t)
                    self.rect.move_ip(0, 400 - self.rect.bottom - 1)
                    self.t = 0
                return
        old_x = self.x
        old_y = self.y
        self.x = self.startx + self.speed_x * self.t
        self.y = self.starty + self.speed_y * self.t + self.acceleration/2.0* self.t* self.t
        self.rect.move_ip(self.x - old_x, self.y - old_y)


        if self.player.direction > 0:
            self.frame += 0.4
            if self.frame > 3:
                self.frame = 0
            self.image = self.image_frame[int(round(self.frame))]
        elif self.player.direction < 0:
            self.frame += 0.4
            if self.frame > 7:
                self.frame = 4
            self.image = self.image_frame[int(round(self.frame))]
        if self.type_of_bullet == 1 and not Constant.SCREENRECT.contains(self.rect):
            Utils.load_sound("boom.wav").play()
            Explosion(self)
            self.kill()