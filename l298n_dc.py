# Python Script
# https://www.electronicshub.org/raspberry-pi-l298n-interface-tutorial-control-dc-motor-l298n-raspberry-pi/

import RPi.GPIO as GPIO          
from time import sleep
import time 
in1 = 24
in2 = 25
enA = 23
temp1=1

in3 = 27
in4 = 17
enB = 22

GPIO.setmode(GPIO.BCM)
#Setup Motor1 Pins
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(enA,GPIO.OUT)
GPIO.output(in1,GPIO.LOW)
GPIO.output(in2,GPIO.LOW)
p1=GPIO.PWM(enA,1000)

#Setup Motor2 Pins
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
GPIO.setup(enB,GPIO.OUT)
GPIO.output(in3,GPIO.LOW)
GPIO.output(in4,GPIO.LOW)
p2=GPIO.PWM(enB,1000)


p1.start(45)
p2.start(45)
time.sleep(0.5)
p1.start(25)
p2.start(25)
print("\n")
print("The default speed & direction of motor is LOW & Forward.....")
print("r-run s-stop f-forward b-backward l-low m-medium h-high e-exit")
print("\n")    

while(1):

    x=input()
    
    if x=='r':
        print("run")
        if(temp1==1):
            GPIO.output(in1,GPIO.LOW)
            GPIO.output(in2,GPIO.HIGH)
            GPIO.output(in3,GPIO.LOW)
            GPIO.output(in4,GPIO.HIGH)
            print("forward")
            p1.start(45)
            p2.start(45)
            time.sleep(0.5)
            p1.start(25)
            p2.start(25)
            x='z'
        else:
            GPIO.output(in1,GPIO.HIGH)
            GPIO.output(in2,GPIO.LOW)
            GPIO.output(in3,GPIO.HIGH)
            GPIO.output(in4,GPIO.LOW)
            print("backward")
            p1.start(45)
            p2.start(45)
            time.sleep(0.5)
            p1.start(25)
            p2.start(25)
            x='z'


    elif x=='s':
        print("stop")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.LOW)
        x='z'

    elif x=='f':
        print("forward")
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
        temp1=1
        p1.start(45)
        p2.start(45)
        time.sleep(0.5)
        p1.start(25)
        p2.start(25)
        x='z'

    elif x=='b':
        print("backward")
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
        temp1=0
        p1.start(45)
        p2.start(45)
        time.sleep(0.5)
        p1.start(25)
        p2.start(25)
        x='z'

    elif x=='l':
        print("low")
        p1.ChangeDutyCycle(25)
        p2.ChangeDutyCycle(25)
        x='z'

    elif x=='m':
        print("medium")
        p1.ChangeDutyCycle(50)
        p2.ChangeDutyCycle(50)
        x='z'

    elif x == 'i':
        print ("right")
        p1.ChangeDutyCycle(45)
        p2.ChangeDutyCycle(15)
        x = 'z'

    elif x == 'u':
        print ("left")
        p1.ChangeDutyCycle(15)
        p2.ChangeDutyCycle(45)
        x = 'z'
    
    elif x=='e':
        GPIO.cleanup()
        print("GPIO Clean up")
        break
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")
