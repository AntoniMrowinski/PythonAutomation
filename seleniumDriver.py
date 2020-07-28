from constants import my_driver
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException
import constants
import datetime
from os.path import join


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

    def goToPage(self, url_address):
        my_driver.get(url_address)

# Extracts child selectors
def childSelectorMaker():
    child_selector_list = []
    for i in range(0, len(constants.relevant_auctions_tab)):
        child_selector_list.append(constants.relevant_auctions_tab[i][0])
    return child_selector_list

# Extracts prices selectors
def priceSelectorMaker():
    child_price_selector_list = []
    for i in range(0, len(constants.relevant_auctions_tab)):
        child_price_selector_list.append(constants.relevant_auctions_tab[i][1])
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

# Extracts URLs
def URLsTableGenerator():
    child_URLs_list = []
    for i in constants.relevant_auctions_indexes:
        local_name_selector = "#offers_table > tbody > tr:nth-child(" + str(
            i) + ") > td > div > table > tbody > tr:nth-child(1) > td.title-cell > div > h3 > a"
        url_webelement = constants.my_driver.find_element_by_css_selector(local_name_selector)
        auction_url = url_webelement.get_attribute("href")
        child_URLs_list.append(auction_url)
    return child_URLs_list


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
                constants.relevant_auctions_tab.append([local_selector, price_selector])
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

# output=1 --> prints line after line
# outpit=2 --> returns whole table with formated lines
def fullTablePrinter(full_table, output_version):
    if output_version == 1:
        for i in range(0, len(full_table)):
            given_auction = ""
            given_auction += "--- "
            for j in range(0,3):
                given_auction += full_table[i][j]
                if j < 2:
                    given_auction +=  " -- "
            given_auction += " ---"
            print(given_auction)
    elif output_version == 2:
        txt_format_table = []
        for i in range(0, len(full_table)):
            given_auction = ""
            given_auction += "--- "
            for j in range(0,3):
                given_auction += full_table[i][j]
                if j < 2:
                    given_auction +=  " -- "
            given_auction += " ---"
            txt_format_table.append(given_auction)
        return txt_format_table

def writeToTxt(full_table, cheapest_auction, names_table, urls_table):
    # chapes auction - [price, index]
    local_cheapest_auction = cheapest_auction.copy()
    cheapest_auction_index = int(cheapest_auction[1])
    txt_output = open(join(constants.file_path, "searching_results.txt"), "wt")
    current_date = datetime.datetime.now()
    date_line = "\t" + "Wyszukano " + str(current_date.strftime("%d/%m/%y o %H:%M"))
    txt_output.write(date_line)
    txt_output.write("\n")
    auctions_input = fullTablePrinter(full_table, 2)
    for x in auctions_input:
        txt_output.write("\n")
        txt_output.write(str(x))
        txt_output.write("\n")
    local_cheapest_auction[1] = names_table[1]
    local_cheapest_auction[0] = cheapest_auction[0]
    cheapest_auction_url = urls_table[cheapest_auction_index]
    txt_output.write(f"\n\nThe chapest auction: ->  \"{local_cheapest_auction[1]}\"  <- Price: {local_cheapest_auction[0]}\n\n\tLink: {cheapest_auction_url}")
    txt_output.close()

# Takes out only the number from the price string and makes another table
def priceFloatExcluder(prices_table):
    prices_in_numbers = []
    for i in prices_table:
        index_of_space = str.index(i, " zł")
        only_price = i[0:index_of_space]
        # Z jakiegoś powodu na dole tak musi być, ze robie osobny string ze stringa
        aid_string1 = str(only_price)
        aid_string2 = aid_string1.replace(",", ".")
        only_price = aid_string2.replace(" ", "")
        prices_in_numbers.append(float(only_price))
    # Returns floats like 100.0 !!!
    return prices_in_numbers

def lowPriceIdentifier(prices_table):
    prices_in_numbers = priceFloatExcluder(prices_table)
    cheapest = prices_in_numbers[0]
    for i in range(0, len(prices_in_numbers)):
        if prices_in_numbers[i] < cheapest:
            cheapest = prices_in_numbers[i]
            index_of_cheapest = i
    return [cheapest, index_of_cheapest]


