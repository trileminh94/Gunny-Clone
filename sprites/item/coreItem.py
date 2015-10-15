import pygame
from common.constant import Constant
from common.utils import Utils

import math
from random import randint
from pygame.locals import *
__author__ = 'minh tri'


class coreItem(pygame.sprite.Sprite):
	def __init__(self,x,y,item_name):
		pygame.sprite.Sprite.__init__(self,self.containers)
		self.item_name = item_name
		self.x = x
		self.y = y
		self.state = Constant.ITEM_STATE_LIVE
		self.frame_index = 0
		self.frame_count = 0
		self.timer_die = 0
		self.timer_live = 0
		self.fall = True
		if self.item_name == Constant.MONEY_ITEM :
			self.style = Constant.ADD
			self.feature = Constant.MONEY
			self.num_frame = 7
			image = Utils.my_load_image("vatpham","money.png")
			self.image_frame = Utils.load_frame(image,0,0,40,40,0,self.num_frame)
		elif self.item_name == Constant.BUMERANGE_TREE_ITEM :
			print 28
			self.style = Constant.ADD
			self.feature = Constant.BUMERANGE 
			self.num_frame = 1
			image = Utils.my_load_image("vatpham","bumerange.png")
			self.image_frame = Utils.load_frame(image,0,0,89,70,0,self.num_frame)
			print len(self.image_frame)
		elif self.item_name == Constant.MAGIC_BOX_ITEM :
			self.style = Constant.ADD
			self.feature = Constant.LIFE
			self.num_frame = 1
			image = Utils.my_load_image("vatpham","magic_box.png")
			self.image_frame = Utils.load_frame(image,0,0,69,69,0,self.num_frame)
		elif self.item_name == Constant.MONSTER_ITEM :
			self.style = Constant.SUBTRACT
			self.feature = Constant.LIFE
			self.num_frame = 1
			image = Utils.my_load_image("vatpham","monster.png")
			self.image_frame = Utils.load_frame(image,0,0,89,89,0,self.num_frame)
		elif self.item_name == Constant.BERRY_ITEM :
			self.style = Constant.ADD
			self.feature = Constant.ENERGY
			self.num_frame = 1
			image = Utils.my_load_image("vatpham","berry.png")
			self.image_frame = Utils.load_frame(image,0,0,59,59,0,self.num_frame)
		print len(self.image_frame)
		self.image = self.image_frame[self.frame_index]
		self.rect = self.image.get_rect()
		self.rect.move_ip(x,y)
		self.max_right = x + self.move_length
		self.max_left = x - self.move_length

		self.sound = Utils.load_sound('Ding.ogg')

		self.pos_creep_screen = 0

	def animation(self):
		if(self.state == Constant.ITEM_STATE_LIVE):
			if self.num_frame == 1:
				self.frame_count += self.STEP_FLIP
				if(self.frame_count > 1):
					self.frame_count -= 1
					self.image = pygame.transform.flip(self.image,1,0)
			else:
				self.frame_count += 0.1
				if(self.frame_count > 1):
					self.frame_count -= 1
					self.frame_index += 1
					if(self.frame_index == self.num_frame - 1):
						self.frame_index = 0
				self.image = self.image_frame[self.frame_index]
		else:
			self.frame_count = 0
			self.frame_index = 0

	def checkState(self):
		if(self.state == Constant.ITEM_STATE_DIE):
			self.timer_die += 1
			if(self.timer_die > self.ITEM_TIME_TO_DIE):
				self.state = Constant.ITEM_STATE_LIVE
				self.add(self.containers)
				self.timer_die = 0
		else:
			self.timer_live += 1
			if(self.timer_live > self.ITEM_TIME_TO_LIVE):
				self.state = Constant.ITEM_STATE_DIE
				self.remove(self.containers)
				self.timer_live = 0
				self.playEffect()


	def fallDown(self):
		if(self.rect.y + self.image.get_height() > 410):
			self.fall = False
		else:
			self.rect.y += 3

	def playEffect(self):
		self.sound.play()

	def move(self):

		self.rect.x += self.velocity*self.direction
		if(self.rect.x > self.max_right):
			self.direction *= -1
		elif(self.rect.x < self.max_left):
			self.direction *= -1
			
	def die(self):
		self.state = Constant.ITEM_STATE_DIE
		self.remove(self.containers)

	def getFeature(self):
		return {self.style : self.feature}

	# def moveBackground(self):
	# 	creep_a1.pos_creep_screen = creep_a1.x - player.pos[0] + player.rect.left

	def update(self):
		self.checkState()
		self.animation()
		self.fallDown()
		if(self.state == Constant.ITEM_STATE_LIVE):
			if(self.fall == False):
				self.move()
		self.rect = pygame.Rect(self.pos_creep_screen, self.y, self.rect.width, self.rect.height) # TODO Dang la tao 1 object moi, hoi lau


	def update_pos(self, x_pos_player_world, pos_player_screen):
		self.pos_creep_screen = self.x - x_pos_player_world + pos_player_screen

