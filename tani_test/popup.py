import RPi.GPIO as GPIO
import time
import sys
import subprocess

LED_GPIO = 18
SW_GPIO = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_GPIO, GPIO.OUT)
GPIO.setwarnings(False)
GPIO.setup(SW_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

SwitchStatus = GPIO.input(SW_GPIO)

def sw_led(status):
    if status == 1:
        GPIO.output(LED_GPIO, GPIO.HIGH)
    else:
        GPIO.output(LED_GPIO, GPIO.LOW)

def sw_callback(channel):
    global SwitchStatus
    SwitchStatus = GPIO.input(SW_GPIO)

GPIO.add_event_detect(SW_GPIO, GPIO.FALLING, callback=sw_callback, bouncetime=200)

def popup(app_process):
    print("process exit")
    LastStatus = 1
    LedStatus = 1

    # start music
    try:
        while SwitchStatus == 1:
            sw_led(LedStatus)
            LedStatus = 1 - LedStatus
            time.sleep(1)
        sw_led(0)
    except KeyboardInterrupt:
        pass

    if SwitchStatus == 0:
        sw_led(0)
        # end music
        GPIO.cleanup()
        app_process.terminate()
        sys.exit()
