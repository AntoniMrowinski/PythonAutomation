from selenium import webdriver
import globalConstants

PATH1 = "C:\Program Files (x86)\chromedriver.exe"

url1 = "https://www.olx.pl"

object_searched = str(input("Looking for >> "))

my_driver = webdriver.Chrome(PATH1)

my_driver.maximize_window()


search_field = "#headerSearch"

search_button = "#submit-searchmain"

view_all = "#body-container > div:nth-child(3) > div > div.rel.listHandler > table.fixed.offers.breakword.offers--top.redesigned > tbody > tr:nth-child(1) > td > div > h2 > a > span"

cookies = "#cookiesBar > button"

logged_in_button = "#topLoginLink > span"

results_table = "#body-container > div:nth-child(3) > div"

user_selector = "#topLoginLink > i"

table_initial_index = 3

advertisement = 0

relevant_auctions_dict = []

relevant_auctions_indexes = []