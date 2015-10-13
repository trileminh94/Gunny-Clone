__author__ = 'Luan'

import pygame
from pygame  import *
from common.constant import Constant
class TileCache:
    def __init__(self, imagesheet, width, height):
        self.width = width;
        self.height = height;
        self.imagesheet = imagesheet

    def load_tile_table(self):
        """Load an image and split it into tiles."""

        image = pygame.image.load(self.imagesheet)
        image_width, image_height = image.get_size()
        tile_table = []
        for tile_x in range(0, image_width/self.width):
            line = []
            tile_table.append(line)
            for tile_y in range(0, image_height/self.height):
                rect = (tile_x*self.width, tile_y*self.height, self.width, self.height)
                line.append(image.subsurface(rect))
        return tile_table

class Tile():
    not_downable_list = (1, 2, 3, 6, 7, 8, 9, 10, 18, 19, 20, 24, 25, 27, 28, 29, 31, 32, 33, 37, 38, 39, 41, 42, 43, 92)
    def __init__(self, tiles, id, pos):
        self.tiles = tiles
        self.id = id
        self.type = Constant.MAP[id[0]][id[1]]
        self.image = 0
        self.pos = pos
        self.image = self.tiles[(self.type - 1) % 10][(self.type - 1) / 10]
        if self.type in self.not_downable_list:
            self.downable = False
        else:
            self.downable = True
        if (self.type == 54) or (self.type == 55) or (self.type == 56)  or (self.type == 57) \
            or (self.type == 64) or (self.type == 65) or (self.type == 66) or (self.type == 67) or (self.type == 69) or (self.type == 70) \
            or (self.type == 74) or (self.type == 75) or (self.type == 76) or (self.type == 77)  or (self.type == 79) or (self.type == 80) \
            or (self.type == 44) or (self.type == 45) or (self.type == 46) or (self.type == 47) \
            or (self.type == 81) or (self.type == 82) or (self.type == 83) or (self.type == 86) or (self.type == 87) \
            or (self.type == 89) or (self.type == 90) :
            self.isBlock = False
        else:
            self.isBlock = True






