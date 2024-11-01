import tm1637
import time
import numpy as np
from datetime import datetime
from gpiozero import CPUTemperature
#set all of the pins
tm = tm1637.TM1637(clk=24, dio = 23)
clear = [0,0,0]
#Scroll name
tm.write(clear)
time.sleep(1)
s = input("What is your name: ")
tm.scroll(s)
time.sleep(2)

