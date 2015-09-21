import pygame
from pygame.locals import *
from pygame import Surface



window = pygame.display.set_mode((800,500))
background_colour = (255,255,255)
window.fill(background_colour)
clock = pygame.time.Clock()

def cut_frame(image):
    frame = []
    i = 0
    j = 0
    t = 0
    while j <= 2:
        frame.append(image.subsurface((i*114,j*90,110,90)).convert())
        t += 1
        i += 1
        if(i > 10 ):
            i = 0
            j += 1
    return frame

mypic = pygame.image.load("character.png")
frame = cut_frame(mypic)

def draw_chop_mat(frame):
	t = 9
	while True:
		window.blit(frame[t],(0,0))
		pygame.display.flip()
		t+=1
		if t > 10:
			t = 9
		pygame.time.wait(300)

def draw():
	img = pygame.image.load("radar.png").convert_alpha();
	while True:
		window.blit(img,(0,0))
		pygame.display.flip()
		pygame.time.wait(400)
		window.fill(background_colour)
		

def draw_move(frame):
	t = 0
	while True:
		window.blit(frame[t],(0,0))
		pygame.display.flip()
		t+=1
		if t > 6:
			t = 0
		pygame.time.wait(300)

def draw_cu_dong(frame):
	t = 7
	i = 1
	while True:
		window.blit(frame[t],(0,0))
		pygame.display.flip()
		t+=i
		if t > 8:
			i = -1
		if t < 7:
			i = 1
		pygame.time.wait(300)

def draw_move_left(frame):
        t = 0
        while True:
            window.blit(frame[t],(0,0))
            pygame.display.flip()
            t+=1
            if(t > 10):
            	t = 0
            pygame.time.wait(100)

def draw_throw(frame):
	t = 24;
	while True:
		window.blit(frame[t],(0,0))
		pygame.display.flip()
		t+=1
		if(t > 31):
			t = 17
		pygame.time.wait(100)

def draw_disappear():
	mypic = pygame.image.load("disappear.png")
	for i in range(1,6):
		pic = mypic.subsurface(((i-1)*71,0,71,73)).convert()
		window.blit(pic,(0,0))
		pygame.display.flip()
		pygame.time.wait(300)

def draw_appear():
	mypic = pygame.image.load("appear.png")
	for i in range(1,6):
		pic = mypic.subsurface(((i-1)*60,0,60,68)).convert()
		window.blit(pic,(0,0))
		pygame.display.flip()
		pygame.time.wait(300)
	draw_sexy_girl()

def draw_stand():
	mypic = pygame.image.load("stand.png")
	while True:
		for i in range(1,8):
			if i <= 4:
				pic = mypic.subsurface(((i-1)*60,0,60,65)).convert()
				window.blit(pic,(0,0))
				pygame.display.flip()
				pygame.time.wait(300)
			else :
				pic = mypic.subsurface(((8-i)*60,0,60,65)).convert()
				window.blit(pic,(0,0))
				pygame.display.flip()
				pygame.time.wait(300)
	

draw()
draw_move(frame)
#draw_move_left(frame)
#draw_throw(frame)
clock.tick(30)

raw_input("input: ")