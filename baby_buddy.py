#!/usr/bin/python
import RPi.GPIO as GPIO
import time

sensorPin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensorPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

currState = False

while True:
    time.sleep(0.1)
    currState = GPIO.input(sensorPin)
   
    if currState:
        print "MOTION DETECTED!"
        time.sleep(1)