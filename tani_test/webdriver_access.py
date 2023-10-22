import subprocess
from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
import time

from app import run_script

app_process = subprocess.Popen(["flask", "run"])

time.sleep(5)

result = run_script()
print(result)
