from selenium import webdriver
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service 
from time import sleep 

path1 = '/usr/bin/chromedriver'

options1 = ChromeOptions() 
driver1 = Chrome( service=Service(path1), options=options1 )

url1 = 'https://www.google.com'

search_word1 = "raspberry pi" 

driver1.get( url1 ) 

driver1.implicitly_wait( 5 ) 
elem1 = driver1.find_element(By.NAME, 'q')
elem1.clear()
elem1.send_keys( search_word1 + Keys.ENTER ) 

sleep( 10 ) 

driver1.quit()
