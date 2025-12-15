from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

#options = Options()
#options.add_argument("--start-maximized")

service = Service("D:/test/msedgedriver.exe")
#driver = webdriver.Edge(service=service, options=options)
driver = webdriver.Edge(service=service)

driver.implicitly_wait(10)

driver.get('https://omnidesk.newgen.co.in/')

driver.maximize_window()

ele=driver.find_element(By.XPATH,"//a[@onclick='fprismDirect()']")
ele.click()
windowid=driver.window_handles[0]
driver.switch_to.window(windowid)

time.sleep(10)