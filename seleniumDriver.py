from constants import my_driver
from constants import object_searched
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException
import constants
import globalConstants
import time


class caller():

    def __init__(self, url_address):
        self.url_address = url_address

    def setSelenium(self):
        my_driver.get(self.url_address)

    def quitSelenium(self):
        my_driver.quit()

    def findMeElement(self, element):
        located_element = my_driver.find_element_by_css_selector(element)
        return located_element

    def putText(self, operational_element, searching_text):
        operational_element.send_keys(searching_text)

    def clickElement(self, element):
        element.click()

    def putCursourAtElement(self, element, driver):
        action = webdriver.ActionChains(driver)
        action.move_to_element(element)
        action.perform()
        return action

    def eliminateCoursorAtElement(self, action):
        action.release()
        action.reset_actions()

# Extracts child selectors
def childSelectorMaker():
    child_selector_list = []
    for i in range(0, len(constants.relevant_auctions_dict)):
        child_selector_list.append(constants.relevant_auctions_dict[i][0])
    return child_selector_list

# Extracts prices selectors
def priceSelectorMaker():
    child_price_selector_list = []
    for i in range(0, len(constants.relevant_auctions_dict)):
        child_price_selector_list.append(constants.relevant_auctions_dict[i][1])
    return child_price_selector_list


# Extracts prices based on price_selectors
def priceTableGenerator(child_price_selector_list):
    child_price_list = []
    for i in range(0, len(child_price_selector_list)):
        try:
            child_webelement = constants.my_driver.find_element_by_css_selector(child_price_selector_list[i])
            given_price = child_webelement.text
            child_price_list.append(given_price)
        except NoSuchElementException:
            True
    return child_price_list

# Extracts names
def nameTableGenerator():
    child_name_list = []
    for i in constants.relevant_auctions_indexes:
        loca_name_selector = "#offers_table > tbody > tr:nth-child(" + str(i) + ") > td > div > table > tbody > tr:nth-child(1) > td.title-cell > div > h3 > a > strong"
        name_webelement = constants.my_driver.find_element_by_css_selector(loca_name_selector)
        auction_name = name_webelement.text
        child_name_list.append(auction_name)
    return child_name_list

# Extracts locations
def localisationTableGenerator():
    child_localisation_list = []
    for i in constants.relevant_auctions_indexes:
        loca_name_selector = "#offers_table > tbody > tr:nth-child(" + str(
            i) + ") > td > div > table > tbody > tr:nth-child(2) > td.bottom-cell > div > p > small:nth-child(1) > span"
        location_webelement = constants.my_driver.find_element_by_css_selector(loca_name_selector)
        auction_location = location_webelement.text
        child_localisation_list.append(auction_location)
    return child_localisation_list


# Also creates table of relevant objects.
# It checks whether something has a correct main selector, if it does then if it has price.
# Price and main selector are saved if it is auction, when both conditions are fulfilled.
# Not fulfilled conditions mean that it's not an auction. If something doesn't have selector, it means that
# the list is finished.
def promotedResultsLengthDeterminer():
    stop = False
    size = 0
    initial_index = 3
    while stop != True:
        local_selector = "#offers_table > tbody > tr:nth-child(" + str(initial_index) + ") > td > div"
        price_selector = "#offers_table > tbody > tr:nth-child(" + str(initial_index) + ") > td > div > table > tbody > tr:nth-child(1) > td.wwnormal.tright.td-price > div > p > strong"
        try:
            my_driver.find_element_by_css_selector(local_selector)
            try:
                my_driver.find_element_by_css_selector(price_selector)
                size += 1
                # loads a dict with auction selector and price selector
                constants.relevant_auctions_dict.append([local_selector, price_selector])
                # Extract the indexes of auctions
                constants.relevant_auctions_indexes.append(initial_index)
            except NoSuchElementException:
                True
                constants.advertisement +=1
        except NoSuchElementException:
            stop = True
        initial_index += 1
    return size

# Appends all information into 1 table
def joinTables(names, locations, prices, size):
    all_info_table = []
    for i in range(0, size):
        all_info_table.append([names[i], locations[i], prices[i]])
    return all_info_table

def fullTablePrinter(full_table):
    for i in range(0, len(full_table)):
        given_auction = ""
        given_auction += "--- "
        for j in range(0,3):
            given_auction += full_table[i][j]
            if j < 2:
                given_auction +=  " -- "
        given_auction += " ---"
        print(given_auction)

def writeToTxt(full_table):
    current_date = time.localtime()
    txt_output = open("searching_results.txt", "wt")
    txt_output.write(str(current_date))
    for x in full_table:
        txt_output.write(str(x))
        txt_output.write("\n")
    txt_output.close()

