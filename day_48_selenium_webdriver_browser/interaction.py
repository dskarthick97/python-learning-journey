"""
Scrapping wikipedia's main page.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


# instanstiate the chrome web driver
chrome_driver = webdriver.Chrome(
    executable_path="/home/karthicksabari/karthick.dhilip/tools/chromedriver_linux64/chromedriver"
)

# extract the article count data from https://en.wikipedia.org/wiki/Main_Page
# chrome_driver.get("https://en.wikipedia.org/wiki/Main_Page")
# article_count = chrome_driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# article_count.click()

# alternate way of achieving click action
# all_portals_link = chrome_driver.find_element(By.LINK_TEXT, "All portals")
# all_portals_link.click()

# filling the form and click enter
chrome_driver.get("http://secure-retreat-92358.herokuapp.com/")
first_name_field = chrome_driver.find_element(By.NAME, "fName")
first_name_field.send_keys("Karthick Sabari")

last_name_field = chrome_driver.find_element(By.NAME, "lName")
last_name_field.send_keys("Dhilip Sudhakar")

email_field = chrome_driver.find_element(By.NAME, "email")
email_field.send_keys("dskarthicksabari@gmail.com")

sign_up_button = chrome_driver.find_element(By.TAG_NAME, "button")
sign_up_button.click()

chrome_driver.quit()
