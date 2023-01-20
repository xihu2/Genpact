#!/usr/bin/python3

import pytest
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.color import Color

@pytest.fixture
def browser():

   driver = Chrome()
   driver.implicitly_wait(10)
   yield driver
   driver.close()
   driver.quit()


def getColor(rgba):
    if (int(rgba.split('(')[1].split(',')[0]) > 200):
        return "Red"
    else:
        return "Black"

def testHomegainPage(browser):
    URL = 'http://www.homegain.com/homevalues'
    browser.get(URL)

    # Enter Fremont Zip code and click Go button
    input = browser.find_element(By.ID, 'rewLocation')
    input.send_keys('94539')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[1]/button').click()

    # Select Home Values and click Continue button
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[2]/ul/li[3]').click()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[2]/button[2]').click()

    # Validate Search Home page
    assert browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/span[1]').get_attribute('innerHTML') == "Fremont, CA"


    # Select required inputs and click Continue
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[1]/option[2]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/input').send_keys('123 Fremont Blvd')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[5]/option[5]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[6]/option[8]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[1]').send_keys('Joe')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[2]').send_keys('L')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[3]').send_keys('510-345-6789')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[4]').send_keys('test@gmail.com')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/button[1]').click()

    # Validate Thank you page
    assert browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[4]/header/h3').get_attribute('innerHTML') == "Got It! We'll get you connected with a local pro ASAP."


def testZipCodePage(browser):
    URL = 'http://www.homegain.com/homevalues'
    browser.get(URL)

    # Click Go button without entering Zip code
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[1]/button').click()
    s = browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[1]/input').value_of_css_property("color")

    # Validate Zip Code input field is highlighted Red
    assert getColor(s) == "Red"


def testTypeofRealEstatePage(browser):
    URL = 'http://www.homegain.com/homevalues'
    browser.get(URL)

    # Enter Fremont Zip code and click Go button
    input = browser.find_element(By.ID, 'rewLocation')
    input.send_keys('94539')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[1]/button').click()

    # Click Continue button without select Home Values
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[2]/button[2]').click()
    s = browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[2]').value_of_css_property("border-color")

    # Validate Zip Code input field is highlighted Red
    assert getColor(s) == "Red"


def testSearchHomeValuePage(browser):
    URL = 'http://www.homegain.com/homevalues'
    browser.get(URL)

    # Enter Fremont Zip code and click Go button
    input = browser.find_element(By.ID, 'rewLocation')
    input.send_keys('94539')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[1]/button').click()

    # Select Home Values and click Continue button
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[2]/ul/li[3]').click()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[2]/button[2]').click()

    # Validate Search Home page
    assert browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/span[1]').get_attribute('innerHTML') == "Fremont, CA"

    # Click Continue without selecting any required information
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/button[1]').click()
    s = browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[1]/option[1]').value_of_css_property("border-color")

    # Validate the first selection is highlighted Red
    assert getColor(s) == "Red"

    # Click Continue without selecting all required information
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[1]/option[2]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/button[1]').click()
    s = browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/input').value_of_css_property("border-color")

    # Validate Address input field is highlighted Red
    assert getColor(s) == "Red"

    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[1]/option[2]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/input').send_keys('123 Fremont Blvd')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/button[1]').click()
    s = browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[5]').value_of_css_property("border-color")

    # Validate When you plan to sell your home selection is highlighted Red
    assert getColor(s) == "Red"

    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[1]/option[2]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/input').send_keys('123 Fremont Blvd')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[5]/option[5]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/button[1]').click()
    s = browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[6]').value_of_css_property("border-color")

    # Validate What is the minimum home value selection is highlighted Red
    assert getColor(s) == "Red"

    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[1]/option[2]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/input').send_keys('123 Fremont Blvd')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[5]/option[5]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[6]/option[8]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/button[1]').click()
    s = browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[1]').value_of_css_property("border-color")

    # Validate First Name field is highlighted Red
    assert getColor(s) == "Red"

    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[1]/option[2]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/input').send_keys('123 Fremont Blvd')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[5]/option[5]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[6]/option[8]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[1]').send_keys('Joe')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/button[1]').click()
    s = browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[2]').value_of_css_property("border-color")

    # Validate Last Name field is highlighted Red
    assert getColor(s) == "Red"

    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[1]/option[2]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/input').send_keys('123 Fremont Blvd')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[5]/option[5]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[6]/option[8]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[1]').send_keys('Joe')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[2]').send_keys('L')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/button[1]').click()
    s = browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[3]').value_of_css_property("border-color")

    # Validate Phone field is highlighted Red
    assert getColor(s) == "Red"

    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[1]/option[2]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/input').send_keys('123 Fremont Blvd')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[5]/option[5]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/select[6]/option[8]').is_selected()
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[1]').send_keys('Joe')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[2]').send_keys('L')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[3]').send_keys('510-345-6789')
    browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/button[1]').click()
    s = browser.find_element(By.XPATH, '//form/div[1]/div[2]/div[3]/div[2]/div[1]/div[2]/input[4]').value_of_css_property("border-color")

    # Validate Email field is highlighted Red
    assert getColor(s) == "Red"
