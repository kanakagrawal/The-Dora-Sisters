import random, os
import math
import time
import pygame
import copy
import sys
from pygame.locals import *
from sys import exit

pygame.init()

slope=0.0

screen_width=1000
screen_height=700
game=pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption = ('Game Hack')
sound = pygame.mixer.Sound("music.ogg")
sound.play(-1)
game.fill([255,255,255])

pygame.display.update()
points=100
win=0


for i in range(1, 16):
	if i == 1:
		s="Two people from planet Pandora are stuck on planet Dora. So the Pandorians developed a laser technology by which they"
	if i==2:
		s="               can communicate with their people in Dora. Unfortunately the path is filled with              "
	if i==3: 
		s="          reflectors, refractors and black holes. You have been called to their rescue. Make the            " 
	if i==4:
		s="                    laser ray reach the planet Dora without entering any black hole or going out of their universe.                "
	if i==5:
		s= "                                                                                                                                                                             "
	if i==6:
		s="                                          Instructions                                                 "
	if i==7:
		s="1. Score starts with an initial value of 100."
	if i==8:
		s="2. If the light ray goes out of the screen you lose 10 points."
	if i==9:
		s="3. If the light ray goes into a black hole you lose 20 points."
	if i==10:
		s="4. If at any point during the game the total score goes zero or negative you lose the game."
	if i==11:
		s="5. Click anywhere on screen to send the laser in that direction."	
	if i==12:
		s="6. All laser beams start from pandora, a red quarter circle located on the top left of the screen."
	if i==13:
		s="7. Your target is Dora the small red semi circle located on the bottom right."	
	if i==14:
		s=" "	
	if i==15:
		s="PRESS SPACEBAR TO BEGIN"
		  
	basicfont = pygame.font.SysFont(None, 24)
	text = basicfont.render(s, True, (255, 0, 0), (255, 255, 255))
	textrect = text.get_rect()
	textrect.centerx = 500
	textrect.centery = 200+18*i
	game.blit(text, textrect)
	pygame.display.update()

playing=True
while playing:
	for ev in pygame.event.get():
		if ev.type == KEYDOWN:
			if ev.key == K_SPACE:
				playing = False

bgimg = pygame.image.load("image.jpg").convert()			#for overlapping and removing lines
game.blit(bgimg, [0,0])
basicfont = pygame.font.SysFont(None, 48)		
text = basicfont.render("score-"+str(points), True, (255, 0, 0), (255, 255, 255))
textrect = text.get_rect()
textrect.centerx = 900
textrect.centery = 40
game.blit(text, textrect)	


	
basicfont = pygame.font.SysFont(None, 150)
text4 = basicfont.render("LEVEL 1", True, (255, 0, 0), (255, 255, 255))
textrect4 = text4.get_rect()
textrect4.centerx = 500
textrect4.centery = 350
game.blit(text4, textrect4)
pygame.display.update()
pygame.time.delay(2000)

