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
driver = webdriver.Firefox(firefox_profile=profile)

driver.get("http://tariffdata.wto.org/ReportersAndProducts.aspx")

filt = driver.find_element_by_id("ctl00_ContentView_LinkButtonFilter")
filt.click()
s1= Select(driver.find_element_by_id('ctl00_ContentView_DropDownListNumberYears'))
s1.select_by_index(4)

ok = driver.find_element_by_id("ctl00_ContentView_OkButton")
ok.click()


time.sleep(1)

albania = driver.find_element_by_id("ctl00_ContentView_rn0CheckBox")
albania.click()

time.sleep(0.5)

submit = driver.find_element_by_id("ctl00_ContentView_pn0CheckBox")
submit.click()


driver.get("http://tariffdata.wto.org/TariffList.aspx")

csv = driver.find_element_by_id("ctl00_ContentView_Label1")
csv.click()