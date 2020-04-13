# import config
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
driver = webdriver.Chrome(
    executable_path='./chromedriver', chrome_options=chrome_options)


def loginMethod(driver):
    driver.get('https://robinhood.com/login')

    # user_name = driver.find_element_by_name("username")
    # password = driver.find_element_by_name("password")

    # Inputs Username and Password
    # user_name.send_keys(config.USERNAME)
    # password.send_keys(config.PASSWORD)

    # Accessing submit button and clicking it to submit.
    # driver.find_element_by_xpath("/html/body[@class='theme-open-up']/div[@id='react_root']/div[@class='onfkZGO-08blwMwFO-Wvo']/div[@class='_2kH-MLd7Zn90lh6Lbh25Tg']/div[@class='Aq_2JwntWByhTcNCD2GE1']/div[2]/div[@class='_2Wk-zeITdOtHxxKyuqKguo']/div/form[@class='_17_I0wDhYhTnsfNxPR0_CF form-lg up']/footer[@class='_167T9zawWgojY3Z1O0xGiA']/div[@class='_2FuMYm7qpszdIBO9N56SlF']/button[@class='_3kh8OsNx6QdAbMaoKTi2Yq _1uaripz9PIQ8yApSTs6BKk']").click()


loginMethod(driver)
