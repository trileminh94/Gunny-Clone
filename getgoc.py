import pygame,sys,math
from pygame.locals import *
from pygame import Surface

window = pygame.display.set_mode((800,500))
window.set_alpha(100)
background_colour = (255,255,255)
window.fill(background_colour)
clock = pygame.time.Clock()

angle = 30
R = 50
angleRadian = angle*math.pi/180
while True: 
	keystate = pygame.key.get_pressed()
	if keystate[K_UP] == 1:
		if angle < 70:
			angle += 0.05
			print angle
	elif keystate[K_DOWN] == 1:
		if angle > 20:
			angle -= 0.05
			print angle
	window.fill(background_colour)
	pygame.draw.line(window,Color("yellow"),(100,100),(100 + R*math.cos(angle*math.pi/180),-100 + R*math.sin(angle*math.pi/180)),3)
	pygame.event.pump()
	pygame.display.flip()

raw_input("input: ")