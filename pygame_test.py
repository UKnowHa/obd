#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame, sys
from pygame.locals import *
img = pygame.image.load('cf_background.jpg')

# Globals
rpm = 0
speed = 0
coolantTemp = 0
intakeTemp = 0
oilTemp = 0
intakePressure = 0

# Set up the screen resolution
RESOLUTION = (480, 320)

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the box locations
BOX1 = [22.5, 20, 130, 130]
BOX2 = [172.5, 20, 130, 130]
BOX3 = [322.5, 20, 130, 130]
BOX4 = [22.5, 170, 130, 130]
BOX5 = [172.5, 170, 130, 130]
BOX6 = [322.5, 170, 130, 130]

# 0C
def getRPM():
	global rpm
	rpm += 1

# 0D
def getSpeed():
	global speed
	speed += 1
	
# 05
def getCoolantTemp():
	global coolantTemp
	coolantTemp = "100\xb0F"

# 0F	
def getIntakeTemp():
	global intakeTemp
	intakeTemp = "150\xb0F"

# 5C	
def getOilTemp():
	global oilTemp
	oilTemp = "200\xb0F"

# 0B	
def getIntakePressure():
	global intakePressure
	intakePressure = "5 kPa"
	
# set up pygame
pygame.init()

# set up fonts
basicFont = pygame.font.SysFont(None, 48)

# set up the window
windowSurface = pygame.display.set_mode(RESOLUTION, 0, 32)
pygame.display.set_caption('OBD Display Test')

# run the game loop
while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
			
	# Get everything we want.
	getRPM()
	getSpeed()
	getCoolantTemp()
	getIntakeTemp()
	getOilTemp()
	getIntakePressure()
	
	# Clear the screen
	windowSurface.fill(BLACK)
	
	# Load the background image
	windowSurface.blit(img,(0,0))
	
	# Draw the 6 rectangles (Labeled 1-6)
	pygame.draw.rect(windowSurface, WHITE, BOX1, 2)
	pygame.draw.rect(windowSurface, WHITE, BOX2, 2)
	pygame.draw.rect(windowSurface, WHITE, BOX3, 2)
	pygame.draw.rect(windowSurface, WHITE, BOX4, 2)
	pygame.draw.rect(windowSurface, WHITE, BOX5, 2)
	pygame.draw.rect(windowSurface, WHITE, BOX6, 2)
	
	# Box1 readout
	text = basicFont.render(str(rpm), True, WHITE)
	textRect = text.get_rect()
	textRect.centerx = 87.5
	textRect.centery = 85
	windowSurface.blit(text, textRect)
	
	# BOX1 label
	text = basicFont.render("RPM", True, WHITE)
	textRect = text.get_rect()
	textRect.centerx = 87.5
	textRect.centery = 40
	windowSurface.blit(text, textRect)
	
	# BOX2 readout
	text = basicFont.render(str(speed), True, WHITE)
	textRect = text.get_rect()
	textRect.centerx = 237.5
	textRect.centery = 85
	windowSurface.blit(text, textRect)
	
	# BOX2 label
	text = basicFont.render("SPEED", True, WHITE)
	textRect = text.get_rect()
	textRect.centerx = 237.5
	textRect.centery = 40
	windowSurface.blit(text, textRect)
	
	# BOX3 readout
	text = basicFont.render(str(coolantTemp), True, WHITE)
	textRect = text.get_rect()
	textRect.centerx = 387.5
	textRect.centery = 85
	windowSurface.blit(text, textRect)
	
	# BOX3 label
	text = basicFont.render("CLNT", True, WHITE)
	textRect = text.get_rect()
	textRect.centerx = 387.5
	textRect.centery = 40
	windowSurface.blit(text, textRect)
	
	# BOX4 readout
	text = basicFont.render(str(intakeTemp), True, WHITE)
	textRect = text.get_rect()
	textRect.centerx = 87.5
	textRect.centery = 235
	windowSurface.blit(text, textRect)
	
	# BOX4 label
	text = basicFont.render("INTAKE", True, WHITE)
	textRect = text.get_rect()
	textRect.centerx = 87.5
	textRect.centery = 190
	windowSurface.blit(text, textRect)
	
	# BOX5 readout
	text = basicFont.render(str(oilTemp), True, WHITE)
	textRect = text.get_rect()
	textRect.centerx = 237.5
	textRect.centery = 235
	windowSurface.blit(text, textRect)
	
	# BOX5 label
	text = basicFont.render("OIL", True, WHITE)
	textRect = text.get_rect()
	textRect.centerx = 237.5
	textRect.centery = 190
	windowSurface.blit(text, textRect)
	
	# BOX6 readout
	text = basicFont.render(str(intakePressure), True, WHITE)
	textRect = text.get_rect()
	textRect.centerx = 387.5
	textRect.centery = 235
	windowSurface.blit(text, textRect)
	
	# BOX6 label
	text = basicFont.render("INTAKE", True, WHITE)
	textRect = text.get_rect()
	textRect.centerx = 387.5
	textRect.centery = 190
	windowSurface.blit(text, textRect)
	
	# draw the window onto the screen
	pygame.display.update()