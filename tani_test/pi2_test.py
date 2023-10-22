import RPi.GPIO as GPIO
import time
import sys

SW_GPIO = 5
GPIO.setmode(GPIO.BCM)

GPIO.setup(SW_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(0.1)

while True:
    try:
        SwitchStatus = GPIO.input(SW_GPIO)
        print(SwitchStatus)
        time.sleep(0.3)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()

GPIO.cleanup()
sys.exit()