while win==0 :
	bgimg = pygame.image.load("image.jpg").convert()			#for overlapping and removing lines
	game.blit(bgimg, [0,0])
	basicfont = pygame.font.SysFont(None, 48)		
	text = basicfont.render("score-"+str(points), True, (255, 0, 0), (255, 255, 255))
	textrect = text.get_rect()
	textrect.centerx = 900
	textrect.centery = 40
	game.blit(text, textrect)	
	pygame.draw.circle(game, [255,0,0], [0,0], 100)
	pygame.display.update()
	rl=100.0
	rh=10.0
	a1=350
	b1=600
	a2=900
	b2=400
	a3=500
	b3=200
	a4=600
	b4=350
	a5=700
	b5=200
	c1=750
	d1=600
	xc=550
	yc=500
	xd=775
	yd=700
	final_point = pygame.draw.circle(game, [255,0,0], [xd,yd], 40)
	mirror1= pygame.draw.rect(game, [0, 255, 255], (a1, b1, rl, rh))
	mirror2 = pygame.draw.rect(game, [0, 255, 255], (a2, b2, rh, rl))
	mirror3 = pygame.draw.rect(game, [0, 255, 255], (a3, b3, rl, rh))
	mirror4 = pygame.draw.rect(game, [0, 255, 255], (a4, b4, rl, rh))
	refraction1= pygame.draw.rect(game, [0, 0, 255], (c1, d1, rl, rh))
	refraction2= pygame.draw.rect(game, [0, 0, 255], (c1, d1+rh, rl, rh))
	refraction3= pygame.draw.rect(game, [0, 0, 255], (c1, d1+2*rh, rl, rh))
	refraction4= pygame.draw.rect(game, [0, 0, 255], (c1, d1+3*rh, rl, rh))
	mirror5= pygame.draw.rect(game, [0, 255, 255], (a5, b5, rl, rh))
	blackhole = pygame.draw.circle(game, [0,0,0], [xc,yc], 70)
	pygame.display.update()
	ev = pygame.event.get()
	for event in ev:
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			x, y = pos
			x1=0.0
			y1=0.0
			slope = y*1.0/x
			z=1.0
			while z<screen_width and z>-screen_width and y1+z*slope<730 and y1+z*slope>-10 and x1+z<1100:
				hits_vertical_mirror=0
				hits_mirror5=0				
				pygame.draw.line(game, [255, 255, 0], [x1,y1], [x1+z, y1+z*slope])
				pygame.display.update()
				pygame.time.delay(5)
				if ((y1+z*slope>=b1 and y1+z*slope<=b1+rh and x1+z>=a1 and x1+z<=a1+rl)or(y1+z*slope>=b3 and y1+z*slope<=b3+rh and x1+z>=a3 and x1+z<=a3+rl)or(y1+z*slope>=b4 and y1+z*slope<=b4+rh and x1+z>=a4 and x1+z<=a4+rl)):		#horizontal mirror
					x1=x1+z
					y1=y1+z*slope
					z=1
					slope=-slope
				elif ((y1+z*slope>=b5 and y1+z*slope<=b5+rh and x1+z>=a5 and x1+z<=a5+rl)):		#horizontal mirror
					x1=x1+z
					y1=y1+z*slope
					z=1
					slope=-slope
				elif((y1+z*slope>=d1 and y1+z*slope<=d1+rh and x1+z>=c1 and x1+z<=c1+rl)):	#refraction1
					x1=x1+z
					y1=y1+z*slope
					slope=1/math.tan(math.asin(math.sin(math.atan(1/slope))/1.2))
					if(z>0):
						z=1
					else:
						z=-1
					pygame.time.delay(2)
				elif((y1+z*slope>=d1+rh and y1+z*slope<=d1+rh+rh and x1+z>=c1 and x1+z<=c1+rl)):	#refraction2
					x1=x1+z
					y1=y1+z*slope
					slope=1/math.tan(math.asin(math.sin(math.atan(1/slope))/1.21))
					if(z>0):
						z=1
					else:
						z=-1
					pygame.time.delay(2)
				elif((y1+z*slope>=d1+2*rh and y1+z*slope<=d1+2*rh+rh and x1+z>=c1 and x1+z<=c1+rl)):	#refraction3
					x1=x1+z
					y1=y1+z*slope
					slope=1/math.tan(math.asin(math.sin(math.atan(1/slope))/1.23))
					if(z>0):
						z=1
					else:
						z=-1
					pygame.time.delay(2)
				elif((y1+z*slope>=d1+3*rh and y1+z*slope<=d1+3*rh+rh and x1+z>=c1 and x1+z<=c1+rl)):	#refraction4
					x1=x1+z
					y1=y1+z*slope
					slope=1/math.tan(math.asin(math.sin(math.atan(1/slope))/1.25))
					if(z>0):
						z=1
					else:
						z=-1
					pygame.time.delay(2)
				elif((y1+z*slope>=b2 and y1+z*slope<=b2+rl and x1+z>=a2 and x1+z<=a2+rh)):	#vertical mirror
					alpha=1				
					x1=x1+z
					y1=y1+z*slope
					if(z>0):
						z=-1
					else:
						z=1
					slope=-slope
				elif math.pow((y1+z*slope-yc)*(y1+z*slope-yc)+(x1+z-xc)*(x1+z-xc),0.5)<70 :	#blackhole
					points=points-10
					break					
				elif math.pow((y1+z*slope-yd)*(y1+z*slope-yd)+(x1+z-xd)*(x1+z-xd),0.5)<40:	#final point
					win=1					
					break
				if(z>0):
					z=z+1
				else:
					z=z-1
			if win==0:
				points=points-10
			pygame.display.update()
	if points<=0 :
		win=0				
		break
