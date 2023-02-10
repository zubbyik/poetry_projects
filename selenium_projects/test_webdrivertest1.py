from selenium import webdriver
import pathlib
import pytest


def check_url_of_the_website():
    driver = webdriver.Chrome(pathlib.Path().joinpath('chromedriver'))
    driver.get('http://65.21.1.10:9099')
    driver.close()


check_url_of_the_website()
