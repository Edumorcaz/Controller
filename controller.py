from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


#PATH = "C:\\Users\\214012\\Downloads\\chromedriver_win32\\chromedriver.exe"
PATH = "\\chromedriver_win32\\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("http://192.168.1.254/K_1")
data = driver.page_source
Start_pre=data.find("<pre>")
End_pre=data.find("</pre>")
print(data[Start_pre+5:End_pre])

##data=driver.page_source.find("script")
##print(data)
##search=driver.find_element_by_name("script")
##print(search.text)

driver.quit()

