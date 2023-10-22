#import winsound
import RPi.GPIO as GPIO
import time
import sys
import subprocess

import multi_switch

LED_GPIO = 18
SW_GPIO = 4
SW_GPIO2 = 12

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_GPIO, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(SW_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(SW_GPIO2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)

SwitchStatus = GPIO.input(SW_GPIO)
SwitchStatus2 = GPIO.input(SW_GPIO2)

def main():
    time.sleep(0.1)
    LastStatus = 1
    LastStatus2 = 1

    StartFlag = 0
    EndFlag = 0

    print("start")
    while True:
        try:
            SwitchStatus = GPIO.input(SW_GPIO)
            if SwitchStatus != LastStatus:
                print(SwitchStatus," IO4")
                if SwitchStatus == 0:
                    print("Code run")
                    time.sleep(0.2)

                    multi_switch.adb()
                    StartFlag = 1
                    EndFlag = 0

                LastStatus = SwitchStatus
        except KeyboardInterrupt:
            pass


        try:
            SwtichStatus2 = GPIO.input(SW_GPIO2)
            if SwitchStatus2 != LastStatus2:
                print(SwitchStatus, " IO12")
                if SwitchStatus2 == 0 and StartFlag == 1:
                    print("Code exit")
                    EndFlag = 1
                    time.sleep(0.2)

                    StartFlag = 0
                LastStatus2 = SwtichStatus2
        except KeyboardInterrupt:
            pass
        if EndFlag == 1:
            break

    if EndFlag == 0:
        sw_led(0)
        #end music
        GPIO.cleanup()
        sys.exit()

if __name__ == "__main__":
    main()

