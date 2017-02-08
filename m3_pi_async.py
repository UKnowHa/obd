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

# 804.0 revolutions_per_minute
def new_rpm(r):
	print r.value.magnitude
	#rpm = r.value.magnitude
	##OLD
	#rpmString = str(r.value)
	#pos = rpmString.find("revolutions")
	#rpm = rpmString[:pos]

def new_speed(r):
	print r.value.to("mph").magnitude
	#speed = r.value.to("mph")
	#speed = int(round(speed.magnitude))

def new_coolant_temp(r):
	print r.value.to("degF").magnitude
	#coolantTemp = r.value.to("degF")
	#coolantTemp = int(round(coolantTemp.magnitude))

def new_intake_temp(r):
    print r.value.to("degF").magnitude
	#intakeTemp = r.value.to("degF")
	#intakeTemp = int(round(intakeTemp.magnitude))

def new_oil_temp(r):
    print r.value.to("degF").magnitude
	#oilTemp = r.value.to("degF")
	#oilTemp = int(round(oilTemp.magnitude))

# kPa
def new_intake_pressure(r):
    print r.value.magnitude
	#intakePressure = r.value

# Keep track of everything.
connection.watch(obd.commands.RPM, callback=new_rpm, force=True)
connection.watch(obd.commands.SPEED, callback=new_speed, force=True)
connection.watch(obd.commands.COOLANT_TEMP, callback=new_coolant_temp, force=True)
connection.watch(obd.commands.INTAKE_TEMP, callback=new_intake_temp, force=True)
connection.watch(obd.commands.OIL_TEMP, callback=new_oil_temp, force=True)
connection.watch(obd.commands.INTAKE_PRESSURE, callback=new_intake_pressure, force=True)

# Start the async update loop.
connection.start()

time.sleep(60)
connection.stop()
