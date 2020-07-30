from picamera import PiCamera
from time import sleep
camera = PiCamera()
camera.start_preview()
sleep(2)
camera.stop_preview()
camera.capture('/home/pi/Desktop/image.jpg')


        