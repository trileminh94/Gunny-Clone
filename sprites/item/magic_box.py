import pygame

from coreItem import coreItem
from pygame.locals import *

class magicbox(coreItem):
	STEP_FLIP = 0.06
	move_length = 10
	velocity = 0.4
	direction = 1
	ITEM_TIME_TO_DIE = 400
	ITEM_TIME_TO_LIVE = 1000

	def move(self):
		pass
