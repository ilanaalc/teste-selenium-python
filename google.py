from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()

driver.get("https://google.com.br")
print(driver.current_url)
print(driver.title)
print(driver.capabilities["browserVersion"])

element = driver.find_element("name","q")
element.click()
element.send_keys("Pantera Negra")
element.submit()

assert driver.title == "Pantera Negra - Pesquisa Google"

sleep(10)



driver.close()