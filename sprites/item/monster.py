import pygame

from coreItem import coreItem
from pygame.locals import *

class monster(coreItem):
	STEP_FLIP = 0.07
	move_length = 100
	velocity = 1
	direction = 1
	ITEM_TIME_TO_DIE = 400
	ITEM_TIME_TO_LIVE = 1000
	energy = 100
	TIME_TO_SHOOT = 500
	shoot_timer = 0

	def checkState(self):
		if(energy < 0):
			self.self.state = Constant.ITEM_STATE_DIE

	def update(self):
		self.checkState()
		self.animation()
		self.fallDown()
		if(self.state == Constant.ITEM_STATE_LIVE):
			if(self.fall == False):
				self.move()

	def shot(self):
		self.shoot_timer += 1
		if(self.shoot_timer > self.TIME_TO_SHOOT):
			bullet1 = Bullet(20, 100, self.rect, "fireball.png")
			bullet2 = Bullet(60, 80, self.rect, "fireball.png")
			bullet3 = Bullet(100, 70, self.rect, "fireball.png")
			bullet4 = Bullet(140, 80, self.rect, "fireball.png")
			bullet5 = Bullet(160, 100, self.rect, "fireball.png")
			self.shoot_timer = 0
