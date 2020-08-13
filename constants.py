errors_dictionary = {
    "[0, 0]": "Cannot search for nothing!",
    "[1, 0]": "Use '.' instead of ','!",
    "[1, 1]": "Incorrect price format!",
    "[1, 2]": "No minimal price provided!",
    "[2, 0]": "No choice regarding promotion!",
    "[2, 1]": "Promotion choice must be either 'y' or 'n'!"
}

CHROMEDRIVER_PATH = "C:\\Program Files (x86)\\chromedriver.exe"

TXT_OUTPUT_PATH = "D:\\"

OLX_URL = "https://www.olx.pl"

SEARCH_BOX = "#headerSearch"

SEARCH_BUTTON = "#submit-searchmain"

VIEW_ALL_BUTTON = "#body-container > div:nth-child(3) > div > div.rel.listHandler > table.fixed.offers.breakword.offers--top.redesigned > tbody > tr:nth-child(1) > td > div > h2 > a > span"

COOKIES_CONSENT_BUTTON = "#cookiesBar > button"

LOGGED_IN_BUTTON = "#topLoginLink > span"

RESULTS_TABLE = "#body-container > div:nth-child(3) > div"

USER_SELECTOR = "#topLoginLink > i"

NO_COMMON_AUCTIONS_FOUND = "#body-container > div.wrapper > div > div.emptynew.large.lheight18 > p"

object_searched = ""

promoted_results_input = ""

search_obect_input = ""

next_page_selector = ""

cheapest_auction_url = ""

search_for_promoted_only = ""

free_text = "Za darmo"

currency_text = " zł"

txt_file_name = "searching_results.txt"

no_auctions_found_text = f"\nSorry! No auctions found for  \"{object_searched}\""

min_price = None

in_process = False

results_token = False

first_search = True

multiple_pages_search = False

browser_total_stop = False

promoted_results_stop = True

multiple_results_check_token = False

input_consent = [False, False, True]

relevant_auctions_array = []

communicate_array = []

results_title_label_array = []

input_error_warnings = []

cheapest_auction_for_gui = []

user_input_array = []

results_array = []

initial_index = 2

size = 0

advertisement = 0

browserNextPage_initial_index = 2

browserNextPage_initial_index_multiple_results = 3

browserNextPage_initial_index_assistant = 3

browserNextPage_initial_index_assistant_multiple_results = 4

found_auctions_sum = 0

gui_row_controller = 4

price_input = 0

last_row = 0

initial_limit = 0

max_pages_browsed = 12

potential_page_index = 10