#!/usr/bin/env python

import random, os.path, math

#import basic pygame modules
import pygame
import threading
import math
from pygame.locals import *

#see if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

#game constants
MAX_SHOTS      = 2      #most player bullets onscreen
ALIEN_ODDS     = 22     #chances a new alien appears
BOMB_ODDS      = 60    #chances a new bomb will drop
ALIEN_RELOAD   = 12     #frames between new aliens
SCREENRECT     = Rect(0, 0, 1000, 600)
SCORE          = 0
MOVE_STATE     = 1
LIE_STATE      = 2
THROW_STATE    = 3
COMPLAINT_STATE = 4
ANGRY_STATE    = 5
HEADACHE_STATE = 6
BORING_STATE   = 7
FIRE_EYE_STATE = 8
XFACE_STATE    = 9
CRYING_STATE   = 10
CRYING_CHONG_MAT = 11
BOTAY_STATE    = 12
STEP_EMOTION   = 0.08
FPS            = 60
RADIUS = 35
PLAYER1FIREKEY = K_SPACE
PLAYER1UPKEY   = K_UP
PLAYER1DOWNKey = K_DOWN
PLAYER1CHANGEBULLET = K_TAB
PLAYER1LEFTKEY = K_LEFT
PLAYER1RIGHTKEY = K_RIGHT

PLAYER2FIREKEY = K_x
PLAYER2UPKEY   = K_w
PLAYER2DOWNKey = K_s
PLAYER2CHANGEBULLET = K_CAPSLOCK
PLAYER2LEFTKEY = K_a
PLAYER2RIGHTKEY = K_d

MAXPOWER = 800
ACCELERATION = 200
POWERBARRECT1 = Rect(0, SCREENRECT.height - 25, 400, 20)
POWERBARRECT2 = Rect(SCREENRECT.width - 400, SCREENRECT.height - 25, 400, 20)
POWERBARCOLOR = (0, 255, 255)

main_dir = os.path.split(os.path.abspath(__file__))[0]

