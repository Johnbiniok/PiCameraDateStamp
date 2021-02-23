from picamera import PiCamera
from time import sleep
from gpiozero import Button
from datetime import datetime



button = Button(17)
camera = PiCamera()

camera.start_preview()
frame = 1
while True:
    try:
        button.wait_for_press()
        camera.start_preview()
        sleep(2)
        camera.stop_preview()
        camera.capture('/home/pi/animation/frame%03d.jpg' % frame)
        camera.annotate_text_size = 50 # (values 6 to 160, default is 32)
        camera.annotate_text = datetime.now().strftime('%A %d %b %Y %H:%M')
        frame += 1
    except KeyboardInterrupt:
        camera.stop_preview()
        break