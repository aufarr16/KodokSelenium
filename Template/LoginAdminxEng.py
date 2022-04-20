from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import by
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import warnings
warnings.filterwarnings("ignore")

PATH = "C:\Program Files (x86)\chromedriver.exe"
kodok = webdriver.Chrome(PATH)

kodok.get("http://kodok.me/")					#open website Kodok
print(kodok.title)

#=======================LOGIN====================================
email = kodok.find_element_by_id('email')
email.send_keys("aufar.rizqi@artajasa.co.id")

pwd = kodok.find_element_by_id("password")
pwd.send_keys("opensesaMe16?!")

login = kodok.find_element_by_name("login")
login.click()

#==========================CLOSE=================================
time.sleep(5)	#delay before closing browser

kodok.quit()