import pygame,sys,math
from pygame.locals import *
from pygame import Surface

window = pygame.display.set_mode((800,500))
window.set_alpha(100)
background_colour = (255,255,255)
window.fill(background_colour)
clock = pygame.time.Clock()
down = False
t = 0
f = 0
while True: 
	if down == True:
		t+=1
		f = 10*math.fabs(math.sin(t*math.pi/math.pow(10,6)))
		print "f = " + str(f)
	else:
		t = 0
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN :
			if event.key == pygame.K_SPACE:
				down = True
		elif event.type == pygame.KEYUP :
			if event.key == pygame.K_SPACE:
				down = False

raw_input("input: ")