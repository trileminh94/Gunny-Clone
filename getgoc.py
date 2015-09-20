import pygame,sys,math
from pygame.locals import *
from pygame import Surface

window = pygame.display.set_mode((800,500))
window.set_alpha(100)
background_colour = (255,255,255)
window.fill(background_colour)
clock = pygame.time.Clock()

angle = 30
angleRadian = angle*math.pi/180
while True: 
	keystate = pygame.key.get_pressed()
	if keystate[K_UP] == 1:
		if angle < 60:
			angle += 0.0005
			print angle
	elif keystate[K_DOWN] == 1:
		if angle > 30:
			angle -= 0.0005
			print angle
	pygame.event.pump()

raw_input("input: ")