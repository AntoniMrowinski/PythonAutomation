from constants import my_driver
from constants import object_searched
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException
import constants
import globalConstants


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

# do tworzenia selectorów childa w oparciu o ilośc elementów (aukcji) znalezionych podczas wyszukiwania. Tylko promowane
def childSelectorMaker():
    child_selector_list = []
    for i in range(0, len(constants.relevant_auctions_dict)):
        child_selector_list.append(constants.relevant_auctions_dict[i][0])
    return child_selector_list

    child_selector_list = []
    # for i in range(constants.table_initial_index, list_size + constants.table_initial_index):
    #     given_child = "#offers_table > tbody > tr:nth-child(" + str(i) + ") > td > div"
    #     child_selector_list.append(given_child)
    # # print(child_selector_list)
    # return child_selector_list

# Do tworzenia selektorów cen childa DZIALA

def priceSelectorMaker():
    child_price_selector_list = []
    for i in range(0, len(constants.relevant_auctions_dict)):
        child_price_selector_list.append(constants.relevant_auctions_dict[i][1])
    return child_price_selector_list


# Do wyciągania cen do tabeli
def priceTableGenerator(local_driver, child_price_selector_list):
    child_price_list = []
    for i in range(0, len(child_price_selector_list)):
        try:
            child_webelement = constants.my_driver.find_element_by_css_selector(child_price_selector_list[i])
            given_price = child_webelement.text
            child_price_list.append(given_price)
        except NoSuchElementException:
            True
    return child_price_list

# Also creates table of relevant objects.
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
            except NoSuchElementException:
                True
                constants.advertisement +=1
        except NoSuchElementException:
            stop = True
        initial_index += 1
    return size

