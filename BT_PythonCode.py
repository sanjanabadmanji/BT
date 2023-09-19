from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a webdriver instance (you need to specify the path to your WebDriver)
driver = webdriver.Chrome()

# 1. Launch the URL
driver.get("https://www.bt.com/")
driver.maximize_window()

# 2. Click Accept Cookie Button
try:
    iframe_element = WebDriverWait(driver, 10).until(
        EC.frame_to_be_available_and_switch_to_it((By.CLASS_NAME, 'truste_popframe'))
    )
    accept_cookie_button = driver.find_element(By.XPATH, "//a[text()='Accept all cookies']")
    accept_cookie_button.click()
    time.sleep(6)
finally:
    pass

# 3. Hover over the Mobile menu
mobile_menu = driver.find_element(By.LINK_TEXT, "Mobile")
actions = ActionChains(driver)
actions.move_to_element(mobile_menu).perform()

# 4. Click on "Mobile phones" from the mobile menu
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "(//a[text()='Mobile phones'])[1]"))).click()

# 5. Verify the number of banners
banners = driver.find_elements(By.CLASS_NAME, "flexpay-card_text_container__KQznu")
assert len(banners) >= 3, "Number of banners is less than 3"

# 6. Scroll down and click "View SIM only deals"
driver.execute_script("window.scrollTo(0, window.scrollY + 500)")
driver.find_element(By.LINK_TEXT, "View SIM only deals").click()
time.sleep(7)

# 7. Validate the title for the new page
page_title = "SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile"
assert page_title in driver.title, f"Expected title '{page_title}' not found"

# 8. Validate the specific text on the page
expected_text = "30% off and double data was 125GB 250GB Essential Plan, was £27 £18.90 per month"
text_validate = driver.page_source
assert expected_text in text_validate, f"Expected text '{expected_text}' not found on the page"

# 9. Close the browser and exit
driver.quit()

