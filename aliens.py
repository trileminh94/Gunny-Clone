#!/usr/bin/env python

import random, os.path, math

#import basic pygame modules
import pygame
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
PLAYER1FIREKEY = K_SPACE


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

#load all sprite in list
def my_load_images(*file):
    imgs = []
    for file in files:
        imgs.append(my_load_image(file))
    return imgs

def load_images(*files):
    imgs = []
    for file in files:
        imgs.append(load_image(file))
    return imgs

#cut image to frame
def cut_frame(image):
    frame = []
    i = 0
    j = 0
    t = 0
    while j <= 2:
        frame.append(image.subsurface((i*114,j*90,110,90)))
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
    keydown = False
    fireAngle = 10
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
        self.image_frame = cut_frame(image_source)
        if self.direction > 0:
            self.image = self.image_frame[0]
        else:
            self.image = pygame.transform.flip(self.image_frame[0],0,0)
        self.rect = self.image.get_rect(midbottom=SCREENRECT.midbottom)
        self.origtop = self.rect.top

    def draw_move(self):
        self.frame = (self.frame + 0.2)
        if(self.direction > 0):
            print ' lon hon 0'
            self.image = self.image_frame[int(round(self.frame))%7]
        elif(self.direction < 0):
            print 'nho hon 0'
            self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))%7],1,0)
    
    def draw_throw(self):
        print 'draw throw'
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
        print 'draw lie'
        if(self.frame < 7 or self.frame > 10):
            self.frame = 7
        if(self.direction > 0):
            self.image = self.image_frame[int(round(self.frame))]
        elif(self.direction < 0):
            self.image = pygame.transform.flip(self.image_frame[int(round(self.frame))],1,0)
        self.frame+=self.stepChopMat
        if(self.frame > 10 or self.frame < 7):
            self.stepChopMat*=-1

    def update(self):
        if self.keydown == True:
            self.stepF+=1
            self.fireF = 10*math.fabs(math.sin(self.stepF*math.pi/math.pow(10,3)))
            print "f = " + str(self.fireF)
        else:
            self.stepF = 0
        if(self.state == LIE_STATE):
            self.draw_lie()
        elif(self.state == THROW_STATE):
            self.draw_throw()
        elif(self.state == MOVE_STATE):
            self.move(self.direction)

    # def draw_throw(self):
    #     if self.direction < 0:
    #         self.frame =  

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
        if direction:
            self.direction = direction
        if(self.isBlock == False):
            if(direction == 0 and fire == 0):
                self.state = LIE_STATE
            # elif(direction == 0 and fire == 1):
            #     self.state = THROW_STATE
            elif(direction != 0):
                self.state = MOVE_STATE


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
    speed = -11
    images = []
    def __init__(self, pos):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=pos)

    def update(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top <= 0:
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
    player1 = Player('nhan vat 1','character',-1)
    Alien() #note, this 'lives' because it goes into a sprite group
    if pygame.font:
        all.add(Score())


    while player1.alive():

        #get input
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return
            elif event.type == KEYDOWN:
                if event.key == PLAYER1FIREKEY:
                    player1.keydown = True
            elif event.type == KEYUP:
                if event.key == PLAYER1FIREKEY:
                    player1.keydown = False
                    player1.state = THROW_STATE

        keystate = pygame.key.get_pressed()

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        #update all the sprites
        all.update()

        #handle player input
        player1.check(keystate)
       

        # Create new alien
        if alienreload:
            alienreload = alienreload - 1
        elif not int(random.random() * ALIEN_ODDS):
            Alien()
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

        for alien in pygame.sprite.groupcollide(shots, aliens, 1, 1).keys():
            boom_sound.play()
            Explosion(alien)
            SCORE = SCORE + 1

        for bomb in pygame.sprite.spritecollide(player1, bombs, 1):
            boom_sound.play()
            Explosion(player1)
            Explosion(bomb)
            player1.kill()

        #draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        #cap the framerate
        clock.tick(40)

    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()



#call the "main" function if running this script
if __name__ == '__main__': main()

