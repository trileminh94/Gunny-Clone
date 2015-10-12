import pygame
from pygame.locals import *

import pygbutton
from common.constant import Constant
from common.utils import Utils
from sprites.ground import Ground
from sprites.explosion import Explosion
from sprites.bomb import Bomb
from sprites.energy_bar import Energy_bar
from sprites.power_bar import Power_bar
from sprites.live_bar import Live_bar
from sprites.player import Player
from sprites.screeps.basic_creep import BasicCreep
from sprites.screeps.creep_a import CreepA
from sprites.screeps.creep_b import CreepB
from sprites.screeps.creep_c import CreepC
from sprites.screeps.creep_d import CreepD
from sprites.screeps.creep_e import CreepE
from sprites.screeps.creep_f import CreepF

# See if we can load more than standard BMP
if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")
    
def home(game_state):
    # Initialize pygame
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print ('Warning, no sound')
        pygame.mixer = None

    # Set the display mode
    win_style = 0  # FULL SCREEN
    best_depth = pygame.display.mode_ok(Constant.SCREENRECT.size, win_style, 32)
    screen = pygame.display.set_mode(Constant.SCREENRECT.size, win_style, best_depth)

    pygame.display.set_caption('Gunny')
    pygame.mouse.set_visible(1)

    # Create the background, tile the bgd image
    bg_title = Utils.load_image('home_back.jpg')
    background = pygame.Surface(Constant.SCREENRECT.size)
    for x in range(0, Constant.SCREENRECT.width, bg_title.get_width()):
        background.blit(bg_title, (x, 0))

    button_obj = pygbutton.PygButton((300, 400, 100, 40), 'Play')

    while game_state == Constant.HOME:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            if 'click' in button_obj.handleEvent(event):
                game_state = Constant.GAME
                if game_state == Constant.GAME:
                    main(screen)
        if game_state == Constant.HOME:
            screen.blit(background, (0, 0))
            button_obj.draw(background)
            pygame.display.flip()


def game_over(screen, gamestate):
    pygame.mouse.set_visible(1)

    # #create the background, tile the bgd image
    bgdtile = Utils.load_image('gameover_back.jpg')
    background = pygame.Surface(Constant.SCREENRECT.size)
    for x in range(0, Constant.SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))

    playagain = pygbutton.PygButton((380, 400, 100, 40), 'Play again')
    quit = pygbutton.PygButton((520, 400, 100, 40), 'Quit')

    while gamestate == Constant.GAMEOVER:
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            if 'click' in playagain.handleEvent(event):
                gamestate = Constant.GAME
                if gamestate == Constant.GAME:
                    main(screen,gamestate)
            if 'click' in quit.handleEvent(event):
                if pygame.mixer:
                    pygame.mixer.music.fadeout(1000)
                pygame.time.wait(1000)
                pygame.quit()
        screen.blit(background, (0,0))
        playagain.draw(background)
        quit.draw(background)
        pygame.display.flip()


def main(screen):
    img = Utils.load_image('explosion1.gif')
    Explosion.images = [img, pygame.transform.flip(img, 1, 1)]

    pygame.mouse.set_visible(0)

    # Create the background, tile the bgd image
    bgdtile = Utils.load_image('back.jpg')
    background = pygame.Surface(Constant.SCREENRECT.size)
    for x in range(0, Constant.SCREENRECT.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Load the sound effects
    boom_sound = Utils.load_sound('boom.wav')
    shoot_sound = Utils.load_sound('1.wav')
    if pygame.mixer:
        music = 'resources/data/1037.wav'
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

    # Initialize Game Groups

    bombs = pygame.sprite.Group()
    all_group = pygame.sprite.OrderedUpdates()
    creeps = pygame.sprite.Group()

    # Assign default groups to each sprite class
    Ground.containers = all_group
    Player.containers = all_group
    BasicCreep.containers = all_group, creeps
    Player.screen = screen

    Bomb.containers = bombs, all_group
    Explosion.containers = all_group

    Live_bar.containers = all_group
    Energy_bar.containers = all_group
    Power_bar.containers = all_group

    # Create Some Starting Values
    # Global score

    clock = pygame.time.Clock()

    ground = Ground()
    player = Player('nhan vat 1', 'character1', 1, 1, 350)

    #*************************************
    # Init creeps
    #*************************************
    BasicCreep.screen = screen
    CreepB(200, 200, 0).down_able = False
    #CreepA(500, 200, 1).down_able = False
    CreepC(300, 100, 1).down_able = False
    CreepD(250, 300, 0).down_able = False
    #CreepE(800, 300, 1).down_able = False
    CreepF(600, 150, 1).down_able = False

    while player.health > -10:
        if player.state == Constant.DIE_STATE:
            player.health -= 0.1

        # Get input
        player1_down_to_up = player.fire_down

        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return
            elif event.type == KEYDOWN:
                if event.key == Constant.PLAYER1FIREKEY:
                    player.fire_down = True
                elif event.key == Constant.PLAYER1CHANGEBULLET:
                    player.typeOfBullet *= -1
            elif event.type == KEYUP:
                if event.key == Constant.PLAYER1FIREKEY:
                    player.fire_down = False
                    if player.enegery >= 20:
                        player.state = Constant.THROW_STATE

        # Clear/erase the last drawn sprites

        all_group.clear(screen, background)
        screen.blit(background, (0, 0))

        # Update all the sprites
        all_group.update()

        # Handle player input
        key_state = pygame.key.get_pressed()
        player.check(key_state)

        if player1_down_to_up and not player.fire_down and player.enegery >= 25:
            Bomb(player)
            shoot_sound.play()

        for bomb in pygame.sprite.spritecollide(player, bombs, False):
            if bomb.player.whichplayer == 2:
                boom_sound.play()
                Explosion(player)
                player.lost_blood(bomb.power)
                bomb.kill()

        # Detect collision with ground
        for bomb in pygame.sprite.spritecollide(ground, bombs, False):
            if bomb.type_of_bullet == 1:
                boom_sound.play()
                Explosion(bomb)
                bomb.kill()

        if pygame.sprite.spritecollide(player, creeps, False):
            player.lost_blood(1000)
        #*****************************
        # CHECK OBJECTS CAN MOVE DOWN
        #*****************************


        if pygame.sprite.collide_mask(player, ground):
            player.downable = False


        dirty = all_group.draw(screen)  # Draw all sprite, return list of rect
        pygame.display.update(dirty)    # Draw only changed rect
        # Cap the frame rate
        clock.tick(Constant.FPS)
    game_state = Constant.GAMEOVER

    game_over(screen, game_state)

# Call the "main" function if running this script
if __name__ == '__main__':
    home(Constant.HOME)
