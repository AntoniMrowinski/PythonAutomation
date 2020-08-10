from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from constants import chrome_driver
import selenium.webdriver as webdriver
from selenium.common.exceptions import NoSuchElementException
import constants
import datetime
import time
from os.path import join


# Driver class holds general methods user for managing used webdriver
class Driver():

    def __init__(self, url_address):
        self.url_address = url_address

    def setSelenium(self):
        chrome_driver.get(self.url_address)

    def quitSelenium(self):
        chrome_driver.quit()

    def findMeElement(self, element):
        located_element = chrome_driver.find_element_by_css_selector(element)
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

    def goToPage(self, url_address_external):
        chrome_driver.get(url_address_external)


# Clicks the "See all" button once or more depending on the reaction of the button.
# If is clicked multiple times without reaction, it means that no promoted auctions can be found
def seeAllButtonClicker(chrome_driver_instance,current_browser):
    click_cycle = 0
    while True:
        try:
            click_cycle +=1
            if click_cycle >= 10:
                return False
            see_all_button = chrome_driver_instance.findMeElement(constants.VIEW_ALL_BUTTON)
            chrome_driver_instance.clickElement(see_all_button)
            current_browser_after_click =  constants.chrome_driver.current_url
            if current_browser != current_browser_after_click:
                return True
        except NoSuchElementException:
            True

def nextPageButtonClicker(next_page_selector, previous_page):
    while True:
        try:
            next_page_button = WebDriverWait(chrome_driver, 5).until(
                expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, next_page_selector)))
            new_page = chrome_driver.current_url
            while previous_page == new_page:
                next_page_button.click()
                time.sleep(1)
                new_page = chrome_driver.current_url
            break
        except NoSuchElementException:
            True

# Receives input from the user regarding the object searched and the minimal price
# Minimal price defines the lower price limit for the cheapest auction found.
def userInputReception():
    print("entered input reception")
    # searching object
    try:
        constants.object_searched = constants.search_obect_input
        print(f"in search object: {constants.object_searched}, origina input: {constants.search_obect_input}")
        if constants.object_searched == "":
            constants.input_consent[0] = False
            constants.input_error_warnings.append([0,0])
        else:
            constants.input_consent[0] = True
    except:
        constants.input_consent[0] = False

    #price
    try:
        constants.min_price = constants.price_input
        print(f"in price: {constants.min_price}, origina input: {constants.price_input}")
        if "," in str(constants.min_price):
            constants.input_consent[1] = False
            constants.input_error_warnings.append([1,0])
        else:
            try:
                constants.min_price = float(constants.min_price)
                constants.input_consent[1] = True
            except:
                constants.input_error_warnings.append([1,1])
                constants.input_consent[1] = False
    except:
        constants.input_error_warnings.append([1,2])
        constants.input_consent[0] = False

    #promoted only
    try:
        constants.search_for_promoted_only = constants.promoted_results_input
        print(f"in promotion: {constants.search_for_promoted_only}, origina input: {constants.promoted_results_input}")
        if constants.search_for_promoted_only == "":
            constants.input_error_warnings.append([2,0])
        elif constants.search_for_promoted_only.lower() != "y" and constants.search_for_promoted_only.lower() != "n":
            constants.input_error_warnings.append([2,1])
        else:
            constants.input_consent[2] = True
    except:
        constants.input_consent[2] = False
        constants.input_error_warnings([2,2])


    # consent_sum = constants.input_consent[0] and constants.input_consent[1] and constants.input_consent[2]
    # while consent_sum != True:
    #     while True:
    #         try:
    #             constants.object_searched = constants.search_obect_input
    #             constants.input_consent[0] = True
    #             break
    #         except:
    #             print("Cannot search for Null!")
    #     while True:
    #         try:
    #             constants.min_price = constants.price_input
    #             if "," in str(constants.min_price):
    #                 print("Use \".\" instead of \",\"!")
    #                 constants.input_consent[1] = True
    #             else:
    #                 try:
    #                     constants.min_price = float(constants.min_price)
    #                     break
    #                 except:
    #                     print("Incorrect price format!")
    #         except:
    #             True
    #     while True:
    #         try:
    #             constants.search_for_promoted_only = constants.promoted_results_input
    #             if constants.search_for_promoted_only == "":
    #                 print("Make your choice, please.")
    #             elif constants.search_for_promoted_only.lower() != "y" and constants.search_for_promoted_only.lower() != "n":
    #                 print("Incorrect answer format! Use \"y\" or \"n\".")
    #             else:
    #                 constants.input_consent[2]=True
    #                 break
    #         except:
    #             constants.search_for_promoted_only
    #             print("Make your choice, please.")
    #             True
    # print(f"\nSearching for \"{constants.object_searched}\" ...\n\t Do not interrupt the browser!")

