import seleniumDriver
import constants
import time
import globalConstants
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By



# setting up selenium and searching for webelements
local_driver = seleniumDriver.caller(constants.url1)
local_driver.setSelenium()
# dlaczego tego nie mooge wywolac z poziomu local_drivera ??
constants.my_driver.implicitly_wait(5)
searcher_box = local_driver.findMeElement(constants.search_field)
searching_button = local_driver.findMeElement(constants.search_button)
cookies_consent_button = local_driver.findMeElement(constants.cookies)


# checking if user is logged ( doesn't do anything )
user_tab = local_driver.findMeElement(constants.logged_in_button)
time.sleep(3)
# trzyma obiekt akcji w tym pliku
action_holder = local_driver.putCursourAtElement(user_tab, constants.my_driver)
action_holder.click_and_hold(user_tab)
time.sleep(3)
local_driver.eliminateCoursorAtElement(action_holder)

# searching for element(s) and clicking to see all that are promoted
local_driver.clickElement(cookies_consent_button)
local_driver.clickElement(searcher_box)
local_driver.putText(searcher_box, constants.object_searched)
local_driver.clickElement(searching_button)
### Poniższe powoduje zepsucie i intercepcje
time.sleep(5)
see_all_button = local_driver.findMeElement(constants.view_all)
local_driver.clickElement(see_all_button)
###
time.sleep(7)

# Creating child selectors depending on the found results ( not yet )
size_of_table_generated = seleniumDriver.promotedResultsLengthDeterminer()
size_of_table_generated -= constants.advertisement
seleniumDriver.childSelectorMaker(size_of_table_generated)
child_prices_selectors_list = seleniumDriver.childSelectorForPriceMaker(size_of_table_generated)
prices_table = seleniumDriver.priceTableGenerator(local_driver, child_prices_selectors_list)
print("prices:", end=" ")
print(prices_table)
print("items found:", end=" ")
print(size_of_table_generated)

print("d" + 1)
local_driver.quitSelenium()
