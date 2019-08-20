from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.select import Select


profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # custom location
profile.set_preference('browser.download.manager.showWhenStarting', False)
profile.set_preference('browser.download.dir', '/tmp')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/download')
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/octet-stream')
profile.set_preference("browser.link.open_newwindow", 3)
profile.set_preference("browser.link.open_newwindow.restriction", 2)

driver = webdriver.Firefox(firefox_profile=profile)

countries = ['0', '2', '9', '13', '20', '27', '34', '41', '48', '50', '57', '64', '71', '74', '81', '88', '95', '102', '109', '116', '122', '129', '136', '143', '150', '157', '164', '171', '178', '185', '192', '199', '206', '213', '220', '227', '234', '240', '246', '253', '260', '267', '274', '281', '288', '295', '301', '308', '315', '322', '329', '336', '343', '350', '357', '364', '371', '378', '385', '392', '399', '406', '412', '419', '426', '433', '440', '447', '454', '461', '467', '474', '481', '488', '495', '502', '508', '515', '521', '524', '531', '538', '545', '552', '559', '566', '572', '579', '586', '593', '600', '607', '614', '621', '628', '635', '642', '649', '656', '663', '670', '677', '684', '691', '698', '705', '712', '719', '726', '733', '740', '745', '752', '759', '766', '773', '780', '787', '794', '801', '808', '812', '818', '825', '832', '838', '842', '849', '856', '863', '870', '877', '884', '891', '898', '905', '912', '919', '926', '933', '940', '947', '954', '961', '968', '975', '982', '989', '996', '1001', '1008']

driver.get("http://tariffdata.wto.org/ReportersAndProducts.aspx")


filt = driver.find_element_by_id("ctl00_ContentView_LinkButtonFilter")
filt.click()
s1= Select(driver.find_element_by_id('ctl00_ContentView_DropDownListNumberYears'))
s1.select_by_index(4)
ok = driver.find_element_by_id("ctl00_ContentView_OkButton")
ok.click()
time.sleep(2)




a = driver.execute_script("CheckAllProducts()")


for x in countries:




	country = driver.find_element_by_id("ctl00_ContentView_rn" + x + "CheckBox")
	country.click()

	time.sleep(0.5)


	driver.get("http://tariffdata.wto.org/TariffList.aspx")


	if "Download limit" in driver.page_source: 
		print(x)
		continue


	csv = driver.find_element_by_id("ctl00_ContentView_Label1")
	csv.click()

	#submit = driver.find_element_by_id("ctl00_ContentView_pn0CheckBox")
	#submit.click()

	time.sleep(5)

	driver.execute_script('''window.open("http://tariffdata.wto.org/ReportersAndProducts.aspx","_blank");''')

	country = driver.find_element_by_id("ctl00_ContentView_rn" + x + "CheckBox")
	country.click()

	time.sleep(1)

	exit()



