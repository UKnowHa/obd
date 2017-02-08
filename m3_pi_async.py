#!/usr/bin/python
# -*- coding: utf-8 -*-

import obd
import time
import pprint

# Globals
rpm = 0
speed = 0
coolantTemp = 0
intakeTemp = 0
oilTemp = 0
intakePressure = 0

# DEBUG: Set debug logging so we can see everything that is happening.
obd.logger.setLevel(obd.logging.DEBUG)

# DEBUG: Print out all the ports so we can see if /dev/ttyUSB0 is available.
#ports = obd.scan_serial()
#print ports

# Create an async connection.
connection = obd.Async("/dev/ttyUSB0", 115200, "3", fast=False)

def new_rpm(r):
	print r.value

def new_speed(r):
	print r.value.to("mph")

def new_coolant_temp(r):
	print r.value

def new_intake_temp(r):
    print r.value

def new_oil_temp(r):
    print r.value

def new_intake_pressure(r):
    print r.value

# Keep track of RPM and SPEED.
connection.watch(obd.commands.RPM, callback=new_rpm, force=True)
connection.watch(obd.commands.SPEED, callback=new_speed, force=True)
connection.watch(obd.commands.THROTTLE_POS, callback=new_throttle_pos, force=True)

# Start the async update loop.
connection.start()

time.sleep(60)
connection.stop()
