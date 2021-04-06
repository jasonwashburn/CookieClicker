from selenium import webdriver
import time

webdriver_path = "/Users/wburn/PycharmProjects/chromedriver"
driver = webdriver.Chrome(executable_path=webdriver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_id("cookie")

start_time = time.time()
timeout = time.time() + 60  # 5 minutes from now

cursor_cost = int(driver.find_element_by_id("buyCursor").text.split("\n")[0].split("-")[1].strip().replace(",", ""))

print(cursor_cost)
wait_timer = time.time()

while True:
    for _ in range(400):
        cookie.click()
    elapsed = time.time() - wait_timer
    print(f"100 clicks in {elapsed}s")
    money = int(driver.find_element_by_id("money").text.replace(",", ""))
    cursor = driver.find_element_by_id("buyCursor")
    cursor_cost = int(
        driver.find_element_by_id("buyCursor").text.split("\n")[0].split("-")[1].strip().replace(",", ""))
    grandma = driver.find_element_by_id("buyGrandma")
    grandma_cost = int(
        driver.find_element_by_id("buyGrandma").text.split("\n")[0].split("-")[1].strip().replace(",", ""))
    factory = driver.find_element_by_id("buyFactory")
    factory_cost = int(
        driver.find_element_by_id("buyFactory").text.split("\n")[0].split("-")[1].strip().replace(",", ""))
    mine = driver.find_element_by_id("buyMine")
    mine_cost = int(driver.find_element_by_id("buyMine").text.split("\n")[0].split("-")[1].strip().replace(",", ""))
    shipment = driver.find_element_by_id("buyShipment")
    shipment_cost = int(
        driver.find_element_by_id("buyShipment").text.split("\n")[0].split("-")[1].strip().replace(",", ""))

    cursor_efficiency = cursor_cost / .2
    grandma_efficiency = grandma_cost / .8
    factory_efficiency = factory_cost / 4


    if money > shipment_cost:
        mine.click()
        print(f"Bought Shipment - Cost: {shipment_cost}")
        wait_timer = time.time()
    if money > mine_cost:
        mine.click()
        print(f"Bought Mine - Cost: {mine_cost}")
        wait_timer = time.time()
    if money > factory_cost:
        factory.click()
        print(f"Bought Factory - Cost/Cookie/Sec: {factory_efficiency}")
        wait_timer = time.time()
    elif money > grandma_cost:
        grandma.click()
        print(f"Bought Grandma - Cost/Cookie/Sec: {grandma_efficiency}")
        wait_timer = time.time()
    elif money > cursor_cost:
        cursor.click()
        print(f"Bought Cursor - Cost/Cookie/Sec: {cursor_efficiency}")
        wait_timer = time.time()
    if time.time() > timeout:
        break




