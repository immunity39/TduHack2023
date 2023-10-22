import RPi.GPIO as GPIO
import sys
import time

LED_GPIO = 13

GPIO.setmode(GPIO.BCM)

GPIO.setup(LED_GPIO, GPIO.OUT, initial=GPIO.LOW)

LedFlag = 1

while True:
    try:
        if LedFlag == 1:
            GPIO.output(LED_GPIO, GPIO.HIGH)
            time.sleep(1)
            LedFlag = 0
        else:
            GPIO.output(LED_GPIO, GPIO.LOW)
            time.sleep(1)
            LedFlag = 1
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit()

GPIO.cleanup()
sys.exit()

