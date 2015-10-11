import pygame
import os.path
__author__ = 'tri'


class Utils:
    __main_dir = "resources"

    def __init__(self):
        pass

    def load_image(file_name):
        """loads an image, prepares it for play"""
        file_name = os.path.join(Utils.__main_dir, 'data', file_name)
        try:
            surface = pygame.image.load(file_name)
        except pygame.error:
            raise SystemExit('Could not load image "%s" %s' % (file_name, pygame.get_error()))
        return surface.convert()
    load_image = staticmethod(load_image)

    def my_load_image(sub_folder, file_name):
        """loads an image, prepares it for play"""
        folder = os.path.join(Utils.__main_dir, 'image')
        file_name = os.path.join(folder, sub_folder, file_name)
        try:
            surface = pygame.image.load(file_name)
        except pygame.error:
            raise SystemExit('Could not load image "%s" %s' % (file_name, pygame.get_error()))
        return surface.convert_alpha()
    my_load_image = staticmethod(my_load_image)

    def load_images(*files):
        images = []
        for f in files:
            images.append(Utils.load_image(f))
        return images
    load_images = staticmethod(load_images)

    def cut_frame(image, x, y, width, length):
        frame = []
        i = 0
        j = 0
        t = 0
        while j <= 2:
            frame.append(image.subsurface((i*x, j*y, width, length)))
            t += 1
            i += 1
            if i > 10:
                i = 0
                j += 1
        return frame
    cut_frame = staticmethod(cut_frame)

    def load_sound(file_name):
        if not pygame.mixer:
            return Dummy_sound()

        file_name = os.path.join(Utils.__main_dir, 'data', file_name)
        try:
            sound = pygame.mixer.Sound(file_name)
            return sound
        except pygame.error:
            print ('Warning, unable to load, %s' % file_name)
        return Dummy_sound()
    load_sound = staticmethod(load_sound)

    def load_frame(image, x, y, width, height, step_x, num):
        """
        Init list of sprite sheets from an image
        :param image: source image
        :param x: position x of top left corner of the first sprite
        :param y: position y of top left corner of the first sprite
        :param width: width of each sprite
        :param height: height of each sprite
        :param step_x: distance between two sprite
        :param num: number of sprites
        :return: list surface
        """
        frame = []
        i = 0
        while (i < num) & (x + width < image.get_width()):
            frame.append(image.subsurface(x, y, width, height))
            x = x + width
            x = x + step_x
            i += 1
        return frame
    load_frame = staticmethod(load_frame)