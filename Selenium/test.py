from selenium import webdriver
driver = webdriver.Chrome('C:\\Users\\da.long\\Software Package\\chromedriver')
driver.get("https://www.baidu.com")

input = driver.find_element_by_css_selector('#kw')
input.send_keys("IQVIA")

button = driver.find_element_by_css_selector('#su')
button.click()