def checkNoCommonAuctionsFound():
    look_cycle = 0
    while True:
        try:
            look_cycle += 1
            if look_cycle >= 10:
                return False
            constants.chrome_driver.find_element_by_css_selector(constants.NO_COMMON_AUCTIONS_FOUND)
            return True
        except NoSuchElementException:
            True


# Extracts a price based on a price_selector
def priceTableGenerator(price_selector):
    child_webelement = constants.chrome_driver.find_element_by_css_selector(price_selector)
    auction_price = child_webelement.text
    return auction_price


# Extracts a name of a given auction
def nameExtractor(index):
    loca_name_selector = "#offers_table > tbody > tr:nth-child(" + str(index) + ") > td > div > table > tbody >" \
                                                            " tr:nth-child(1) > td.title-cell > div > h3 > a > strong"
    name_webelement = constants.chrome_driver.find_element_by_css_selector(loca_name_selector)
    auction_name = name_webelement.text
    return auction_name


# Extracts a location of a given auction
def locationExtractor(index):
    loca_name_selector = "#offers_table > tbody > tr:nth-child(" + str(
        index) + ") > td > div > table > tbody > tr:nth-child(2) > td.bottom-cell > div > p > small:nth-child(1) > span"
    location_webelement = constants.chrome_driver.find_element_by_css_selector(loca_name_selector)
    auction_location = location_webelement.text
    return auction_location


# Extracts an URL of a given auction
def urlExtractor(index):
    local_name_selector = "#offers_table > tbody > tr:nth-child(" + str(
        index) + ") > td > div > table > tbody > tr:nth-child(1) > td.title-cell > div > h3 > a"
    url_webelement = constants.chrome_driver.find_element_by_css_selector(local_name_selector)
    auction_url = url_webelement.get_attribute("href")
    return auction_url


# auctionBrowser construes an array of auctions.
#   The array rows include information about auctions including index, name, price, location, url
#   Only auctions with prices are added to the final array.
#   Function creates css selectors of a potential next auction WebElement and it's price WebElement.
#   If auction exist, it looks for price. If price WebElement cannot be found,
#   then the auction is omitted in final results table.
#   If next potential auction WebElement cannot be located, it is checked whether next result page exist.
#   If yes, it is clicked and browsing continues. If not, the browsing is finished.
def auctionBrowser():
    time.sleep(2)
    while constants.promoted_results_stop == True:
        constants.initial_index += 1
        local_selector = "#offers_table > tbody > tr:nth-child(" + str(constants.initial_index) + ") > td > div"
        price_selector = "#offers_table > tbody > tr:nth-child(" + str(constants.initial_index) + ") > td > div >" \
                                    " table > tbody > tr:nth-child(1) > td.wwnormal.tright.td-price > div > p > strong"
        try:
            chrome_driver.find_element_by_css_selector(local_selector)
            try:
                chrome_driver.find_element_by_css_selector(price_selector)
                price_check = priceTableGenerator(price_selector)
                if "Zamienię" in price_check:
                    auctionBrowser()
                constants.size += 1
                dummy_initial_index = constants.initial_index-2
                right_index = (dummy_initial_index + constants.found_auctions_sum + 1)

                name = nameExtractor(constants.initial_index)
                price = priceTableGenerator(price_selector)
                location = locationExtractor(constants.initial_index)
                url = urlExtractor(constants.initial_index)
                table_insert = [right_index, name, price, location, url]

                constants.relevant_auctions_array.append(table_insert)
            except NoSuchElementException:
                aid_advertisement = constants.advertisement
                constants.advertisement = aid_advertisement + 1
        except NoSuchElementException:
            time.sleep(5)
            is_there_next_page = browseNextPage()
            if is_there_next_page == True:
                constants.found_auctions_sum += (constants.initial_index - 2) - constants.advertisement
                constants.initial_index = 2
                constants.advertisement = 0
            else:
                constants.promoted_results_stop = False
                constants.found_auctions_sum += (constants.initial_index - 2) - constants.advertisement
                constants.initial_index = 2
                constants.advertisement = 0


