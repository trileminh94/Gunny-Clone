import pygame

from coreItem import coreItem
from pygame.locals import *

class berry(coreItem):
	STEP_FLIP = 0.03
	move_length = 200
	velocity = 0.2
	direction = -1
	ITEM_TIME_TO_DIE = 400
	ITEM_TIME_TO_LIVE = 1000