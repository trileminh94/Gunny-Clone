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
FPS            = 40
RADIUS = 100
PLAYER1FIREKEY = K_SPACE
PLAYER1UPKEY   = K_UP
PLAYER1DOWNKey = K_DOWN
PLAYER1CHANGEBULLET = K_TAB
ACCELERATION = 100

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
    heath = 100
    state = LIE_STATE
    isBlock = False
    stepChopMat = 0.08
    firedown = False
    angle = 30
    fireF = 0
    stepF = 0
    def __init__(self,folder,sprite_name,direction):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.reloading = 0
        self.frame = 0
        self.thow_frame = 24
        self.facing = direction
        self.direction = direction
        image_source = my_load_image(folder,sprite_name+".png")
        self.image_frame = cut_frame(image_source, 114, 90, 110, 90)
        if self.direction > 0:
            self.image = self.image_frame[0]
        else:
            self.image = pygame.transform.flip(self.image_frame[0],0,0)
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.origtop = self.rect.top
        self.angle = 45
        self.power = 200
        self.typeOfBullet = 1

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

    # def draw_direction(self,surface):
    #     pygame.draw.line(surface,Color("yellow"),(20,20),(20 + 20*math.cos(self.angle*math.pi/180),20 - 20*math.sin(self.angle*math.pi/180)),3)


    def update(self):
        #pygame.display.update(pygame.Rect(20,0,40,20))<<<<<<<<<<<<<<<<<<<<<----------------------------
        if self.firedown == True:
            self.stepF+=1
            #self.fireF = 10*math.fabs(math.sin(self.stepF*math.pi/math.pow(10,2)))
            self.fireF = 10*math.fabs(math.sin(self.stepF*math.pi/math.pow(10,3)))
        else:
            self.stepF = 0
        if(self.state == LIE_STATE):
            self.draw_lie()
        elif(self.state == THROW_STATE):
            self.draw_throw()
        elif(self.state == MOVE_STATE):
            self.move(self.direction)
        #self.draw_direction(self.image)


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

    def heath(self):
        return self.heath

    def check(self,keystate):
        direction = keystate[K_RIGHT] - keystate[K_LEFT]
        fire = keystate[K_SPACE]
        up = keystate[PLAYER1UPKEY]
        down = keystate[PLAYER1DOWNKey]
        if keystate[PLAYER1CHANGEBULLET]:
            self.typeOfBullet *= -1
        if direction:
            self.direction = direction
        if(self.isBlock == False):
            if(direction == 0 and fire == 0):
                self.state = LIE_STATE
            elif(direction != 0):
                self.state = MOVE_STATE
            if up != 0:
                if self.angle < 90:
                    self.angle += 1

            elif down != 0:
                if self.angle > 0:
                    self.angle -= 1
            pygame.event.pump()

# class dead(pygame.sprite.Sprite):

#     def __init__(self):
#         pygame.sprite.Sprite.__init__(self,self.containers)

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
    def __init__(self,pos, angle, power, typeOfBullet):
        pygame.sprite.Sprite.__init__(self, self.containers)
        folder = 'dan'
        if (typeOfBullet > 0):
            loaidan = 'phitieu'
            x = 0
            y = 0
            width = 40
            height = 41
        else:
            loaidan = 'bumerang'
            x = 0
            y = 0
            width = 33
            height = 34

        image_source = my_load_image(folder,loaidan+".png")
        image = image_source.subsurface(x, y, width, height)
        j = 0
        self.image_frame = []
        while j <= 36:
            self.image_frame.append(pygame.transform.rotate(image, 10 * j))
            j += 1
        self.frame = 0
        self.image = self.image_frame[int(round(self.frame))]
        self.rect = self.image.get_rect(midbottom=pos)
        self.origtop = self.rect.top
        self.speed_x = math.cos(math.radians(angle)) * power
        self.speed_y = math.sin(math.radians(angle)) * power
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
        self.frame += 72/FPS
        if self.frame > 36:
            self.frame = 0
        self.image = self.image_frame[int(round(self.frame))]
        if not SCREENRECT.contains(self.rect):
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

#TODO : handling multithread keyboard input, need improvement
LOCK = threading.Lock()
def input(keystate, player1):
    shoot_sound = load_sound('car_door.wav')
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
    shoot_sound = load_sound('car_door.wav')
    if pygame.mixer:
        music = os.path.join(main_dir, 'data', 'house_lo.wav')
        pygame.mixer.music.load(music)
        #pygame.mixer.music.play(-1)

    # Initialize Game Groups
    aliens = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    lastalien = pygame.sprite.GroupSingle()

    #assign default groups to each sprite class
    Player.containers = all
    Alien.containers = aliens, all, lastalien
    Shot.containers = shots, all
    Bomb.containers = bombs, all
    Explosion.containers = all
    Score.containers = all

    #Create Some Starting Values
    global score
    alienreload = ALIEN_RELOAD
    kills = 0
    clock = pygame.time.Clock()

    #initialize our starting sprites
    global SCORE
# <<<<<<< HEAD
#     player1 = Player('nhan vat 1','character1',-1)
#     Alien() #note, this 'lives' because it goes into a sprite group
# =======
    player1 = Player('nhan vat 1','character',-1)
    #Alien() #note, this 'lives' because it goes into a sprite group
# >>>>>>> origin/luan
    if pygame.font:
        all.add(Score())
    #keystate = 0
    #threading._start_new_thread(input, (keystate, player1))
    while player1.alive():
        #get input
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return
            elif event.type == KEYDOWN:
                if event.key == PLAYER1FIREKEY:
                    player1.firedown = True
            elif event.type == KEYUP:
                if event.key == PLAYER1FIREKEY:
                    player1.firedown = False
                    player1.state = THROW_STATE

        # clear/erase the last drawn sprites
        all.clear(screen, background)
        screen.blit(background, (0,0))

        #update all the sprites
        all.update()

        #handle player input
        keystate = pygame.key.get_pressed()
        player1.check(keystate)
        fire = keystate[PLAYER1FIREKEY]
        if not player1.reloading and fire:
            Shot((player1.rect.centerx, player1.rect.centery), player1.angle, player1.power, player1.typeOfBullet)
            shoot_sound.play()
        player1.reloading = fire
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
        #draw the scene
        pos1 = (player1.rect.centerx, player1.rect.centery)
        pos2 = (pos1[0] + math.cos(math.radians(player1.angle))*RADIUS, pos1[1]  - math.sin(math.radians(player1.angle))*RADIUS)
        #print pos1, pos2
        pygame.draw.line(screen, Color('black'), pos1, pos2, 2)
        pygame.draw.arc(screen,Color('black'),Rect(pos1[0] - RADIUS, pos1[1] - RADIUS, 2 * RADIUS, 2 * RADIUS), 0, math.pi/2 ,1)
        screen.blit(pygame.font.Font(None, 25).render(str(player1.angle), True, Color('red')), (pos2[0], pos2[1] - 12 ))
        pygame.display.flip()
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

