from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup


class NaverMovie:
    def __init__(self, url):
        driver = webdriver.Chrome('chromedriver')
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        print(soup)