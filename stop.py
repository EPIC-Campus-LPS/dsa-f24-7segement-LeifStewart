
import RPi.GPIO as GPIO 
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup([23,16,24], GPIO.OUT)
GPIO.output(23,GPIO.LOW)
GPIO.output(24,GPIO.LOW)
GPIO.output(16,GPIO.LOW)