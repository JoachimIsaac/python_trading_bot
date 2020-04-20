
import time
from selenium import webdriver


search_query1 = 'Mutex lock'
# structuring our search query for search url.
search_query1 = search_query1.replace(' ', '+')

search_query2 = 'Java linked list'
# structuring our search query for search url.
search_query2 = search_query2.replace(' ', '+')

search_query3 = 'Java array list'
# structuring our search query for search url.
search_query3 = search_query3.replace(' ', '+')

executable_path = './chromedriver'
browser = webdriver.Chrome(executable_path=executable_path)


for i in range(20):
    time.sleep(2.4)
    if i % 2 == 0 and i < 10:

        browser.get("https://www.google.com/search?q=" +
                    search_query1 + "&start=" + str(10 * i))
        matched_elements = browser.find_elements_by_xpath(
            '//a[starts-with(@href, "https://www.thetaranights.com")]')
    elif i % 2 != 0 and i < 10:
        browser.get("https://www.google.com/search?q=" +
                    search_query2 + "&start=" + str(10 * i))
        matched_elements = browser.find_elements_by_xpath(
            '//a[starts-with(@href, "https://www.thetaranights.com")]')
    elif i > 15:
        browser.get("https://www.google.com/search?q=" +
                    search_query3 + "&start=" + str(10 * i))
        matched_elements = browser.find_elements_by_xpath(
            '//a[starts-with(@href, "https://www.thetaranights.com")]')

    if matched_elements:
        matched_elements[0].click()
        break