def load_image(file):
    "loads an image, prepares it for play"
    file = os.path.join(main_dir, 'data',file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert()

#load sprite from subfolder and file name 
#for each character
def my_load_image(subFolder,file):
    "loads an image, prepares it for play"
    folder = os.path.join(main_dir, 'image')
    file = os.path.join(folder, subFolder,file)
    try:
        surface = pygame.image.load(file)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s'%(file, pygame.get_error()))
    return surface.convert_alpha()

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

#cut image to frame
def cut_frame(image, x, y, width, length):
    frame = []
    i = 0
    j = 0
    t = 0
    while j <= 2:
        frame.append(image.subsurface((i*x,j*y,width,length)))
        t += 1
        i += 1
        if(i > 10 ):
            i = 0
            j += 1
    return frame

class dummysound:
    def play(self): pass

def load_sound(file):
    if not pygame.mixer: return dummysound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print ('Warning, unable to load, %s' % file)
    return dummysound()



# each type of game object gets an init and an
# update function. the update function is called
# once per frame, and it is when each object should
# change it's current position and state. the Player
# object actually gets a "move" function instead of
# update, since it is passed extra information about
# the keyboard


class Player(pygame.sprite.Sprite):
    speed = 1.5
    bounce = 24
    gun_offset = -11
    state = LIE_STATE
    isBlock = False
    stepChopMat = 0.08
    firedown = False
    angle = 30
    fireF = 0
    stepF = 0
    def __init__(self,folder,sprite_name,direction, whichplayer):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.reloading = 0
        self.frame = 0
        self.thow_frame = 24
        self.facing = direction
        self.direction = direction
        self.sound_change_radar = load_sound("bite.wav");
        self.sound_change_radar.set_volume(0.3)
        image_source = my_load_image(folder,sprite_name+".png")
        emotion_source = my_load_image(folder,sprite_name+"_emotion.png")
        self.image_frame = cut_frame(image_source, 114, 90, 110, 90)
        self.image_frame.extend(cut_frame(emotion_source,114,90,110,90))
        if self.direction > 0:
            self.image = self.image_frame[0]
        else:
            self.image = pygame.transform.flip(self.image_frame[0],0,0)

        self.rect = self.image.get_rect(midbottom=(SCREENRECT.midbottom[0], SCREENRECT.midbottom[1] - 100))

        self.origtop = self.rect.top
        self.health = 100
        self.angle = 45
        self.power = MAXPOWER * self.fireF
        self.typeOfBullet = 1
        self.whichplayer = whichplayer
        Livebar(self)
        Powerbar(self)

    def draw_move(self):
        self.frame = (self.frame + 0.2)
        if(self.direction > 0):
            self.image = self.image_frame[int(round(self.frame))%7]
        elif(self.direction < 0):
            self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))%7],1,0)
    
    def draw_throw(self):
        if(self.state == THROW_STATE):
            self.isBlock = True
            if(self.direction > 0):
                self.image = self.image_frame[int(round(self.thow_frame))]
            elif(self.direction < 0):
                self.image = pygame.transform.flip(self.image_frame[int(round(self.thow_frame))],1,0)
            self.thow_frame = self.thow_frame + 0.6
            if(self.thow_frame > 31):
                self.thow_frame = 17
            if(int(round(self.thow_frame))== 23):
                self.state == LIE_STATE
                self.isBlock = False

    def draw_lie(self):
        if(self.frame < 7 or self.frame > 10):
            self.frame = 7
        if(self.direction > 0):
            self.image = self.image_frame[int(round(self.frame))]
        elif(self.direction < 0):
            self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
        self.frame+=self.stepChopMat
        if(self.frame > 10 or self.frame < 7):
            self.stepChopMat*=-1

    def drawEmotion(self):
        self.isBlock = True
        if(self.direction > 0):
            if(self.state == COMPLAINT_STATE):
                if(self.frame < 33 or self.frame > 36):
                    self.frame = 33
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= STEP_EMOTION
                if(self.frame > 36):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == ANGRY_STATE):
                if(self.frame < 37 or self.frame > 40):
                    self.frame = 37
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= STEP_EMOTION
                if(self.frame > 40):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == HEADACHE_STATE):
                if(self.frame < 41 or self.frame > 43):
                    self.frame = 41
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= STEP_EMOTION
                if(self.frame > 43):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == BORING_STATE):
                if(self.frame < 44 or self.frame > 47):
                    self.frame = 44
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= STEP_EMOTION
                if(self.frame > 47):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == FIRE_EYE_STATE):
                if(self.frame < 48 or self.frame > 51):
                    self.frame = 48
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= STEP_EMOTION
                if(self.frame > 51):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == XFACE_STATE):
                if(self.frame < 52 or self.frame > 54):
                    self.frame = 52
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= STEP_EMOTION
                if(self.frame > 54):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == CRYING_STATE):
                if(self.frame < 55 or self.frame > 58):
                    self.frame = 55
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= STEP_EMOTION
                if(self.frame > 58):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == CRYING_CHONG_MAT):
                if(self.frame < 59 or self.frame > 62):
                    self.frame = 59
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= STEP_EMOTION
                if(self.frame > 62):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == BOTAY_STATE):
                if(self.frame < 63 or self.frame > 65):
                    self.frame = 63
                self.image = self.image_frame[int(round(self.frame))]
                self.frame+= STEP_EMOTION
                if(self.frame > 65):
                    self.state = LIE_STATE
                    self.isBlock = False
        elif(self.direction < 0):
            if(self.state == COMPLAINT_STATE):
                if(self.frame < 33 or self.frame > 36):
                    self.frame = 33
                pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= STEP_EMOTION
                if(self.frame > 36):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == ANGRY_STATE):
                if(self.frame < 37 or self.frame > 40):
                    self.frame = 37
                pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= STEP_EMOTION
                if(self.frame > 40):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == HEADACHE_STATE):
                if(self.frame < 41 or self.frame > 43):
                    self.frame = 41
                pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= STEP_EMOTION
                if(self.frame > 43):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == BORING_STATE):
                if(self.frame < 44 or self.frame > 47):
                    self.frame = 44
                pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= STEP_EMOTION
                if(self.frame > 47):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == FIRE_EYE_STATE):
                if(self.frame < 48 or self.frame > 51):
                    self.frame = 48
                pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= STEP_EMOTION
                if(self.frame > 51):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == XFACE_STATE):
                if(self.frame < 52 or self.frame > 54):
                    self.frame = 52
                pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= STEP_EMOTION
                if(self.frame > 54):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == CRYING_STATE):
                if(self.frame < 55 or self.frame > 58):
                    self.frame = 55
                pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= STEP_EMOTION
                if(self.frame > 58):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == CRYING_CHONG_MAT):
                if(self.frame < 59 or self.frame > 62):
                    self.frame = 59
                pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= STEP_EMOTION
                if(self.frame > 62):
                    self.state = LIE_STATE
                    self.isBlock = False
            elif(self.state == BOTAY_STATE):
                if(self.frame < 63 or self.frame > 65):
                    self.frame = 63
                pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
                self.frame+= STEP_EMOTION
                if(self.frame > 65):
                    self.state = LIE_STATE
                    self.isBlock = False


    def update(self):

        #change angle if player changes the direction
        if (self.direction  < 0 and self.angle < 90) or (self.direction > 0 and self.angle > 90):
            self.angle  = 180 - self.angle
        if self.firedown == True:
            self.stepF+= 0.5
            self.fireF = 10*math.fabs(math.sin(self.stepF*math.pi/math.pow(10,3)))
        else:
            self.stepF = 0
            self.fireF -= 10*math.fabs(math.sin(1*math.pi/math.pow(10,3)))
        self.power = MAXPOWER * self.fireF
        if(self.state == LIE_STATE):
            self.draw_lie()
        elif(self.state == THROW_STATE):
            self.draw_throw()
        elif(self.state == MOVE_STATE):
            self.move(self.direction)
        else:
            self.drawEmotion()
        self.drawRadar()

    def drawRadar(self):
        pos1 = (self.rect.centerx, self.rect.centery)
        pos2 = (pos1[0] + math.cos(math.radians(self.angle))*RADIUS, pos1[1]  - math.sin(math.radians(self.angle))*RADIUS)
        pygame.draw.line(self.screen, Color('yellow'), pos1, pos2, 2)
        if self.direction > 0:
            self.screen.blit(pygame.font.Font(None, 15).render(str(self.angle), True, Color('white')), (pos2[0], pos2[1] - 12 ))
        else:
            self.screen.blit(pygame.font.Font(None, 15).render(str(180 - self.angle), True, Color('white')), (pos2[0] - 18, pos2[1] - 12 ))
        #pygame.display.flip()



    def move(self, direction):
        if direction: 
            self.facing = direction
            self.draw_move()
        self.rect.move_ip(direction*self.speed, 0)
        self.rect = self.rect.clamp(SCREENRECT)
        self.rect.top = self.origtop - (self.rect.left//self.bounce%2)

    def gunpos(self):
        pos = self.facing*self.gun_offset + self.rect.centerx
        return pos, self.rect.top

    def check(self,keystate):
        if(self.whichplayer == 1):
            direction = keystate[PLAYER1RIGHTKEY] - keystate[PLAYER1LEFTKEY]
            fire = keystate[PLAYER1FIREKEY]
            up = keystate[PLAYER1UPKEY]
            down = keystate[PLAYER1DOWNKey]
        elif(self.whichplayer == 2):
            direction = keystate[PLAYER2RIGHTKEY] - keystate[PLAYER2LEFTKEY]
            fire = keystate[PLAYER2FIREKEY]
            up = keystate[PLAYER2UPKEY]
            down = keystate[PLAYER2DOWNKey]
        if direction:
            self.direction = direction
        if(self.isBlock == False):
            if(keystate[K_1] == 1):
                self.state = COMPLAINT_STATE
            elif(keystate[K_2] == 1):
                self.state = ANGRY_STATE
            elif(keystate[K_3] == 1):
                self.state = HEADACHE_STATE
            elif(keystate[K_4] == 1):
                self.state = BORING_STATE
            elif(keystate[K_5] == 1):
                self.state = FIRE_EYE_STATE
            elif(keystate[K_6] == 1):
                self.state = XFACE_STATE
            elif(keystate[K_7] == 1):
                self.state = CRYING_STATE
            elif(keystate[K_8] == 1):
                self.state = CRYING_CHONG_MAT
            elif(keystate[K_2] == 1):
                self.state = BOTAY_STATE
            elif(direction == 0 and fire == 0):
                self.state = LIE_STATE
            elif(direction != 0):
                self.state = MOVE_STATE
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

class Alien(pygame.sprite.Sprite):
    speed = 13
    animcycle = 12
    images = []
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1,1)) * Alien.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = SCREENRECT.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not SCREENRECT.contains(self.rect):
            self.facing = -self.facing;
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(SCREENRECT)
        self.frame = self.frame + 1
        self.image = self.images[self.frame//self.animcycle%3]


class Explosion(pygame.sprite.Sprite):
    defaultlife = 12
    animcycle = 3
    images = []
    def __init__(self, actor):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(center=actor.rect.center)
        self.life = self.defaultlife

    def update(self):
        self.life = self.life - 1
        self.image = self.images[self.life//self.animcycle%2]
        if self.life <= 0: self.kill()


class Shot(pygame.sprite.Sprite):
    speed = -5
    images = []
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        folder = 'dan'
        self.player = player
        if (player.typeOfBullet > 0):
            loaidan = 'abc'
            x = 0
            y = 0
            width = 50
            height = 50
        else:
            loaidan = 'bumerange'
            x = 0
            y = 0
            width = 50
            height = 50
            
        image_source = my_load_image(folder,loaidan+".png")
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
        self.speed_y = math.sin(math.radians(player.angle)) * player.power
        self.t = 0
        self.dx = 0
        self.dy = 0

    def update(self):
        self.t += 1.0/FPS
        x = self.dx
        y = self.dy
        self.dx = self.speed_x * self.t
        self.dy = self.speed_y * self.t - ACCELERATION/2.0* self.t* self.t
        self.rect.move_ip(self.dx - x, y - self.dy)
        
        if self.player.direction > 0:
            self.frame += 0.4 #72/FPS
            if self.frame > 3:
                self.frame = 0
            self.image = self.image_frame[int(round(self.frame))]
        elif self.player.direction < 0:
            self.frame += 0.4 #72/FPS
            if self.frame > 7:
                self.frame = 4
            self.image = self.image_frame[int(round(self.frame))]
        if not SCREENRECT.contains(self.rect):
            load_sound("boom.wav").play()
            self.kill()


class Bomb(pygame.sprite.Sprite):
    speed = 9
    images = []
    def __init__(self, alien):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=
                    alien.rect.move(0,5).midbottom)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom >= 470:
            Explosion(self)
            self.kill()


class Score(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = Color('white')
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        if SCORE != self.lastscore:
            self.lastscore = SCORE
            msg = "Score: %d" % SCORE
            self.image = self.font.render(msg, 0, self.color)
#TODO:
class Livebar(pygame.sprite.Sprite):
    """shows a bar with the hitpoints of a Bird sprite"""
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.player = player
        self.image = pygame.Surface((self.player.rect.width,7))
        self.image.set_colorkey((0,0,0)) # black transparent
        pygame.draw.rect(self.image, Color('green'), (0,0,self.player.rect.width,7),1)
        self.rect = self.image.get_rect()
        self.oldpercent = 0

    def update(self):
        self.percent = self.player.health / 100.0
        if self.percent != self.oldpercent:
            pygame.draw.rect(self.image, (0,0,0), (1,1,self.player.rect.width-2,5)) # fill black
            pygame.draw.rect(self.image, Color('green'), (1,1,
                int(self.player.rect.width * self.percent),5),0) # fill green
        self.oldpercent = self.percent
        self.rect.centerx = self.player.rect.centerx
        self.rect.centery = self.player.rect.centery - self.player.rect.height /2 - 10
        #check if player is still alive
        if not self.player.alive():
            self.kill() # kill the hitbar

class Powerbar(pygame.sprite.Sprite):
    """shows a bar with the hitpoints of a Bird sprite"""
    def __init__(self, player):
        pygame.sprite.Sprite.__init__(self, self.containers)
        if (player.whichplayer == 1):
            self.rect = POWERBARRECT1
        else:
            self.rect = POWERBARRECT2
        self.player = player
        self.image = pygame.Surface((self.rect.width,self.rect.height))
        self.image.set_colorkey((0,0,0)) # black transparent
        pygame.draw.rect(self.image, POWERBARCOLOR, (0, 0, self.rect.width,self.rect.height),1)
        self.oldpercent = 0

    def update(self):
        self.percent = self.player.fireF
        if self.percent != self.oldpercent:
            pygame.draw.rect(self.image, (0,0,0), (1,1,self.rect.width - 2,self.rect.height - 2)) # fill black
            if self.player.whichplayer == 1:
                pygame.draw.rect(self.image, POWERBARCOLOR, (1, 1, int(self.percent * self.rect.width) , self.rect.height - 2),0) # fill green
            else:
                pygame.draw.rect(self.image, POWERBARCOLOR, (1 + self.rect.width - int(self.percent * self.rect.width) , 1, int(self.percent * self.rect.width) , self.rect.height - 2),0) # fill green
        self.oldpercent = self.percent
        #check if player is still alive
        if not self.player.alive():
            self.kill()



#TODO : handling multithread keyboard input, need improvement
LOCK = threading.Lock()
def input(keystate, player1):
    shoot_sound = load_sound('2.wav')
    while True:
        keystate = pygame.key.get_pressed()
        LOCK.acquire()
        player1.check(keystate)
        fire = keystate[PLAYER1FIREKEY]
        if not player1.reloading and fire:
            Shot(player1.gunpos(), player1.angle, player1.power, player1.typeOfBullet)
            shoot_sound.play()
        player1.reloading = fire
        LOCK.release()

def main(winstyle = 0):
    # Initialize pygame
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None

    # Set the display mode
    winstyle = 0  # |FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    #Load images, assign to sprite classes
    #(do this before the classes are used, after screen setup)
    img = load_image('explosion1.gif')
    Explosion.images = [img, pygame.transform.flip(img, 1, 1)]
    Alien.images = load_images('alien1.gif', 'alien2.gif', 'alien3.gif')
    Bomb.images = [load_image('bomb.gif')]
    Shot.images = [load_image('shot.gif')]

    #decorate the game window
    icon = pygame.transform.scale(Alien.images[0], (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Pygame Aliens')
    pygame.mouse.set_visible(0)

    #create the background, tile the bgd image
    bgdtile = load_image('back.jpg')
    background = pygame.Surface(SCREENRECT.size)
    for x in range(0, SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0,0))
    pygame.display.flip()

    #load the sound effects
    boom_sound = load_sound('boom.wav')
    shoot_sound = load_sound('1.wav')
    if pygame.mixer:
        music = os.path.join(main_dir, 'data', '1037.wav')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

    # Initialize Game Groups
    aliens = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    lastalien = pygame.sprite.GroupSingle()

    #assign default groups to each sprite class
    Player.containers = all
    Player.screen = screen
    
    Alien.containers = aliens, all, lastalien
    Bomb.containers = bombs, all
    Explosion.containers = all
    Score.containers = all
    Livebar.containers = all
    Powerbar.containers = all

    #Create Some Starting Values
    global score
    alienreload = ALIEN_RELOAD
    kills = 0
    clock = pygame.time.Clock()

    #initialize our starting sprites
    global SCORE
#<<<<<<< HEAD
    player1 = Player('nhan vat 1','character1',-1, 1)
    player2 = Player('nhan vat 2','character2',-1, 2)
    shots = pygame.sprite.Group()
    Shot.containers = shots, all
#=======

    #player1 = Player('nhan vat 1','character1',-1, 1)
    #Alien() #note, this 'lives' because it goes into a sprite group
#>>>>>>> b6e13de9173c656016d3e59b8d7b01618c56b21a

    if pygame.font:
        all.add(Score())
   
    while player1.alive():
        #get input
        player1downToUp = player1.firedown
        player2downToUp = player2.firedown
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return
            elif event.type == KEYDOWN:
                if event.key == PLAYER1FIREKEY:
                    player1.firedown = True
                elif event.key == PLAYER1CHANGEBULLET:
                    player1.typeOfBullet *= -1
                if event.key == PLAYER2FIREKEY:
                    player2.firedown = True
                elif event.key == PLAYER2CHANGEBULLET:
                    player2.typeOfBullet *= -1
            elif event.type == KEYUP:
                if event.key == PLAYER1FIREKEY:
                    player1.firedown = False
                    player1.state = THROW_STATE
                if event.key == PLAYER2FIREKEY:
                    player2.firedown = False
                    player2.state = THROW_STATE

        # clear/erase the last drawn sprites
        all.clear(screen, background)
        screen.blit(background, (0,0))

        #update all the sprites
        all.update()

        #handle player input
        keystate = pygame.key.get_pressed()
        player1.check(keystate)
        player2.check(keystate)
        if player1downToUp and not player1.firedown:
            Shot(player1)
            shoot_sound.play()
            shoot_sound.play()
            shoot_sound.play()
        if player2downToUp and not player2.firedown:
            Shot(player2)
            shoot_sound.play()
            shoot_sound.play()
            shoot_sound.play()
        # Create new alien
        if alienreload:
            alienreload = alienreload - 1
        elif not int(random.random() * ALIEN_ODDS):
            #Alien()
            alienreload = ALIEN_RELOAD

        # Drop bombs
        if lastalien and not int(random.random() * BOMB_ODDS):
            Bomb(lastalien.sprite)

        # Detect collisions
        for alien in pygame.sprite.spritecollide(player1, aliens, 1):
            boom_sound.play()
            Explosion(alien)
            Explosion(player1)
            SCORE = SCORE + 1
            player1.kill()
        #LOCK.acquire()
        for alien in pygame.sprite.groupcollide(shots, aliens, 1, 1).keys():
            boom_sound.play()
            Explosion(alien)
            SCORE = SCORE + 1
        #LOCK.release()
        for bomb in pygame.sprite.spritecollide(player1, bombs, 1):
            boom_sound.play()
            Explosion(player1)
            Explosion(bomb)
            player1.kill()

        # drawAiming(screen, player1)

        dirty = all.draw(screen) # draw all sprite, return list of rect
        pygame.display.update(dirty) # draw only changed rect
        #cap the framerate
        clock.tick(FPS)

    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()



#call the "main" function if running this script
if __name__ == '__main__': main()

