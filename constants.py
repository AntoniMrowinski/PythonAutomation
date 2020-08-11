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

min_price = None

browserNextPage_initial_index = 2

browserNextPage_initial_index_multiple_results = 3

browserNextPage_initial_index_assistant = 3

browserNextPage_initial_index_assistant_multiple_results = 4

found_auctions_sum = 0

gui_row_controller = 4

user_input_array = []

search_obect_input = ""

results_array = []

price_input = 0

promoted_results_input = ""

first_search = True

last_row = 0

initial_limit = 0

max_pages_browsed = 12

in_process = False

results_token = False

multiple_pages_search = False

communicate_array = []

results_title_label_array = []

# original arrray before checkbox:
# input_consent = [False, False, False]
input_consent = [False, False, True]

input_error_warnings = []

cheapest_auction_for_gui = []

multiple_results_check_token = False

errors_dictionary = {
    "[0, 0]": "Cannot search for nothing!",
    "[1, 0]": "Use '.' instead of ','!",
    "[1, 1]": "Incorrect price format!",
    "[1, 2]": "No minimal price provided!",
    "[2, 0]": "No choice regarding promotion!",
    "[2, 1]": "Promotion choice must be either 'y' or 'n'!"
}

potential_page_index = 10