# Checks whether there is another page.
#   Requires checking whether there are two following pages due to the presence
#    of an invisible WebElement that normally causes browsing last results page twice.
#
# The function creates selector of a next page WebElement and further next page WebElement.
#   If there is another page, it is clicked and the function returns true, to signalise presence of the next result page
#   and readiness for further auction browsing.
#   If there is no other page, the function returns False to signalise that browsing auctions should end
def browseNextPage():
    try:
        constants.browserNextPage_initial_index += 1
        constants.next_page_selector = "#body-container > div:nth-child(3) > div > div.pager.rel.clr > " \
                                       "span:nth-child(" + str(constants.browserNextPage_initial_index) + ") > a"
        chrome_driver.find_element_by_css_selector(constants.next_page_selector)
        try:
            constants.browserNextPage_initial_index_assistant += 1
            constants.next_page_selector_assistant = "#body-container > div:nth-child(3) > div > div.pager.rel.clr > " \
                                                     "span:nth-child(" + str(
                constants.browserNextPage_initial_index_assistant) + ") > a"
            chrome_driver.find_element_by_css_selector(constants.next_page_selector_assistant)
        except NoSuchElementException:
            return False
        current_url = chrome_driver.current_url
        nextPageButtonClicker(constants.next_page_selector, current_url)
        return True
    except NoSuchElementException:
        return False


# Assigns a new array which assigns ordered indexes to the original array of all relevant auctions
def tableOrderer(full_array):
    ordered_table = []
    new_index = 0
    for item in full_array:
        item[0] = new_index
        ordered_table.append(item)
        new_index +=1
    return ordered_table


# Prints the array of found auctions.
#   output=1 --> prints line after line
#   outpit=2 --> returns whole table with formated lines. Used for writing to txt.
#   The latter doest not include URLs to improve readability of the txt file.
def fullTablePrinter(full_array, output_version):
    if output_version == 1:
        for i in range(0, len(full_array)):
            given_auction = ""
            given_auction += "--- "
            for j in range(0,5):
                given_auction += str(full_array[i][j])
                if j < 4:
                    given_auction +=  " -- "
            given_auction += " ---"
            print(given_auction)
    elif output_version == 2:
        txt_format_table = []
        for i in range(0, len(full_array)):
            given_auction = ""
            given_auction += "--- "
            for j in range(0,4):
                given_auction += str(full_array[i][j])
                if j < 3:
                    given_auction +=  " -- "
            given_auction += " ---"
            txt_format_table.append(given_auction)
        return txt_format_table


