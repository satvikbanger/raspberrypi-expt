import RPi.GPIO as gpio
import time
def init():    
    gpio.setmode(gpio.BCM)
    gpio.setup(17, gpio.OUT)
    gpio.setup(22, gpio.OUT)
    gpio.setup(23, gpio.OUT)
    gpio.setup(24, gpio.OUT)
def test_pin(sec, pin_num, value):
    init()
    gpio.output(pin_num, value )
    time.sleep(sec)
    gpio.cleanup() 
seconds = 10
print("test_pin")
for i in range (10):
    if i%2:
        print ("True")
        test_pin(seconds, 17, True)
    else:
        print ("False")
        test_pin(seconds, 17, False)

