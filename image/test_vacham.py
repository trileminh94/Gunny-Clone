import pygame
from pygame.locals import *
from pygame import Surface

window = pygame.display.set_mode((800,500))
window.set_alpha(100)
background_colour = (255,255,255)
window.fill(background_colour)
clock = pygame.time.Clock()

img = pygame.image.load("craterbrink.png").convert()
img.set_colorkey((6,95,230))
img.convert_alpha()

window.blit(img,(0,0))
pygame.display.flip()
pygame.time.wait(100)

raw_input("input: ")