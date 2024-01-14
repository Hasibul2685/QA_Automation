from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a Chrome webdriver instance
driver = webdriver.Chrome()

# URL of the login page
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

# Open the URL in the browser
driver.get(url)

# Locate the username and password input fields by class name
username_input = driver.find_elements(By.CLASS_NAME, 'oxd-input')[0]
password_input = driver.find_elements(By.CLASS_NAME, 'oxd-input')[1]

# Enter the username and password
username_input.send_keys('Admin')
password_input.send_keys('admin123')

# Locate the login button by class name
login_button = driver.find_element(By.CLASS_NAME, 'oxd-button')

# Click the login button
login_button.click()

# Close the browser window (you may want to remove this line if you want to keep the browser open for further actions)
driver.quit()
