from selenium import webdriver
import time

# Change webdriver_path to the appropriate path on your machine
webdriver_path = "/Users/wburn/PycharmProjects/chromedriver"
driver = webdriver.Chrome(executable_path=webdriver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

# Set up timer
start_time = time.time()
timeout = time.time() + 300  # Run for 5 minutes (5 * 60 seconds)


def get_available_upgrades():
    """
    Creates a list of store elements that are able to be purchased
    :return: Returns a list of page elements
    """
    store_items = driver.find_elements_by_css_selector("#store div")
    available_items = [element for element in store_items if element.get_attribute("class") != "grayed"]

    return available_items


while True:
    for _ in range(200):  # Can be adjusted to tweak performance...
        cookie.click()
    upgradeable_items = get_available_upgrades()  # Get list of available upgrades
    biggest_upgrade = upgradeable_items[-1]  # Find the biggest one
    biggest_upgrade.click()  # Buy it

    if time.time() > timeout:  # Break out of the loop once the timer is complete
        break





