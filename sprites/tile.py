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
    not_blockwall_list = (54, 55, 56, 57, 64, 65, 66, 67, 69, 70, 74, 75, 76, 77, 79, 80, 44, 45, 46, 47, 81, 82, 83, 86, 87, 89, 90)
    not_blockground_list = (54, 55, 56, 57, 64, 65, 66, 67, 69, 70, 74, 75, 76, 77, 79, 80, 44, 45, 46, 47, 81, 82, 83, 86, 87, 89, 90)
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
        if self.type in self.not_blockwall_list:
            self.isBlockByWall = False
        else:
            self.isBlockByWall = True
        if self.type in self.not_blockground_list:
            self.isBlockByGround = False
        else:
            self.isBlockByGround = True





