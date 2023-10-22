import RPi.GPIO as GPIO
import time
import sys
import subprocess
import app
import pygame

# GPIO setting
SW_GPIO = 5
LED_GPIO = 13

GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)
GPIO.setup(SW_GPIO, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_GPIO, GPIO.OUT, initial=GPIO.LOW)

app_process = None

# Flag, counter
SW_cnt = 0
SW_flg = False
LED_cnt = 0
LED_flg = False
Prog_flg = False

pygame.mixer.init()
sound = pygame.mixer.Sound("maou_se_onepoint28.wav")

def main():
    # global set
    global SW_flg
    global SW_cnt
    global LED_flg
    global LED_cnt
    global app_process
    global Prog_flg

    print("process run")
    try:
        # set gpio event
        GPIO.add_event_detect(SW_GPIO, GPIO.FALLING, bouncetime=100)
        GPIO.add_event_callback(SW_GPIO, SW_pressed)

        # processing
        while not Prog_flg:
            time.sleep(0.1)

    except KeyboardInterrupt:
        print("except in raspi.py")

    Prog_flag = False
    print("end & cleanup")
    GPIO.cleanup()
    return 0

def SW_pressed(gpio_no):
    print("sw press")
    global SW_flg
    global SW_cnt
    global LED_flg
    global LED_cnt
    global app_process
    global Prog_flg

    if LED_flg == True:
        print("prog exit")
        SW_flg = False
        SW_cnt = 0
        LED_flg = False
        LED_cnt = 0
        Prog_flg = True
    else:
        if SW_cnt == 0:
            #print("flask run")
            if app_process is None:
                app_process = subprocess.Popen(["flask", "run"])
                time.sleep(0.5)
            SW_cnt += 1
            app.run_script(app_process)

def LED_swiching(app_process):
    print("led swiching")
    global LED_flg
    global LED_cnt

    LED_flg = True
    print(LED_flg)
    print(LED_cnt)

    app_process.terminate()

    SW_status = GPIO.input(SW_GPIO)
    #print("now sw status: ", SW_status)

    LED_status = 1
    loop = 0

    try:
        sound.play(loops=-1)
        while LED_flg == True:
            time.sleep(0.1)

            # SW_GPIOの状態を確認してプログラム終了
            SW_status = GPIO.input(SW_GPIO)
            if SW_status == 0:
                print("SW pressed, exiting program")
                break

            # LEDの点滅
            if loop < 10:
                LED_set(LED_status)
                loop += 1
            else:
                LED_status = abs(1 - LED_status)
                print("LED status: ", LED_status)
                loop = 0

    except KeyboardInterrupt:
        print("except LED swiching")
    sound.stop()
    GPIO.output(LED_GPIO, GPIO.LOW)
    sys.exit()

def LED_set(LED_status):
    if LED_status == 0:
        print("LED LOW")
        GPIO.output(LED_GPIO, GPIO.LOW)
    else:
        print("LED HIGH")
        GPIO.output(LED_GPIO, GPIO.HIGH)

if __name__ == "__main__":
    sys.exit(main())

