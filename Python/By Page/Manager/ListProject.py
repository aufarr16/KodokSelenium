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
	#excel.click()
#########################################################################Filter
	element = kodok.find_element_by_id("filter")
	extend = element.find_element_by_xpath("//button[@class='btn btn-tool']")		#find the "+" button to extend

	extend.click()																	#extend

	filters = WebDriverWait(kodok, 10).until(
		EC.presence_of_element_located((By.XPATH, "//div[@class='card-body']"))		#take the filter body to access the dropdown
	)
#========================================================================PIC
	dropdown = filters.find_element_by_id("filter-pic")								#ambil filter pic
	select = Select(dropdown)

	select.select_by_visible_text("YBP")
#========================================================================Product
	dropdown = filters.find_element_by_id("filter-product")							#ambil filter product
	select = Select(dropdown)

	select.select_by_visible_text("BersamaKU")
#========================================================================Mitra
	dropdown = filters.find_element_by_id("filter-mitra")							#ambil filter mitra
	select = Select(dropdown)

	select.select_by_visible_text("Western Union")
#========================================================================Project
	dropdown = filters.find_element_by_id("filter-namap")							#ambil filter nama project

	dropdown.send_keys("Remittance")
	dropdown.clear()																#kalo mau ngosongin filter bentuk textbox
#========================================================================Jenis Project
	dropdown = filters.find_element_by_id("filter-ptype")							#ambil filter jenis project
	select = Select(dropdown)

	select.select_by_visible_text("Sertifikasi")
#========================================================================Status
	dropdown = filters.find_element_by_id("filter-pstat")							#ambil filter status project
	select = Select(dropdown)

	select.select_by_visible_text("Pengujian Done")
	time.sleep(2)
	select.select_by_visible_text("Drop")
	#select.select_by_visible_text("-")												#kalo mau ngosongin filter bentuk select
#########################################################################Logout
	time.sleep(3)
	element = kodok.find_element_by_id("rn-dropdown")
	element.click()

	logout = element.find_element_by_xpath("//a[@class='dropdown-item' and @href='/logout']")
	logout.click()

finally:
	time.sleep(3)
	kodok.quit()