#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import urllib

device_id = "1000"

def fetch_url(url, params, method): 
    result = urllib.urlopen(url, params)
    print result.code

def write_motion_sample():
    fetch_url("http://babybuddy.cloudapp.net/api/motions?deviceId=" + device_id, device_id.encode("ASCII"), "POST")


sensor_pin = 7

GPIO.setmode(GPIO.BOARD)
GPIO.setup(sensor_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

motion_detected = False


while True:
    time.sleep(0.1)
    motion_detected = GPIO.input(sensor_pin)
   
    if motion_detected:
        write_motion_sample()
        time.sleep(1)