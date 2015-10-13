import pygame

from coreItem import coreItem
from pygame.locals import *

class monster(coreItem):
	STEP_FLIP = 0.07
	move_length = 100
	velocity = 1
	direction = 1