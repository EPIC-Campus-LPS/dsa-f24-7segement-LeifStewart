
import tm1637#type: ignore
import RPi.GPIO as GPIO 
import numpy as np
import time
from gpiozero import Button

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([18,24,23,16], GPIO.IN)
GPIO.setup([21,12],GPIO.OUT)
#Set up the display
tm = tm1637.TM1637(clk=24,dio=23)
clear = [0,0,0,0]

#Set up the light
light = GPIO.input(12)
#Set up the Button
button=GPIO.input(18)

#Main control system:
def main():
    while True:
        button = GPIO.input(18)
        if button == 1:
            GPIO.output(12, GPIO.HIGH)
            print("light on")
            seconds = stopwatch()
            GPIO.output(12, GPIO.LOW)
            print("light off")
            doomscrolling(seconds)
        time.sleep(0.1)

#Stopwatch Function
def stopwatch():
    seconds = 0
    while True:
        seconds += 1
        time.sleep(1)
        button=GPIO.input(18)
        if button == 1:
            break
    return seconds
        
def doomscrolling(s):
     tm.write(clear)
     time.sleep(1)
     tm.scroll(str(s),delay=250)
     time.sleep(2)
     print(s,"seconds")
#Scroll the time:
main()