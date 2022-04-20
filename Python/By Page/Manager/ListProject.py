from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
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
email.send_keys("aufar.rizqi@artajasa.co.id")

pwd = kodok.find_element_by_id("password")
pwd.send_keys("opensesaMe16?!")

login = kodok.find_element_by_name("login")
login.click()

#=======================CHOOSE ROLE==============================
try:
	#pilih role yg mau dimasukkin. pilihan id: login_manager / login_admin / login_engineer
	role = WebDriverWait(kodok, 10).until(
		EC.presence_of_element_located((By.ID, "login_manager"))
	)

	role.click()	#klik tombol rolenya

	listp = WebDriverWait(kodok, 10).until(
		EC.presence_of_element_located((By.ID, "listpage"))
	)

	listp.click()	#klik tombol rolenya

#########################################################################Generate Excel
	element = WebDriverWait(kodok, 10).until(
		EC.presence_of_element_located((By.ID, "tabel"))
	)

	excel = element.find_element_by_xpath("//a[@href='/manager/projects/export']")
	excel.click()

#########################################################################Logout
	element = kodok.find_element_by_id("rn-dropdown")
	element.click()

	logout = element.find_element_by_xpath("//a[@class='dropdown-item' and @href='/logout']")
	logout.click()

finally:
	time.sleep(3)
	kodok.quit()