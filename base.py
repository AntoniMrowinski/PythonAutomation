import seleniumDriver
import constants


def variablesWipe():
    constants.browser_total_stop = False
    constants.promoted_results_stop = True
    constants.relevant_auctions_array.clear()
    constants.next_page_selector = ""
    constants.cheapest_auction_url = ""
    constants.initial_index = 2
    constants.size = 0
    constants.advertisement = 0
    constants.browserNextPage_initial_index = 2
    constants.browserNextPage_initial_index_multiple_results = 3
    constants.browserNextPage_initial_index_assistant = 3
    constants.browserNextPage_initial_index_assistant_multiple_results = 4
    constants.multiple_pages_search = False
    constants.found_auctions_sum = 0
    constants.user_input_array = []
    constants.input_error_warnings.clear()
    constants.input_error_warnings = []
    constants.input_consent.clear()
    constants.input_consent = [False, False, True]


def backend_core():
    variablesWipe()
    while True:
        # Setting up selenium:
        chrome_driver_instance = seleniumDriver.Driver(constants.OLX_URL)
        chrome_driver_instance.setSelenium()
        seleniumDriver.chrome_driver.implicitly_wait(0.05)

        # Receiving relevant WebElements:
        searcher_box = chrome_driver_instance.findMeElement(constants.SEARCH_BOX)
        searching_button = chrome_driver_instance.findMeElement(constants.SEARCH_BUTTON)
        cookies_consent_button = chrome_driver_instance.findMeElement(constants.COOKIES_CONSENT_BUTTON)

        # Checking whether the user is logged in (still in development) and clearing coursor placement:
        user_tab = chrome_driver_instance.findMeElement(constants.LOGGED_IN_BUTTON)
        elicit_user_tab_reaction = chrome_driver_instance.putCursourAtElement(user_tab, seleniumDriver.chrome_driver)
        elicit_user_tab_reaction.click_and_hold(user_tab)
        chrome_driver_instance.eliminateCoursorAtElement(elicit_user_tab_reaction)

        # Searching OLX for the search object and clicking to see all that are promoted:
        # Cookies consent is necessary due to the interception they cause while being displayed.
        # "See all" button may required multiple attempts of clicking.
        if constants.first_search:
            chrome_driver_instance.clickElement(cookies_consent_button)
        constants.first_search = False
        chrome_driver_instance.clickElement(searcher_box)
        chrome_driver_instance.putText(searcher_box, constants.object_searched)
        chrome_driver_instance.clickElement(searching_button)

        # Checks whether the user is searching only for promoted auctions.
        # If so, it enters the only-promoted section on OLX
        # If no results are found, an appropriate text is put into searching_results.txt file and onto the tkinter GUI.
        if constants.search_for_promoted_only == 1:
            current_browser = seleniumDriver.chrome_driver.current_url
            promoted_auctions = seleniumDriver.seeAllButtonClicker(chrome_driver_instance, current_browser)
            if not promoted_auctions:
                seleniumDriver.writeToTxt([], True)
                break

        # Checks whether any auctions are going to be found before the main browsing loop.
        # If not, an appropriate text is put into searching_results.txt file and onto the tkinter GUI.
        if seleniumDriver.checkNoCommonAuctionsFound():
            seleniumDriver.writeToTxt([], True)
            break

        # Information operations:
        # Browsing page/pages of the results to search for auctions.
        # Auctions which are not ads and contain price are saved and put with further information into an array.
        # The array is printed into the .txt file with the information about the cheapest auction
        # (not cheaper than the price given by the user)
        # After processing, the user is directed to the cheapest auction URL
        # If there is no cheapest auction within the limit imposed by the user, the browser is closed.
        #   ! The chromedriver.exe process remains active after closing Chrome MANUALLY
        #   as the code does not quit Selenium !
        #   ! Quitting Selenium would cause closing the page with the cheapest auction found !
        seleniumDriver.auctionBrowser()
        # Produces an ordered table based on the original table of results which is easier to manipulate.
        ordered_table = seleniumDriver.tableOrderer(constants.relevant_auctions_array)
        seleniumDriver.writeToTxt(ordered_table, False)
        try:
            chrome_driver_instance.goToPage(constants.cheapest_auction_url)
        except:
            chrome_driver_instance.quitSelenium()
        return ordered_table
        order_table.clear()
        break