if win==1:
	pygame.time.delay(2000)
	bgimg = pygame.image.load("image.jpg").convert()			#for overlapping and removing lines
	game.blit(bgimg, [0,0])
	basicfont = pygame.font.SysFont(None, 48)		
	text = basicfont.render("score-"+str(points), True, (255, 0, 0), (255, 255, 255))
	textrect = text.get_rect()
	textrect.centerx = 900
	textrect.centery = 40
	game.blit(text, textrect)	

	basicfont = pygame.font.SysFont(None, 150)
	text3 = basicfont.render("LEVEL 2", True, (255, 0, 0), (255, 255, 255))
	textrect3 = text3.get_rect()
	textrect3.centerx = 500
	textrect3.centery = 350
	game.blit(text3, textrect3)
	pygame.display.update()
	pygame.time.delay(2000)












while win==1:
	
	rl=100.0
	rh=10.0
	a1=350
	b1=600
	a2=900
	b2=400	
	a3=500
	b3=200
	a4=625
	b4=340
	a5=790
	b5=380
	a6=110
	b6=200
	a7=150
	b7=100
	a8=800
	b8=650
	a9=550
	b9=250
	a10=200
	b10=550
	c1=750
	d1=600
	c2=600
	d2=300
	c3=200
	d3=500
	xc=550
	yc=500
	xd=725
	yd=700

	bgimg = pygame.image.load("image.jpg").convert()			#for overlapping and removing lines
	game.blit(bgimg, [0,0])
	basicfont = pygame.font.SysFont(None, 48)		
	text = basicfont.render("score-"+str(points), True, (255, 0, 0), (255, 255, 255))
	textrect = text.get_rect()
	textrect.centerx = 900
	textrect.centery = 40
	game.blit(text, textrect)	
	pygame.draw.circle(game, [255,0,0], [0,0], 100)
	pygame.display.update()
	final_point = pygame.draw.circle(game, [255,0,0], [xd,yd], 40)
	mirror1= pygame.draw.rect(game, [0, 255, 255], (a1, b1, rl, rh))
	mirror2 = pygame.draw.rect(game, [0, 255, 255], (a2, b2, rh, rl))
	mirror10 = pygame.draw.rect(game, [0, 255, 255], (a10, b10, rl, rh))
	mirror3 = pygame.draw.rect(game, [0, 255, 255], (a3, b3, rl, rh))
	mirror4 = pygame.draw.rect(game, [0, 255, 255], (a4, b4, rl, rh))
	refraction2= pygame.draw.rect(game, [0, 0, 255], (c3, d3, rl, rh))
	refraction2= pygame.draw.rect(game, [0, 0, 255], (c2, d2, rl, rh))
	refraction1= pygame.draw.rect(game, [0, 0, 255], (c1, d1, rl, rh))
	refraction11= pygame.draw.rect(game, [0, 0, 255], (c1, d1+rh, rl, rh))
	refraction111= pygame.draw.rect(game, [0, 0, 255], (c1, d1+2*rh, rl, rh))
	refraction1111= pygame.draw.rect(game, [0, 0, 255], (c1, d1+3*rh, rl, rh))
	mirror5= pygame.draw.rect(game, [0, 255, 255], (a5, b5, rl, rh))
	mirror6= pygame.draw.rect(game, [0, 255, 255], (a6, b6, rh, rl))
	mirror7= pygame.draw.rect(game, [0, 255, 255], (a7, b7, rl, rh))
	mirror8= pygame.draw.rect(game, [0, 255, 255], (a8, b8, rl, rh))
	mirror9 = pygame.draw.rect(game, [0, 255, 255], (a9, b9, rl, rh))
	blackhole = pygame.draw.circle(game, [0,0,0], [xc,yc], 50)
	pygame.display.update()
	
	ev = pygame.event.get()
	for event in ev:
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			pos = pygame.mouse.get_pos()
			x, y = pos
			x1=0.0
			y1=0.0
			slope = y*1.0/x
			z=1.0
			while z<screen_width and z>-screen_width and y1+z*slope<730 and y1+z*slope>-10 and x1+z<1100:
				hits_vertical_mirror=0
				hits_mirror5=0				
				line1=pygame.draw.line(game, [255, 255, 0], [x1,y1], [x1+z, y1+z*slope])
				pygame.display.update()
				pygame.time.delay(5)
				if ((y1+z*slope>=b1 and y1+z*slope<=b1+rh and x1+z>=a1 and x1+z<=a1+rl)or(y1+z*slope>=b3 and y1+z*slope<=b3+rh and x1+z>=a3 and x1+z<=a3+rl)or(y1+z*slope>=b4 and y1+z*slope<=b4+rh and x1+z>=a4 and x1+z<=a4+rl)or(y1+z*slope>=b9 and y1+z*slope<=b9+rh and x1+z>=a9 and x1+z<=a9+rl)):		#horizontal mirror
					x1=x1+z
					y1=y1+z*slope
					z=1
					slope=-slope
				elif ((y1+z*slope>=b5 and y1+z*slope<=b5+rh and x1+z>=a5 and x1+z<=a5+rl)or(y1+z*slope>=b7 and y1+z*slope<=b7+rh and x1+z>=a7 and x1+z<=a7+rl)or(y1+z*slope>=b8 and y1+z*slope<=b8+rh and x1+z>=a8 and x1+z<=a8+rl)or(y1+z*slope>=b10 and y1+z*slope<=b10+rh and x1+z>=a10 and x1+z<=a10+rl)):		#horizontal mirror
					x1=x1+z
					y1=y1+z*slope
					z=1
					slope=-slope
				elif((y1+z*slope>=d1 and y1+z*slope<=d1+rh and x1+z>=c1 and x1+z<=c1+rl)or(y1+z*slope>=d2 and y1+z*slope<=d2+rh and x1+z>=c2 and x1+z<=c2+rl)or(y1+z*slope>=d3 and y1+z*slope<=d3+rh and x1+z>=c3 and x1+z<=c3+rl)):	#refraction1,refraction2,refraction3
					x1=x1+z
					y1=y1+z*slope
					slope=1/math.tan(math.asin(math.sin(math.atan(1/slope))/1.2))
					if(z>0):
						z=1
					else:
						z=-1
					pygame.time.delay(2)
				elif((y1+z*slope>=d1+rh and y1+z*slope<=d1+rh+rh and x1+z>=c1 and x1+z<=c1+rl)):	#refraction2
					x1=x1+z
					y1=y1+z*slope
					slope=1/math.tan(math.asin(math.sin(math.atan(1/slope))/1))
					if(z>0):
						z=1
					else:
						z=-1
					pygame.time.delay(2)
				elif((y1+z*slope>=d1+2*rh and y1+z*slope<=d1+2*rh+rh and x1+z>=c1 and x1+z<=c1+rl)or(y1+z*slope>=d1+3*rh and y1+z*slope<=d1+3*rh+rh and x1+z>=c1 and x1+z<=c1+rl)):	#refraction3 #refraction4
					x1=x1+z
					y1=y1+z*slope
					slope=1/math.tan(math.asin(math.sin(math.atan(1/slope))/1.2))
					if(z>0):
						z=1
					else:
						z=-1
					pygame.time.delay(2)					
				elif((y1+z*slope>=b2 and y1+z*slope<=b2+rl and x1+z>=a2 and x1+z<=a2+rh)or(y1+z*slope>=b6 and y1+z*slope<=b6+rl and x1+z>=a6 and x1+z<=a6+rh)):	#vertical mirror
					alpha=1				
					x1=x1+z
					y1=y1+z*slope
					if(z>0):
						z=-1
					else:
						z=1
					slope=-slope
				elif math.pow((y1+z*slope-yc)*(y1+z*slope-yc)+(x1+z-xc)*(x1+z-xc),0.5)<50 :	#blackhole
					points=points-10
					break					
				elif math.pow((y1+z*slope-yd)*(y1+z*slope-yd)+(x1+z-xd)*(x1+z-xd),0.5)<40:	#final point
					win=2
					break
				if(z>0):
					z=z+1
				else:
					z=z-1
			if win==1:
				points=points-10
			
			pygame.display.update()
	if points<=0 :
		win=0				
		break
	
if win==0 :  
	basicfont = pygame.font.SysFont(None, 150)
	text1 = basicfont.render("GAME OVER", True, (255, 0, 0), (255, 255, 255))
	textrect1 = text1.get_rect()
	textrect1.centerx = 500
	textrect1.centery = 350
	game.blit(text1, textrect1)
if win==2 :  
	basicfont = pygame.font.SysFont(None, 150)
	text2 = basicfont.render("YOU WIN", True, (255, 0, 0), (255, 255, 255))
	textrect2 = text2.get_rect()
	textrect2.centerx = 500
	textrect2.centery = 350
	game.blit(text2, textrect2)


pygame.display.update()
pygame.time.delay(5000)	
