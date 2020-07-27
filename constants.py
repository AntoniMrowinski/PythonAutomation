from selenium import webdriver
import globalConstants
from selenium.common.exceptions import NoSuchElementException


PATH1 = "C:\Program Files (x86)\chromedriver.exe"

url1 = "https://www.olx.pl"

my_driver = webdriver.Chrome(PATH1)
my_driver.maximize_window()

object_searched = "rower"

search_field = "#headerSearch"

search_button = "#submit-searchmain"

view_all = "#body-container > div:nth-child(3) > div > div.rel.listHandler > table.fixed.offers.breakword.offers--top.redesigned > tbody > tr:nth-child(1) > td > div > h2 > a > span"

cookies = "#cookiesBar > button"

logged_in_button = "#topLoginLink > span"

results_table = "#body-container > div:nth-child(3) > div"

user_selector = "#topLoginLink > i"
# user_selector = "#userLoginBox"

table_initial_index = 3

advertisement = 0









#
# # do tworzenia selectorów childa w oparciu o ilośc elementów (aukcji) znalezionych podczas wyszukiwania. Tylko promowane
# def childSelectorMaker(list_size):
#     child_selector_list = []
#     for i in range(table_initial_index, list_size+table_initial_index):
#         given_child = "#offers_table > tbody > tr:nth-child(" + str(i) + ") > td > div"
#         child_selector_list.append(given_child)
#     # print(child_selector_list)
#     return child_selector_list
#
# # Do tworzenia selektorów cen childa DZIALA
# def childSelectorForPriceMaker(list_size):
#     child_price_selector_list = []
#     for i in range(table_initial_index, list_size+table_initial_index):
#         given_child = "#offers_table > tbody > tr:nth-child(" + str(i) + ") > td > div > table > tbody > tr:nth-child(1) > td.wwnormal.tright.td-price > div > p > strong"
#         child_price_selector_list.append(given_child)
#     # print(child_price_selector_list)
#     return child_price_selector_list
#
# # Do wyciągania cen do tabeli
# def priceTableGenerator(local_driver, child_price_selector_list):
#     child_price_list = []
#     for i in range(0, len(child_price_selector_list)):
#         # print(child_price_selector_list[i])
#         try:
#             child_webelement = my_driver.find_element_by_css_selector(child_price_selector_list[i])
#         except NoSuchElementException:
#                 globalConstants.advertisement +=1
#         # print(child_webelement)
#         given_price = child_webelement.text
#         # get_attribute("class=\"price\"")
#         # print(given_price)
#         child_price_list.append(given_price)
#     print(child_price_list)
#     return child_price_list
#
# def promotedResultsLengthDeterminer():
#     stop = False
#     size = 0
#     initial_index = 3
#     while stop != True:
#         local_selector = "#offers_table > tbody > tr:nth-child(" + str(initial_index) + ") > td > div"
#         size += 1
#         try:
#             my_driver.find_element_by_css_selector(local_selector)
#         except NoSuchElementException:
#             stop = True
#         initial_index += 1
#     return size
