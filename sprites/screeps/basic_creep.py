import pygame
__author__ = 'tri'


class BasicCreep(pygame.sprite.Sprite):
    screen = None   # TODO for testing

    def __init__(self, x, y, left, right):
        """
        Constructor
        :param x: position x in world
        :param y: position y in world
        :param left, right: limit position for moving of creep
        :return: None
        """
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.x = x
        self.y = y
        self.pos_creep_screen = 0   # position x of creep in screen, = creep-player + player-screen
        self.left = left
        self.right = right
        self.base_line = y

    def update(self):

        self.frame += 0.1
        if self.direction == 0:
            self.image = self.images_forward[int(round(self.frame))%self.frame_length]
        else:
            self.image = self.images_back[int(round(self.frame))%self.frame_length]

        self.x += self.move_speed_x

        if self.y <= self.base_line and (self.x < self.left or self.x > self.right):
            self.redirect()
        self.rect = pygame.Rect(self.pos_creep_screen, self.y, self.rect.width, self.rect.height) # TODO Dang la tao 1 object moi, hoi lau

        if self.down_able:
                self.rect = self.rect.move(0, self.move_speed_y)
        pygame.draw.rect(BasicCreep.screen, 0x000000, self.rect)

    def redirect(self):
        # if isinstance(self, CreepASpecial):
        #     if self.y > self.base_line:
        #         return
        self.frame = 0
        self.move_speed_x = -self.move_speed_x
        if self.move_speed_x > 0:
            self.direction = 0
        else:
            self.direction = 1

    def set_down_able(self, isTrue):
        self.down_able = isTrue