# Prints the information about searching to the searching_results.txt file.
#   Includes information about time of searching, number of results, auctions themselves, and the cheapest auction.
def writeToTxt(full_array, no_promoted_auctions_found):
    if no_promoted_auctions_found == False:
        txt_output = open(join(constants.TXT_OUTPUT_PATH, "searching_results.txt"), "wt", encoding="utf-8")

        # Prints general searching data:
        current_date = datetime.datetime.now()
        date_line = "\t" + "Searched on " + str(current_date.strftime("%d/%m/%y at %H:%M\n"))
        found_auctions_line = f"\nFound {len(full_array)} auctions total for \"{constants.object_searched}\"\n\n"
        txt_output.write(date_line)
        txt_output.write(found_auctions_line)

        # Prints detailed auction information
        formatted_auctions_array = fullTablePrinter(full_array, 2)
        for x in formatted_auctions_array:
            txt_output.write(f"\n{str(x)}\n")

        # Prints detailed cheapest auction information
        price_str, name_str, auction_index, limit_imposed_by_the_user = cheapestAuctionInformationFormatter(full_array)
        txt_output.write("\n\n\nThe lowest-price limit imposed by the user: {} zł\n\nThe chapest auction:\t ---->  \"{}\"  <----\t\tPrice:"
                         " {} zł\n\nLink:\t{}".format(limit_imposed_by_the_user, name_str, price_str,
                            constants.cheapest_auction_url))
        txt_output.close()
    else:
        txt_output = open(join(constants.TXT_OUTPUT_PATH, "searching_results.txt"), "wt", encoding="utf-8")
        current_date = datetime.datetime.now()
        date_line = "\t" + "Searched on " + str(current_date.strftime("%d/%m/%y at %H:%M\n"))
        txt_output.write(date_line)
        no_promoted_auctions_found_message =f"\nSorry! No auctions found for  \"{constants.object_searched}\""
        txt_output.write(no_promoted_auctions_found_message)


# Extracts sole values from the price_collumn.
#   Eliminates " zł" and spaces, turns "," into "." to allow for float parsing
#   Returns array in a form of [x1.0, x2.0, ...]
def priceFloatValueExtractor(prices_table):
    prices_float_values = []
    # index_of_space = 0
    for i in prices_table:
        if "Za darmo" in i:
           prices_float_values.append(float(0))
        else:
            index_of_space = str.index(i, " zł")
            only_price = i[0:index_of_space]
            aid_string1 = str(only_price)
            aid_string2 = aid_string1.replace(",", ".")
            only_price = aid_string2.replace(" ", "")
            prices_float_values.append(float(only_price))
    return prices_float_values


# Returns the information about the cheapest auction within the limit initially imposed by the user
#   Returns array [price, index]
def cheapestAuctionIdentifier(full_array):
    extracted_prices_collumn = []
    prices_above_the_limit = []

    index_of_cheapest = 0
    for i in range(0, len(full_array)):
        extracted_prices_collumn.append(full_array[i][2])
    prices_in_float_values = priceFloatValueExtractor(extracted_prices_collumn)
    for i in range(0, len(prices_in_float_values)):
        if prices_in_float_values[i] >= constants.min_price:
            prices_above_the_limit.append([prices_in_float_values[i],i])
    cheapest = prices_above_the_limit[0][0]
    for j in range(1, len(prices_above_the_limit)):
        if prices_above_the_limit[j][0] < cheapest:
            cheapest = prices_above_the_limit[j][0]
            index_of_cheapest = prices_above_the_limit[j][1]
    return [cheapest, index_of_cheapest]


# Prepares information about the cheapest auction found by eliminating unnecessary zeros or "."
def cheapestAuctionInformationFormatter(full_array):
    cheapest_auction = cheapestAuctionIdentifier(full_array)
    excluded_index = cheapest_auction[1]
    limit_imposed_by_the_user = str(constants.min_price)
    limit_imposed_by_the_user = limit_imposed_by_the_user.strip("0")
    limit_imposed_by_the_user = limit_imposed_by_the_user.strip(".")
    price = str(cheapest_auction[0])
    price = price.strip("0")
    price = price.strip(".")
    name = str(full_array[excluded_index][1])
    constants.cheapest_auction_url = full_array[excluded_index][4]
    return price, name, excluded_index, limit_imposed_by_the_user
