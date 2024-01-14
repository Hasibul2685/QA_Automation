from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a Chrome webdriver instance
driver = webdriver.Chrome()
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver

def find(identifier, selector, wait_time, driver, find_all=True):
    """
    Find the first element or all elements based on the identifier and selector,
    with the specified explicit wait time.
    Parameters:
    - identifier (str): The type of identifier to be used (e.g., ID, NAME, XPATH).
    - selector (str): The value of the identifier (e.g., the ID value, XPATH expression).
    - wait_time (float): The explicit wait time in seconds.
    - driver (webdriver): The Selenium WebDriver instance.
    - find_all (bool): If True, find all matching elements; if False, find the first one. Default is True.
    Returns:
    - If find_all is True, returns a list of elements; if False, returns the first matching element.
    - Returns None if no elements are found within the specified wait time.
    """
    by_map = {
        "ID": By.ID,
        "NAME": By.NAME,
        "XPATH": By.XPATH,
        "LINK_TEXT": By.LINK_TEXT,
        "PARTIAL_LINK_TEXT": By.PARTIAL_LINK_TEXT,
        "TAG_NAME": By.TAG_NAME,
        "CLASS_NAME": By.CLASS_NAME,
        "CSS_SELECTOR": By.CSS_SELECTOR,
    }
    by = by_map.get(identifier.upper())
    if by is None:
        raise ValueError("Invalid identifier. Supported values are: ID, NAME, XPATH, LINK_TEXT, PARTIAL_LINK_TEXT, TAG_NAME, CLASS_NAME, CSS_SELECTOR")
    try:
        if find_all:
            elements = WebDriverWait(driver, wait_time).until(
                EC.presence_of_all_elements_located((by, selector))
            )
        else:
            element = WebDriverWait(driver, wait_time).until(
                EC.presence_of_element_located((by, selector))
            )
    except TimeoutError:
        if find_all:
            return []
        else:
            return None
    return elements if find_all else element

# URL of the login page
url = 'https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'

# Open the URL in the browser
driver.get(url)
find("CLASS_NAME",'oxd-input', 5,driver)
# Locate the username and password input fields by class name
username_input = find("CLASS_NAME",'oxd-input', 2,driver)[0]
password_input =  find("CLASS_NAME",'oxd-input', 2,driver)[1]

# Enter the username and password
username_input.send_keys('Admin')
password_input.send_keys('admin123')

# Locate the login button by class name
login_button = driver.find_element(By.CLASS_NAME, 'oxd-button')

# Click the login button
login_button.click()

# Close the browser window (you may want to remove this line if you want to keep the browser open for further actions)
'''
# driver.quit()
'''
