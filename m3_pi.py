#!/usr/bin/python
# -*- coding: utf-8 -*-

import obd, time, pygame, sys
from pygame.locals import *
img = pygame.image.load('cf_background.jpg')

# Set up the screen resolution
RESOLUTION = (480, 320)

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the box locations
BOX1 = [22.5, 20, 130, 130]
BOX2 = [172.5, 20, 130, 130]
BOX3 = [322.5, 20, 130, 130]

# Globals
speed = 0
RPM = 0
coolantTemp = 0

# DEBUG: Set debug logging so we can see everything that is happening.
obd.logger.setLevel(obd.logging.DEBUG)

# DEBUG: Print out all the ports so we can see if /dev/ttyUSB0 is available.
ports = obd.scan_serial()
print ports

# Create an async connection.
#connection = obd.Async("/dev/ttyUSB0", 115200, "3", fast=False)

# Create a connection to the ECU.
connection = obd.OBD("/dev/ttyUSB0", 115200, "3", fast=False)

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
            break

    # Get everything we want.
    response = connection.query(obd.commands.SPEED)
    speed = response.value.to("mph")
    speed = int(round(speed.magnitude))

    # 804.0 revolutions_per_minute
    response = connection.query(obd.commands.RPM)
    rpmString = str(response.value)
    pos = rpmString.find("revolutions")
    RPM = rpmString[:pos]

    # 86 degC
    response = connection.query(obd.commands.COOLANT_TEMP)
    coolantTemp = response.value

    # Clear the screen
    windowSurface.fill(BLACK)

    # Load the background image
    windowSurface.blit(img,(0,0))

    # Draw the 6 rectangles (Labeled 1-6)
    pygame.draw.rect(windowSurface, WHITE, BOX1, 2)
    pygame.draw.rect(windowSurface, WHITE, BOX2, 2)
    pygame.draw.rect(windowSurface, WHITE, BOX3, 2)

    # Box1 readout
    text = basicFont.render(str(speed), True, WHITE)
    textRect = text.get_rect()
    textRect.centerx = 87.5
    textRect.centery = 85
    windowSurface.blit(text, textRect)

    # BOX1 label
    text = basicFont.render("SPEED", True, WHITE)
    textRect = text.get_rect()
    textRect.centerx = 87.5
    textRect.centery = 40
    windowSurface.blit(text, textRect)

    # BOX2 readout
    text = basicFont.render(str(RPM), True, WHITE)
    textRect = text.get_rect()
    textRect.centerx = 237.5
    textRect.centery = 85
    windowSurface.blit(text, textRect)

    # BOX2 label
    text = basicFont.render("RPM", True, WHITE)
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

    # draw the window onto the screen
    pygame.display.update()
