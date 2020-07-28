import seleniumDriver
import constants


# Receiving input from the user:
seleniumDriver.userInputReception()

while True:
    # Setting up selenium:
    chrome_driver_instance = seleniumDriver.Driver(constants.OLX_URL)
    chrome_driver_instance.setSelenium()
    constants.chrome_driver.implicitly_wait(0.1)

    # Receiving relevant WebElements:
    searcher_box = chrome_driver_instance.findMeElement(constants.SEARCH_BOX)
    searching_button = chrome_driver_instance.findMeElement(constants.SEARCH_BUTTON)
    cookies_consent_button = chrome_driver_instance.findMeElement(constants.COOKIES_CONSENT_BUTTON)

    # Checking whether the user is logged in (still in development) and clearing coursor placement:
    user_tab = chrome_driver_instance.findMeElement(constants.LOGGED_IN_BUTTON)
    elicit_user_tab_reaction = chrome_driver_instance.putCursourAtElement(user_tab, constants.chrome_driver)
    elicit_user_tab_reaction.click_and_hold(user_tab)
    chrome_driver_instance.eliminateCoursorAtElement(elicit_user_tab_reaction)

    # Searching OLX for the search object and clicking to see all that are promoted:
    # Cookies consent is necessary due to the interception they cause while being displayed.
    # "See all" button may required multiple attempts of clicking.
    chrome_driver_instance.clickElement(cookies_consent_button)
    chrome_driver_instance.clickElement(searcher_box)
    chrome_driver_instance.putText(searcher_box, constants.object_searched)
    chrome_driver_instance.clickElement(searching_button)
    seleniumDriver.seeAllButtonClicker(chrome_driver_instance)

    # Information operations:
    # Browsing page/pages of the results to search for auctions.
    # Auctions which are not ads and contain price are saved and put with further information into an array.
    # The array is printed into the .txt file with the information about the cheapest auction
    # (not cheaper than the price given by the user)
    # After processing, the user is directed to the cheapest auction URL
    #   ! The chromedriver.exe process remains active after closing Chrome manually as the code does not quit selenium !
    #   ! Quitting selenium would cause closing the page with the cheapest auction found !
    seleniumDriver.auctionBrowser()
    ordered_table = seleniumDriver.tableOrderer(constants.relevant_auctions_array)
    seleniumDriver.writeToTxt(ordered_table)
    chrome_driver_instance.goToPage(constants.cheapest_auction_url)
    print(f"\nDone!\n\tGo to searching_results.txt in {constants.TXT_OUTPUT_PATH} to see full results.")
    break