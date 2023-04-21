from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time


def get_skinport_price(skin_name, condition, is_stattrack):
    """
    Searches skinport and finds the cheapest listing for the skin passed into the function.

    :param skin_name: The name of the skin to be searched for
    :param condition: The wear condition of the skin
    :param is_stattrack: Whether the skin is stattrack or not
    :return: The cheapest listing
    """
    link = f"https://skinport.com/market?search={skin_name.replace(' ', '+')}"

    if condition == 1:
        link += "&exterior=2"
    elif condition == 2:
        link += "&exterior=4"
    elif condition == 3:
        link += "&exterior=3"
    elif condition == 4:
        link += "&exterior=5"
    elif condition == 5:
        link += "&exterior=1"

    if is_stattrack:
        link += "&stattrak=1"

    options = Options()
    options.headless = True
    driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))

    driver.get(link)
    time.sleep(2)

    x_path = "/html/body/div[1]/div[1]/div[2]/div[1]/div/div[3]/div[2]/div/div/div/div[1]/a/div[1]/div/div[1]/div[" \
             "1]/div[1] "

    listings = driver.find_elements(By.XPATH, x_path)
    prices = []
    for element in listings:
        price = float(element.get_attribute('innerHTML').strip('$'))
        prices.append(price)

    driver.quit()

    return min(prices)



