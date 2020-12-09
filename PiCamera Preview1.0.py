#import functions
from picamera import PiCamera
from time import sleep

#set variable 
camera = PiCamera()

#show cameras view on screen
camera.start_preview()
sleep(2)
camera.stop_preview()

#take photo
camera.capture('/home/pi/Desktop/image.jpg') 
