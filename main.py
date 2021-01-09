from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.implicitly_wait(10)
driver.get("https://www.ozon.ru/")


myDynamicElement = driver.find_element_by_id('__ozon')

myDynamicElement = driver.find_element_by_name('search')

myDynamicElement = driver.find_element_by_class_name('c4u1')

myDynamicElement = driver.find_element_by_tag_name('input')

myDynamicElement = driver.find_element_by_link_text('Избранное')

element = WebDriverWait(driver, 10).until(
EC.presence_of_element_located((By.ID, "__ozon"))
)

element = WebDriverWait(driver, 10).until(
EC.title_is((By.CLASS_NAME, "c6u1"))
)

element = WebDriverWait(driver, 10).until(
EC.title_contains((By.CLASS_NAME, "c6d0"))
)

element = WebDriverWait(driver, 10).until(
EC.visibility_of_element_located((By.CLASS_NAME, "b6e2"))
)

element = WebDriverWait(driver, 10).until(
EC.visibility_of((By.CLASS_NAME, "b6e2"))
)

element = WebDriverWait(driver, 10).until(
EC.presence_of_all_elements_located((By.CLASS_NAME, "b6e2"))
)

element = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CLASS_NAME, "b6e2"))
)

element = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element_value((By.CLASS_NAME, "b6e2"))
)


element = WebDriverWait(driver, 10).until(
EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, "b6e2"))
)

element = WebDriverWait(driver, 10).until(
EC.invisibility_of_element_located((By.CLASS_NAME, "b6e2"))
)

element = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.CLASS_NAME, "b6e2"))
)
element = WebDriverWait(driver, 10).until(
EC.element_to_be_selected((By.CLASS_NAME, "b6e2"))

)element = WebDriverWait(driver, 10).until(
EC.element_located_to_be_selected((By.CLASS_NAME, "b6e2"))
)

)element = WebDriverWait(driver, 10).until(
EC.element_selection_state_to_be((By.CLASS_NAME, "b6e2"))
)
)element = WebDriverWait(driver, 10).until(
EC.element_located_selection_state_to_be((By.CLASS_NAME, "b6e2"))
)
)element = WebDriverWait(driver, 10).until(
EC.alert_is_present((By.CLASS_NAME, "b6e2"))
)