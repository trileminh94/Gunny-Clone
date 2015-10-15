import pygame

from coreItem import coreItem
from common.constant import Constant
from sprites.bullet import Bullet
from sprites.MonsterBullet import MonsterBullet
from sprites.live_bar import Live_bar
from pygame.locals import *

class monster(coreItem):
	STEP_FLIP = 0.07
	move_length = 250
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
		self.x = x
		self.y = y
		self.pos_creep_screen = 0
		self.velocity = 1
		Live_bar(None, self, 0)
		#self.rect.x =  7550;


	def checkState(self):
		if(self.energy < 0):
			self.state = Constant.ITEM_STATE_DIE
			self.kill()

	def lost_blood(self,blood):
		self.energy -= blood

	def update(self):
		self.shot()
		self.checkState()
		self.animation()
		self.fallDown()
		if(self.state == Constant.ITEM_STATE_LIVE):
			if(self.fall == False):
				self.move()
		self.rect = pygame.Rect(self.pos_creep_screen, self.y, self.rect.width, self.rect.height) # TODO Dang la tao 1 object moi, hoi lau

	def update_pos(self, x_pos_player_world, pos_player_screen):
		self.pos_creep_screen = self.x - x_pos_player_world + pos_player_screen

	def shot(self):
		self.shoot_timer += 1
		if(self.shoot_timer > self.TIME_TO_SHOOT):
			bullet1 = MonsterBullet(20, 170, self.rect, "fireball.png")
			bullet2 = MonsterBullet(60, 200, self.rect, "fireball.png")
			bullet3 = MonsterBullet(60, 230, self.rect, "fireball.png")
			bullet4 = MonsterBullet(100, 270, self.rect, "fireball.png")
			bullet5 = MonsterBullet(140, 200, self.rect, "fireball.png")
			bullet6 = MonsterBullet(160, 140, self.rect, "fireball.png")
			self.shoot_timer = 0

	def move(self):
		self.x += 10

	def fallDown(self):
		# if(self.y + self.image.get_height() > 410):
		# 	self.fall = False
		# else:
		# 	self.y += 3
		self.fall = False

	def move(self):
		self.x += self.velocity*self.direction
		if(self.x > self.max_right):
			self.direction *= -1
		elif(self.x < self.max_left):
			self.direction *= -1