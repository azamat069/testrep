from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math

# driver = webdriver.Chrome()
# wait = WebDriverWait(driver, 20)
# driver.get('http://suninjuly.github.io/explicit_wait2.html')
#
# price = wait.until(EC.text_to_be_present_in_element((By.ID, 'price'), '100'))
# driver.find_element(By.ID, 'book').click()
#
# x = driver.find_element(By.ID, 'input_value').text
# value = math.log((abs(12 * math.sin(int(x)))))
# answer = driver.find_element(By.ID, 'answer').send_keys(value)
# driver.find_element(By.ID, 'solve').click()


driver = webdriver.Chrome()
driver.get('http://suninjuly.github.io/math.html')
people_radio = driver.find_element(By.ID, "peopleRule")
people_checked = people_radio.get_attribute("checked")
print("value of people radio: ", people_checked)
assert people_checked is not None, "People radio is not selected by default"
