import time
import raspi
import subprocess

def popup(app_process):
    #print("tmp process exit")
    #print(app_process)
    raspi.LED_swiching(app_process)
