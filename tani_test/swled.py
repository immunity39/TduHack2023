import RPi.GPIO as GPIO
import time
import sys

SW_GPIO = 5
LED_GPIO = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(SW_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_GPIO, GPIO.OUT, initial=GPIO.LOW)

SW_cnt = 0
SW_flg = False
LED_cnt = 1
LED_flg = True

def main():
    global SW_flg
    global LED_flg
    
    status = 0
    LED_status = 1
    resume = 0
    loop = 0

    print("start")
    try:
        GPIO.add_event_detect(SW_GPIO, GPIO.FALLING, bouncetime=100)
        GPIO.add_event_callback(SW_GPIO, SW_pressed)

        while True:
            time.sleep(0.1)
            if LED_flg == False:
                status = 1
                break
            elif LED_flg == True and loop < 10:
                loop += 1
                LED_set(LED_status)
            elif loop >= 10:
                LED_status = abs(1 - LED_status)
                print("loop reset")
                print("LED status: ", LED_status)
                loop = 0

            LED_flg = True
    except KeyboardInterrupt:
        print("output yo!")

    GPIO.cleanup()
    return 0

def SW_pressed(gpio_no):
    global SW_flg
    global LED_flg
    print("onput sw")
    LED_flg = False

def LED_set(LED_status):
    if LED_status == 0:
        print("led low")
        GPIO.output(LED_GPIO, GPIO.LOW)
    else:
        print("led high")
        GPIO.output(LED_GPIO, GPIO.HIGH)

if __name__=="__main__":
    sys.exit(main())

