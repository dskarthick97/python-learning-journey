"""
Webscrapping using selenium webdriver.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By


# instanstiate the chrome web driver
chrome_driver_path = (
    "/home/karthicksabari/karthick.dhilip/tools/chromedriver_linux64/chromedriver"
)

chrome_driver = webdriver.Chrome(executable_path=chrome_driver_path)

# extract the upcoming events time and name as a dict from https://www.python.org/
chrome_driver.get("https://www.python.org/")
event_times = chrome_driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = chrome_driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {
    key: {"time": value[0].text, "name": value[1].text}
    for key, value in enumerate(zip(event_times, event_names))
}  # using dict comprehension
print(events)


# chrome_driver.close()  # closes the single tab.
chrome_driver.quit()  # closes all the opened tabs.
