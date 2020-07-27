import seleniumDriver
import constants
import time
import globalConstants
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By



# Setting up selenium
local_driver = seleniumDriver.caller(constants.url1)
local_driver.setSelenium()
# dlaczego tego nie mooge wywolac z poziomu local_drivera ??
constants.my_driver.implicitly_wait(5)
searcher_box = local_driver.findMeElement(constants.search_field)
searching_button = local_driver.findMeElement(constants.search_button)
cookies_consent_button = local_driver.findMeElement(constants.cookies)



# Supposed to check if user is logged (doesn't work)
user_tab = local_driver.findMeElement(constants.logged_in_button)
action_holder = local_driver.putCursourAtElement(user_tab, constants.my_driver)
action_holder.click_and_hold(user_tab)
local_driver.eliminateCoursorAtElement(action_holder)



# Searching for a given object and clicking to see all that are promoted
local_driver.clickElement(cookies_consent_button)
local_driver.clickElement(searcher_box)
local_driver.putText(searcher_box, constants.object_searched)
local_driver.clickElement(searching_button)
see_all_button = local_driver.findMeElement(constants.view_all)
local_driver.clickElement(see_all_button)



# Creating child selectors depending on the found results
size_of_table_generated = seleniumDriver.promotedResultsLengthDeterminer()
print(f"All auctions found: {size_of_table_generated}")
print(f"Adverts or auctions without price: {constants.advertisement}")
child_selectors = seleniumDriver.childSelectorMaker()
# print(f"Child selectors: {child_selectors}")
prices_selectors = seleniumDriver.priceSelectorMaker()
# print(f"Price selectors: {prices_selectors}")
prices_table = seleniumDriver.priceTableGenerator(local_driver, prices_selectors)
# print(f"Both child:price selectors: {constants.relevant_auctions_dict}")
print(f"prices: {prices_table}")



# # Force-stopping code
# print("d" + 1)

local_driver.quitSelenium()
