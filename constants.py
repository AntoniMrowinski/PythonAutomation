from selenium import webdriver

CHROMEDRIVER_PATH = "C:\\Program Files (x86)\\chromedriver.exe"

TXT_OUTPUT_PATH = "C:\\Users\\Antoni\\Desktop"

OLX_URL = "https://www.olx.pl"

SEARCH_BOX = "#headerSearch"

SEARCH_BUTTON = "#submit-searchmain"

VIEW_ALL_BUTTON = "#body-container > div:nth-child(3) > div > div.rel.listHandler > table.fixed.offers.breakword.offers--top.redesigned > tbody > tr:nth-child(1) > td > div > h2 > a > span"

COOKIES_CONSENT_BUTTON = "#cookiesBar > button"

LOGGED_IN_BUTTON = "#topLoginLink > span"

RESULTS_TABLE = "#body-container > div:nth-child(3) > div"

USER_SELECTOR = "#topLoginLink > i"

NO_COMMON_AUCTIONS_FOUND = "#body-container > div.wrapper > div > div.emptynew.large.lheight18 > p"

chrome_driver = webdriver.Chrome(CHROMEDRIVER_PATH)

chrome_driver.maximize_window()

browser_total_stop = False

promoted_results_stop = True

relevant_auctions_array = []

next_page_selector = ""

cheapest_auction_url = ""

search_for_promoted_only = ""

object_searched = ""

initial_index = 2

size = 0

advertisement = 0

min_price = 0

browserNextPage_initial_index = 2

browserNextPage_initial_index_assistant = 3

found_auctions_sum = 0

gui_row_controller = 4

user_input_array = []

search_obect_input = ""

price_input = 0

promoted_results_input = ""

first_search = True

print("kasuje")
last_row = 0

initial_limit = 0