from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

# init driver
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()

# open the url
driver.get('https://staging.tryproven.com')
driver.find_element(By.CSS_SELECTOR, ".src-components-shared-proven-button-___style__text___3aBIJ").click()

wait = WebDriverWait(driver, 20)
wait.until(EC.invisibility_of_element((By.CSS_SELECTOR, ".src-components-quiz-transition-___transition__transition___1JiNQ h4")))

driver.find_element(By.CSS_SELECTOR, ".src-components-quiz-inputs-select-input-container-___select-input-container__label-container___2RsPZ").click()

# wait for 4 sec
sleep(4)



driver.quit()