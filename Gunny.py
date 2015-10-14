import pygame
from pygame.locals import *
import pygbutton
from common.constant import Constant
from common.utils import Utils
from sprites.ground import Ground
from sprites.explosion import Explosion
from sprites.bullet import Bullet
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
from sprites.screeps.creep_a_special import CreepASpecial
from sprites.item.coreItem import coreItem


from sprites.item.money import money
from sprites.item.magic_box import magicbox
from sprites.item.bumerange import bumerange
from sprites.item.monster import monster
from sprites.item.berry import berry

from sprites.creep_manager import CreepManager

from sprites.tile import TileCache
from sprites.tile import Tile
from common.e_bullet_type import EBulletType
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

def game_over(screen,gamestate):
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
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    return
            if 'click' in playagain.handleEvent(event):
                gamestate = Constant.GAME
                if(gamestate == Constant.GAME):
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
    background = pygame.image.load("resources\image\TileSet\\background.png").convert()

    # Load the sound effects
    boom_sound = Utils.load_sound('boom.wav')
    shoot_sound = Utils.load_sound('1.wav')
    if pygame.mixer:
        music = 'resources/data/1037.wav'
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)

    # Initialize Game Groups
    aliens = pygame.sprite.Group()
    bombs = pygame.sprite.Group()
    render_group = pygame.sprite.OrderedUpdates()
    creeps = pygame.sprite.Group()
    items = pygame.sprite.Group()

    # Assign default groups to each sprite class

    # Ground.containers = all_group
    # Player.containers = all_group
    # BasicCreep.containers = all_group, creeps
    coreItem.containers = render_group

    Player.containers = render_group
    Player.screen = screen

    BasicCreep.containers = creeps, render_group
    Bullet.containers = bombs, render_group
    Explosion.containers = render_group

    Live_bar.containers = render_group
    Energy_bar.containers = render_group
    Power_bar.containers = render_group

    # Create Some Starting Values
    # Global score

    clock = pygame.time.Clock()


    #ground = Ground()
    player = Player('nhan vat 1', 'character1', 1, 1, 350)

    #*************************************
    # Init creeps
    #*************************************
    BasicCreep.screen = screen
    Player.screen = screen
    #*************************************
    # Init item
    #*************************************
    item1 = money(100,100,"money")
    print "xong item1"
    item2 = bumerange(200,100,"bumerange_tree")
    print "xong item2"
    item3 = magicbox(300,100,"magic_box")
    print "xong item3"
    item4 = monster(400,100,"monster")
    #item5 = berry(500,100,"berry")

    items.add(item1)
    items.add(item2)
    items.add(item3)
    items.add(item4)
    #items.add(item5)


    # CreepManager.create_creep(creeps, 'A', 365, 332, 365, 510, 0, 1)
    # CreepManager.create_creep(creeps, 'A', 611, 332, 576, 989, 0, 1)
    # CreepManager.create_creep(creeps, 'A', 874, 332, 576, 989, 1, 1)
    # CreepManager.create_creep(creeps, 'D', 1472+10, 316-50, 1472+10, 1588, 1, 1)
    # CreepManager.create_creep(creeps, 'D', 1218+10, 380-50, 1218+10, 1374, 1, 1)
    #
    # CreepManager.create_creep(creeps, 'B', 1280+20, 508-30, 1280+20, 1374-20, 1, 1)
    # CreepManager.create_creep(creeps, 'B', 1474+20, 508-30, 1474+20, 1628-50, 1, 1)
    # CreepManager.create_creep(creeps, 'B', 1664+45, 508-30, 1664+45, 1782-20, 1, 1)
    #
    # CreepManager.create_creep(creeps, 'A', 2592+45, 442-48, 2592+45, 2876-20, 1, 1)
    # CreepManager.create_creep(creeps, 'F', 2592+45, 100, 2592+45, 2876-20, 1, 4)
    #
    # CreepManager.create_creep(creeps, 'B', 3302+45, 442 - 30, 3302+45-20, 3548-20, 1, 2)
    # CreepManager.create_creep(creeps, 'F', 3312+45, 300, 3302+45-20, 3548-20, 1, 4)
    # CreepManager.create_creep(creeps, 'F', 3400, 200, 3302+45-20, 3548-20, 0, 3)
    # CreepManager.create_creep(creeps, 'F', 3390, 70, 3302+45-20, 3548-20, 0, 3)
    #
    # CreepManager.create_creep(creeps, 'A', 3840+55, 442 - 15, 3840+50, 4000-20-20, 0, 1)
    #
    # CreepManager.create_creep(creeps, 'A', 4706+55, 362, 4706, 4862-20, 0, 1)
    #
    # CreepManager.create_creep(creeps, 'C', 5365, 162, 5365, 6000, 0, 4)
    # CreepManager.create_creep(creeps, 'C', 5365, 62, 5365, 6000, 0, 4)
    #
    # CreepManager.create_creep(creeps, 'B', 6505, 316, 6505, 6645, 0, 4)

    CreepManager.create_creep(creeps, 'A_SPECIAL', 4917, 382, 4907, 5033, 0, 1)

    tileset = TileCache("resources/image/TileSet/ImageSheet.png", Constant.TILE_WIDTH, Constant.TILE_HEIGHT).load_tile_table()
    camera_left = 0
    camera_right = Constant.SCREENRECT.width
    hCount = 1

    player.typeOfBullet = EBulletType.BASIC

    while player.health > -10:

        # CREEP MANAGER
        CreepManager.update(creeps, player.pos[0], player.pos[1], player.rect.left)
        CreepManager.create_creep_dynamic(player.pos[0], creeps)
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
                    player.typeOfBullet += 1
                    if player.typeOfBullet >= Constant.NUM_BULLET_TYPE:
                        player.typeOfBullet = EBulletType.BASIC
                elif event.key == Constant.PLAYER1JUMPKEY:
                    if not player.downable:
                        player.jump = 15
            elif event.type == KEYUP:
                if event.key == Constant.PLAYER1FIREKEY:
                    player.fire_down = False
                    if player.enegery >= 20:
                        player.state = Constant.THROW_STATE

        # Clear/erase the last drawn sprites
        render_group.clear(screen, background)
        screen.fill((0, 0, 0))
        if (camera_right < Constant.SCREENRECT.width * 8):
            if camera_left < (hCount - 1) * background.get_width():
                hCount -= 1
            elif (camera_left < hCount * background.get_width()):
                if (camera_right > hCount * background.get_width()):
                        screen.blit(background, (0  - camera_left + (hCount - 1) * background.get_width(), 0))
                        screen.blit(background, (hCount * background.get_width() - camera_left, 0))
                else:
                        screen.blit(background, (0  - camera_left + (hCount -1) * background.get_width(), 0))
            else:
                hCount += 1

        tiles = []
        for y in range(int(camera_left) / Constant.TILE_WIDTH, (int(camera_right) / Constant.TILE_WIDTH) + 1):
            if y > 239:
                y = 239
            for x in range(0, 20):
                if Constant.MAP[x][y] is not 0:
                    tile = Tile(tileset, (x, y), (32 * y, 32 * x))
                    screen.blit(tile.image, (Constant.TILE_WIDTH * y - camera_left, Constant.TILE_HEIGHT * x))
                    tiles.append(tile)
        """PLAYER GOES DOWN"""
        player.downable = True
        for tile in tiles:
            if tile.downable == True:
                continue;
            if(player.pos[0]  >= tile.pos[0] and player.pos[0]  <= tile.pos[0] + Constant.TILE_WIDTH) \
                    or ( player.pos[0] + Constant.PLAYERWIDTH  >= tile.pos [0] and player.pos[0] + Constant.PLAYERWIDTH  <= tile.pos[0] + Constant.TILE_WIDTH):
                if (player.pos[1] + Constant.PLAYERHEIGHT  >= tile.pos[1] and player.pos[1] + Constant.PLAYERHEIGHT <= tile.pos[1] + Constant.TILE_HEIGHT):
                    player.downable = False
                    break;
        # Update all the sprites
        render_group.update()
        items.update()

        # Handle player input
        key_state = pygame.key.get_pressed()

        player.check(key_state)

        if player1_down_to_up and not player.fire_down and player.enegery >= 25:
            if player.typeOfBullet == EBulletType.BASIC:
                butllet = Bullet(player.angle, player.power, player.rect, "fireball.png")
                shoot_sound.play()
                player.enegery -= butllet.energy_cost
            else:
                butllet = Bullet(player.angle, player.power, player.rect, "simple.png")
                butllet = Bullet(player.angle+10, player.power, player.rect, "simple.png")
                butllet = Bullet(player.angle-10, player.power, player.rect, "simple.png")
                shoot_sound.play()
                player.enegery -= butllet.energy_cost


        # *************************************************************
        # CHECK COLLISION HERE!
        # *************************************************************

        """ WALL BLOCK """
        player.isBlockByWall = False
        for tile in tiles:
            if tile.isBlock == True and player.pos[1] <= tile.pos[1] and player.pos[1] + Constant.PLAYERHEIGHT >= tile.pos[1] \
                and player.pos[1] > tile.pos[1] - Constant.TILE_HEIGHT:
                """ Player goes to the right """
                if player.direction == 1 and not player.isBlockByWall:
                    if player.pos[0] + Constant.PLAYERWIDTH >= tile.pos[0] \
                            and player.pos[0] + Constant.PLAYERWIDTH  <= tile.pos[0] + Constant.TILE_WIDTH:

                        player.isBlockByWall = True


                else:
                    if player.pos[0]  >= tile.pos[0] and player.pos[0] <= tile.pos[0] + Constant.TILE_WIDTH and not player.isBlockByWall:
                        player.isBlockByWall = True


        if not player.isBlockByWall and player.state == Constant.MOVE_STATE:
            if (((player.pos[0] + player.direction * player.speed) >= 0 ) and (player.pos[0] + player.direction * player.speed <= Constant.SCREENRECT.width * 8)):
                player.pos[0] += player.direction * player.speed
            if (camera_left + player.direction * player.speed >= 0) and (camera_right + player.direction * player.speed < Constant.SCREENRECT.width * 8):
                camera_left += player.direction * player.speed
                camera_right += player.direction * player.speed
                player.moveWithScreen = False
            else:
                player.moveWithScreen = True

        dict_collide = pygame.sprite.groupcollide(bombs, creeps, True, False)
        for key in dict_collide.keys():
            boom_sound.play()
            Explosion(key)
            for creep in dict_collide[key]:
                if not isinstance(creep, CreepASpecial):
                    creep.kill()
                else:
                    creep.check_die()

            #dict_collide[key].kill()

        # # Detect collision with ground
        # for bomb in pygame.sprite.spritecollide(ground, bombs, False):
        #     boom_sound.play()
        #     Explosion(bomb)
        #     bomb.kill()

        if pygame.sprite.spritecollide(player, creeps, False):
            player.lost_blood(1000)
        # *****************************
        # CHECK OBJECTS CAN MOVE DOWN
        # *****************************

        dirty = render_group.draw(screen)  # Draw all sprite, return list of rect
        pygame.display.update(dirty)    # Draw only changed rect
        pygame.display.flip()
        # Cap the frame rate
        clock.tick(Constant.FPS)
        #Clear tile list
        tiles[:] = []


    game_state = Constant.GAMEOVER

    game_over(screen, game_state)

# Call the "main" function if running this script
if __name__ == '__main__':
    home(Constant.HOME)
