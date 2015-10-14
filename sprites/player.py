import pygame
from common.constant import Constant
from common.utils import Utils
from sprites.live_bar import Live_bar
from sprites.power_bar import Power_bar
from sprites.energy_bar import Energy_bar

import math
from random import randint
from pygame.locals import *
from common.e_bullet_type import EBulletType
__author__ = 'tri'


class Player(pygame.sprite.Sprite):
    speed = 5
    bounce = 24
    gun_offset = -11
    state = Constant.LIE_STATE
    isBlock = False
    stepChopMat = 0.08
    fire_down = False
    angle = 30
    fireF = 0
    stepF = 0
    downable = True
    isBlockByWall = False
    jump = 0
    screen = None
    def __init__(self, folder, sprite_name, direction, whichplayer, offset):

        pygame.sprite.Sprite.__init__(self, self.containers)
        self.reloading = 0
        self.frame = 0
        self.thow_frame = 24
        self.facing = direction
        self.direction = direction
        self.sound_change_radar = Utils.load_sound("bite.wav");
        self.sound_change_radar.set_volume(0.3)
        image_source = Utils.my_load_image(folder, sprite_name+".png")
        emotion_source = Utils.my_load_image(folder, sprite_name+"_emotion.png")
        if whichplayer == 1:
            self.image_frame = Utils.cut_frame(image_source, 114, 90, 110, 90)
            self.image_frame.extend(Utils.cut_frame(emotion_source,114,90,110,90))
        else:
            self.image_frame = Utils.cut_frame(image_source, 114, 85, 110, 98)
            self.image_frame.extend(Utils.cut_frame(emotion_source,114,85,110,98))

        if self.direction > 0:
            self.image = self.image_frame[0]
        else:
            self.image = pygame.transform.flip(self.image_frame[0],0,0)

        self.rect = self.image.get_rect()
        self.rect = self.rect.inflate(-30, -25)
        self.rect.move_ip(250, 0)
        self.pos = [self.rect.left + 25 , self.rect.top + 20]
        self.origtop = self.rect.top
        self.health = 100
        self.angle = 45
        self.power = Constant.MAXPOWER * self.fireF
        self.typeOfBullet = EBulletType.BASIC
        self.moveWithScreen = False
        self.mask = pygame.mask.from_surface(self.image)
        self.whichplayer = whichplayer
        self.enegery = 100
        Live_bar(self)
        Energy_bar(self)
        Power_bar(self)

    def lost_blood(self, power):
        self.health-= power
        if(self.health <= 0):
            self.state = Constant.DIE_STATE
        else:
            if(randint(5,12) == 5):
                self.state = Constant.ANGRY_STATE
            elif(randint(5,12) == 6):
                self.state = Constant.HEADACHE_STATE
            elif(randint(5,12) == 7):
                self.state = Constant.BORING_STATE
            elif(randint(5,12) == 8):
                self.state = Constant.FIRE_EYE_STATE
            elif(randint(5,12) == 9):
                self.state = Constant.XFACE_STATE
            elif(randint(5,12) == 10):
                self.state = Constant.CRYING_STATE
            elif(randint(5,12) == 11):
                self.state = Constant.CRYING_CHONG_MAT
            elif(randint(5,12) == 12):
                self.state = Constant.BOTAY_STATE


    def draw_move(self):
        """
        Just draw sprites
        :return:
        """
        self.frame = (self.frame + 0.2)
        if(self.direction > 0):
            self.image = self.image_frame[int(round(self.frame))%7]
        elif(self.direction < 0):
            self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))%7],1,0)

    def draw_throw(self):
        if(self.state == Constant.THROW_STATE):
            self.isBlock = True
            if(self.direction > 0):
                self.image = self.image_frame[int(round(self.thow_frame))]
            elif(self.direction < 0):
                self.image = pygame.transform.flip(self.image_frame[int(round(self.thow_frame))],1,0)
            self.thow_frame = self.thow_frame + 0.6
            if(self.thow_frame > 31):
                self.thow_frame = 17
            if(int(round(self.thow_frame))== 23):
                self.state == Constant.LIE_STATE
                self.isBlock = False

    def draw_lie(self):
        if self.frame < 7 or self.frame > 10:
            self.frame = 7
        if self.direction > 0:
            self.image = self.image_frame[int(round(self.frame))]
        elif self.direction < 0:
            self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))], 1, 0)
        self.frame+=self.stepChopMat
        if self.frame > 10 or self.frame < 7:
            self.stepChopMat*=-1

    def drawEmotion(self):
        self.isBlock = True
        if(self.direction > 0):
            if(self.state == Constant.COMPLAINT_STATE):
                if(self.frame < 33 or self.frame > 36):
                    self.frame = 33
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 36):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.ANGRY_STATE):
                if(self.frame < 37 or self.frame > 40):
                    self.frame = 37
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 40):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.HEADACHE_STATE):
                if(self.frame < 41 or self.frame > 43):
                    self.frame = 41
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 43):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.BORING_STATE):
                if(self.frame < 44 or self.frame > 47):
                    self.frame = 44
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 47):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.FIRE_EYE_STATE):
                if self.frame < 48 or self.frame > 51:
                    self.frame = 48
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 51):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.XFACE_STATE):
                if(self.frame < 52 or self.frame > 54):
                    self.frame = 52
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 54):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.CRYING_STATE):
                if(self.frame < 55 or self.frame > 58):
                    self.frame = 55
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 58):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.CRYING_CHONG_MAT):
                if(self.frame < 59 or self.frame > 62):
                    self.frame = 59
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 62):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.BOTAY_STATE):
                if(self.frame < 63 or self.frame > 65):
                    self.frame = 63
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 65):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
        elif(self.direction < 0):
            if(self.state == Constant.COMPLAINT_STATE):
                if(self.frame < 33 or self.frame > 36):
                    self.frame = 33
                self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 36):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.ANGRY_STATE):
                if(self.frame < 37 or self.frame > 40):
                    self.frame = 37
                self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 40):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.HEADACHE_STATE):
                if(self.frame < 41 or self.frame > 43):
                    self.frame = 41
                self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 43):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.BORING_STATE):
                if(self.frame < 44 or self.frame > 47):
                    self.frame = 44
                self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 47):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.FIRE_EYE_STATE):
                if(self.frame < 48 or self.frame > 51):
                    self.frame = 48
                self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 51):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.XFACE_STATE):
                if(self.frame < 52 or self.frame > 54):
                    self.frame = 52
                self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 54):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.CRYING_STATE):
                if(self.frame < 55 or self.frame > 58):
                    self.frame = 55
                self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 58):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.CRYING_CHONG_MAT):
                if(self.frame < 59 or self.frame > 62):
                    self.frame = 59
                self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 62):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False
            elif(self.state == Constant.BOTAY_STATE):
                if(self.frame < 63 or self.frame > 65):
                    self.frame = 63
                self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= Constant.STEP_EMOTION
                if(self.frame > 65):
                    self.state = Constant.LIE_STATE
                    self.isBlock = False

    def update(self):
        if self.enegery < 100:
            self.enegery += 0.05
        if self.state == Constant.DIE_STATE:
            self.frame = 32
            self.image = self.image_frame[self.frame]
        else:
            # change angle if player changes the direction
            if (self.direction  < 0 and self.angle < 90) or (self.direction > 0 and self.angle > 90):
                self.angle  = 180 - self.angle
            if self.fire_down == True:
                self.stepF+= 0.5
                self.fireF = 10*math.fabs(math.sin(self.stepF*math.pi/math.pow(10,3)))
            else:
                self.stepF = 0
                self.fireF -= 10*math.fabs(math.sin(1*math.pi/math.pow(10,3)))
            self.power = Constant.MAXPOWER * self.fireF + 100
            if(self.state == Constant.LIE_STATE):
                self.draw_lie()
            elif(self.state == Constant.THROW_STATE):
                self.draw_throw()
            elif(self.state == Constant.MOVE_STATE):

                if not self.isBlockByWall:
                    self.move(self.direction)
            else:
                self.drawEmotion()
            self.drawRadar()


            if self.jump > 0:
                self.rect.move_ip(0, - Constant.JUMPPERFRAME)
                self.pos[1] -= Constant.JUMPPERFRAME
                self.jump -= 1
            elif self.downable:

                self.rect.move_ip(0, Constant.DOWNPERFRAME)
                self.pos[1] += Constant.DOWNPERFRAME
        pygame.draw.rect(Player.screen, 0x000000, self.rect)

    def drawRadar(self):
        pos1 = (self.rect.centerx, self.rect.centery)
        pos2 = (pos1[0] + math.cos(math.radians(self.angle))*Constant.RADIUS, pos1[1]  - math.sin(math.radians(self.angle))*Constant.RADIUS)
        pygame.draw.line(self.screen, Color('yellow'), pos1, pos2, 2)
        if self.direction > 0:
            self.screen.blit(pygame.font.Font(None, 15).render(str(self.angle), True, Color('white')), (pos2[0], pos2[1] - 12 ))
        else:
            self.screen.blit(pygame.font.Font(None, 15).render(str(180 - self.angle), True, Color('white')), (pos2[0] - 18, pos2[1] - 12 ))

    def move(self, direction):
        if direction:
            self.facing = direction
            self.draw_move()

        if self.moveWithScreen:
            self.rect.move_ip(direction*self.speed, 0)
        self.rect = self.rect.clamp(Rect(-20, 0, Constant.SCREENRECT.width + 40, Constant.SCREENRECT.height))

    def check(self,keystate):
        if(self.state != Constant.DIE_STATE):
            if(self.whichplayer == 1):
                direction = keystate[Constant.PLAYER1RIGHTKEY] - keystate[Constant.PLAYER1LEFTKEY]
                fire = keystate[Constant.PLAYER1FIREKEY]
                up = keystate[Constant.PLAYER1UPKEY]
                down = keystate[Constant.PLAYER1DOWNKey]

            elif(self.whichplayer == 2):
                direction = keystate[Constant.PLAYER2RIGHTKEY] - keystate[Constant.PLAYER2LEFTKEY]
                fire = keystate[Constant.PLAYER2FIREKEY]
                up = keystate[Constant.PLAYER2UPKEY]
                down = keystate[Constant.PLAYER2DOWNKey]
            if direction:
                self.direction = direction

            if(self.isBlock == False):
                if(direction == 0 and fire == 0):
                    self.state = Constant.LIE_STATE
                elif(direction != 0):
                    self.state = Constant.MOVE_STATE
                if up != 0:
                    if self.angle < 90:
                        self.angle += 1
                    else:
                        self.angle -= 1
                    self.sound_change_radar.play()
                elif down != 0:
                    if self.angle > 0 and self.angle <= 90:
                        self.angle -= 1
                    elif self.angle > 90 and self.angle <180:
                        self.angle += 1
                    self.sound_change_radar.play()
                pygame.event.pump()