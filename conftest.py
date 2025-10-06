import pytest
from selenium import webdriver
from urls import CurrentURL

@pytest.fixture()
def driver():
    driver = webdriver.Firefox()
    driver.get(CurrentURL.scooter_address)
    yield driver
    driver.quit()