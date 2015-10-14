import pygame

from coreItem import coreItem
from common.constant import Constant
from sprites.bullet import Bullet
from pygame.locals import *

class monster(coreItem):
	STEP_FLIP = 0.07
	move_length = 100
	velocity = 1
	direction = 1
	ITEM_TIME_TO_DIE = 400
	ITEM_TIME_TO_LIVE = 1000
	energy = 100
	TIME_TO_SHOOT = 100
	shoot_timer = 0
	energy = 100

	def __init__(self,x,y,item_name):
		coreItem.__init__(self,x,y,item_name)
		self.rect.x = 7550;

	def checkState(self):
		if(self.energy < 0):
			self.state = Constant.ITEM_STATE_DIE

	def update(self):
		self.shot()
		self.checkState()
		self.animation()
		self.fallDown()
		if(self.state == Constant.ITEM_STATE_LIVE):
			if(self.fall == False):
				self.move()

	def shot(self):
		self.shoot_timer += 1
		if(self.shoot_timer > self.TIME_TO_SHOOT):
			bullet1 = Bullet(20, 170, self.rect, "fireball.png")
			bullet2 = Bullet(60, 200, self.rect, "fireball.png")
			bullet3 = Bullet(60, 230, self.rect, "fireball.png")
			bullet4 = Bullet(100, 270, self.rect, "fireball.png")
			bullet5 = Bullet(140, 200, self.rect, "fireball.png")
			bullet6 = Bullet(160, 140, self.rect, "fireball.png")
			self.shoot_timer = 0
