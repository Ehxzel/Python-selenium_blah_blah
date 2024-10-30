from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


url = "https://www.google.com"
option_  = Options()
option_.add_argument("--incognito")
#options.add_argument("--headless")

driver = webdriver.Chrome(options=option_)
driver.maximize_window()
action = ActionChains(driver)

# action.click()
# action.move()

driver.get(url)

# search_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, 'q')))
gmail_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="gb"]/div/div[1]/div/div[1]/a')))
gmail_click.click()

sign_in_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/header/div/div/div/a[2]')))
sign_in_click.click()

search_text = "ehysoft@gmail.com"
#input_field_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Identifier"))).send_keys(search_text, Keys.ENTER)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "identifier"))).send_keys(search_text, Keys.ENTER)

# input_field_text.click()
#input_field_text.send_keys(search_text, Keys.ENTER)

sign_in_retry_click = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="next"]/div/div/a')))
action.move_to_element(to_element = sign_in_retry_click)
time.sleep(5)
sign_in_retry_click.click()

time.sleep(7)

search_text = "ehysoft@gmail.com"
#input_field_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Identifier"))).send_keys(search_text, Keys.ENTER)
WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "identifier"))).send_keys(search_text, Keys.ENTER)

time.sleep(7)

driver.quit()

