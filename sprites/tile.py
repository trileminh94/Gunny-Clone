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
    def __init__(self, tiles, id, pos):
        self.tiles = tiles
        self.id = id
        self.type = Constant.MAP[id[0]][id[1]]
        self.image = 0
        self.pos = pos
        self.image = self.tiles[(self.type - 1) % 10][(self.type - 1) / 10]
        if (self.type == 1) or (self.type == 2) or (self.type == 3) or (self.type == 6) or (self.type == 7) or (self.type == 8) \
            or (self.type == 24) or (self.type == 25) or (self.type == 26) or (self.type == 92) or (self.type == 12):
            self.downable = False
        else:
            self.downable = True
        if (self.type == 81) or (self.type == 82) or (self.type == 83)  or (self.type == 86) or (self.type == 87):
            self.isBlock = False
        else:
            self.isBlock = True






