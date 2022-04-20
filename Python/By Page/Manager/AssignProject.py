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

	assign = WebDriverWait(kodok, 10).until(
		EC.presence_of_element_located((By.ID, "assignpage"))
	)

	assign.click()	#klik tombol rolenya
############################################################################Assign New Project
	pname = "T3st @ss16n pR0j3ct?! (soon deleted)"
#===========================================================================PIC
	element = WebDriverWait(kodok, 10).until(
		EC.presence_of_element_located((By.ID, "id_user"))
	)

	select = Select(element)
	select.select_by_visible_text("Yudha Bagus Bayu Pratidana")
#==========================================================================Produk
	element = kodok.find_element_by_id("id_product")

	select = Select(element)
	select.select_by_visible_text("Mynt")
#=========================================================================Jenis Project
	element = kodok.find_element_by_id("id_ptype")


	select = Select(element)
	select.select_by_visible_text("Sertifikasi")
#=========================================================================Mitra
	element = kodok.find_element_by_id("id_mitra")


	select = Select(element)
	select.select_by_visible_text("Bank Mandiri")
#=========================================================================Nama Project
	textbox = kodok.find_element_by_id("nama_project")

	textbox.send_keys(pname) 
#=========================================================================Submit data	
	select = kodok.find_element_by_id("btn-submit")
	select.click()

##########################################################################Handover Project
	element = WebDriverWait(kodok, 10).until(
		EC.presence_of_element_located((By.XPATH, "//ul[@role='tablist']"))
	)

	handover = element.find_element_by_id("custom-tabs-three-profile-tab")
	handover.click() 
#===========================================================================PIC Original
	time.sleep(4)
	element = WebDriverWait(kodok, 10).until(
		EC.presence_of_element_located((By.ID, "PIC2"))
	)

	select = Select(element)
	select.select_by_visible_text("Yudha Bagus Bayu Pratidana")
#=========================================================================Nama Project
	element = WebDriverWait(kodok, 10).until(
		EC.presence_of_element_located((By.ID, "nama_project2"))
	)

	select = Select(element)
	select.select_by_visible_text(pname)
#=========================================================================PIC Handover
	time.sleep(2)
	element = kodok.find_element_by_id("PIChandover")


	select = Select(element)
	select.select_by_visible_text("Hadi Santoso")
#=========================================================================Submit data handover	
	select = kodok.find_element_by_id("btn-submithandover")
	select.click()

##########################################################################Logout
	time.sleep(4)
	element = kodok.find_element_by_id("rn-dropdown")
	element.click()

	logout = element.find_element_by_xpath("//a[@class='dropdown-item' and @href='/logout']")
	logout.click()

finally:	#If done, then quit
	time.sleep(3)	#wait for 3 second
	kodok.quit()	#close browser