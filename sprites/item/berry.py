import pygame

from coreItem import coreItem
from pygame.locals import *

class berry(coreItem):
	STEP_FLIP = 0.03
	move_length = 200
	velocity = 0.2
	direction = -1