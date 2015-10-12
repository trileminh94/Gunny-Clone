__author__ = 'Luan'

import pygame

class TileCache:
    def __init__(self, imagesheet, width, height):
        self.width = width;
        self.height = height;
        self.imagesheet = imagesheet

    def load_tile_table(self):
        """Load an image and split it into tiles."""

        image = pygame.image.load(self.imagesheet).convert()
        image_width, image_height = image.get_size()
        tile_table = []
        for tile_x in range(0, image_width/self.width):
            line = []
            tile_table.append(line)
            for tile_y in range(0, image_height/self.height):
                rect = (tile_x*self.width, tile_y*self.height, self.width, self.height)
                line.append(image.subsurface(rect))
        return tile_table

class Tile:
    def __init__(self, tiles, id, width, height):
        self.width = width
        self.height = height
        self.tiles = tiles
        self.id = id
        self.image = 0

    def render(self):
            self.image = self.tiles[(self.id - 1) % 10][(self.id - 1) / 10]




