import RPi.GPIO as GPIO
import time
import sys
import subprocess
from selenium import webdriver
from app import run_script

# LED_GPIO set 4
SW1_GPIO = 4
SW2_GPIO = 12

# 制御用
GPIO.setmode(GPIO.BOARD)

# GPIO.IN で入力モード
# setting
GPIO.setup(SW1_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW2_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)

time.sleep(0.1)

LastStatus = 1

app_process = subprocess.Popen(["flask", "run"])
print("starting switch status:", LastStatus)

# Switching Button
print("start switching programm")
while True:
    try:
        # read GPIO 4 pin
        SwitchStatus = GPIO.input(SW1_GPIO)
        if SwitchStatus != LastStatus:
            print(SwitchStatus)
            if SwitchStatus == 0:
                print("Code run")
                time.sleep(1)

                GPIO.cleanup()
                result = run_script(app_process)
            LastStatus = SwitchStatus

        time.sleep(0.3)
    except KeyboardInterrupt:
        pass

GPIO.cleanup()
sys.exit()

