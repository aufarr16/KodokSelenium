from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import warnings
warnings.filterwarnings("ignore")

PATH = "C:\Program Files (x86)\chromedriver.exe"
kodok = webdriver.Chrome(PATH)

kodok.get("http://kodok.me/")					#open website Kodok
print(kodok.title)

#==========================LOGIN=================================
email = kodok.find_element_by_id('email')
email.send_keys("aufar.rizqi@artajasa.co.id")	#input email

pwd = kodok.find_element_by_id("password")		#input pass
pwd.send_keys("opensesaMe16?!")

login = kodok.find_element_by_name("login")		#cari tombol login
login.click()									#click tombol login

#=======================CHOOSE ROLE==============================
try:
	#pilih role yg mau dimasukkin. pilihan id: login_manager / login_admin / login_engineer
	role = WebDriverWait(kodok, 10).until(
		EC.presence_of_element_located((By.ID, "login_engineer"))
	)

	role.click()	#klik tombol rolenya
#====================================================================================Logout
	element = WebDriverWait(kodok, 10).until(
		EC.presence_of_element_located((By.ID, "rn-dropdown"))
	)
	element.click()

	logout = element.find_element_by_xpath("//a[@class='dropdown-item' and @href='/logout']")
	logout.click()

finally:	#if all done, then
	time.sleep(3)
	kodok.quit()	#close browser

