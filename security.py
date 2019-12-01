import RPi.GPIO as GPIO
import time
from time import sleep
from picamera import PiCamera
 
SENSOR_PIN = 23
 
GPIO.setmode(GPIO.BCM)
GPIO.setup(SENSOR_PIN, GPIO.IN)

camera = PiCamera()
 
def motion_detected(channel):
    print('motion detected, turning camera on.')
    camera.start_preview()
    sleep(10)
    camera.stop_preview()
    print('turning camera off.')
    
 
try:
    print('listening...bleep bloop.')
    GPIO.add_event_detect(SENSOR_PIN , GPIO.RISING, callback=motion_detected)
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print('shutting down... bleep bloop.')
GPIO.cleanup()
