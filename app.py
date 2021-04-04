import os
import time
import wget
from urllib.parse import urlparse
import pathlib
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("https://www.instagram.com/")
wait = WebDriverWait(driver, 10)

# Accept The cookies
accept_cookies = wait.until(EC.element_to_be_clickable((
    By.XPATH, 
    "//button[contains(text(), 'Accept')]"
    ))).click()

# Get the username
username = wait.until(EC.element_to_be_clickable((By.NAME, "username")))
#get the password
password = wait.until(EC.element_to_be_clickable((By.NAME, "password")))


# Cleare the username and password fields
username.clear()
password.clear()
# Send the username and password keys
username.send_keys('queen_of_coin')
password.send_keys('myteddyjune16')

#get the Login button
login = wait.until(EC.element_to_be_clickable((
    By.CSS_SELECTOR, 
    "button[type='submit']"
    ))).click()

# Click on Not Now Button after Login
not_now = wait.until(EC.element_to_be_clickable((
    By.XPATH, 
    "//button[contains(text(), 'Not Now')]"
    ))).click()

# Click on Not Now Button again
not_now_two = wait.until(EC.element_to_be_clickable((
    By.XPATH, 
    "//button[contains(text(), 'Not Now')]"
    ))).click()

# Search Box
search_box = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Search']")))

# Cleare the search Box
search_box.clear()
# Search a particular user
search_term = 'swedishtenor'
search_box.send_keys(search_term)

# Press Enter to saerch the term
# swedishtenor
search_box_enter = wait.until(EC.element_to_be_clickable((
    By.XPATH, 
    "//div[contains(text(), '{}')]".format(search_term)
    ))).click()

# Target all images

js_cript = 'window.scrollTo(0, 4000);'
driver.execute_script(js_cript)

# Get element by tag name
# sleep for 10 sec
time.sleep(10)
images = driver.find_elements_by_tag_name('img')

images = [image.get_attribute("src") for image in images]

# navigate to the current working directory
path = os.getcwd()
path = os.path.join(path, search_term)
# Make directory
file = pathlib.Path(search_term)
if file.exists():
    pass
else:
    os.mkdir(path)

# Download each of the file
for image_url in images:
    # get the image name
    image_name = os.path.basename(urlparse(image_url).path) 
    # Download the actual image
    wget.download(image_url, "{}/{}".format(path, image_name))

print("The Instagram Profile Pictures downloaded sucessfully!")

