from tkinter import *
import constants
import base
import seleniumDriver


root = Tk()
root.title("Olx Browser 1.0")
root.anchor(NW)
root.geometry("+10+10")

search_text = "Search for:"

price_text = "Minimal price:"

promoted_text = "Search for promoted ONLY:"

confirm_button_text = "Search"

delete_button_text = "Clear Results"

go_to_txt_text = f"\nGo to searching_results.txt for other search details."

txt_multiple_results_text = f"\nGo to searching_results.txt in {constants.TXT_OUTPUT_PATH} to see full results."

cheapest_auction_text = "\nThe chapest auction: >>  \"{}\"  << Price: {} zł\n"

no_results_text = "No results found!\n"

results_text = "Results:"

no_cheapest_auction_found = "No auction found above the limit imposed by the user!\n"

font_type = "Calibri"

font_size = 13

fields_width = 14

y_spacing = 5

x_spacing = 5

results_font_size = 11

results_column = 0

results_row = 4

column_span = 3

search_label_row = 0

search_label_column = 3

price_label_row = 1

price_label_column = 3

promoted_label_row = 2

promoted_label_column = 3

search_text_row = 0

search_text_column = 0

price_text_row = 1

price_text_column = 0

promotion_text_row = 2

promotion_text_column = 0

wait_for_searching_row = 4

wait_for_searching_column = 0

search_field_row = 0

search_field_column = 1

price_field_row = 1

price_field_column = 1

promotion_field_row = 2

promotion_field_column = 1

button_field_row = 2

button_field_column = 2

# Displays errors regarding input, may present multiple errors at once.
# The text of an error depends on the input_error_warnings array which is matched with the errors dictionary.
def inputErrorPrinter():
    error_text = ""
    communicateDestroyer()
    for error in constants.input_error_warnings:
        error_text += constants.errors_dictionary[str(error)] + "\n"
        errorlabel = Label(root, text=error_text)
        constants.communicate_array.append(errorlabel)
        errorlabel.config(font=(font_type, font_size), foreground="red")
        errorlabel.grid(row=wait_for_searching_row, column=wait_for_searching_column, pady=5, rowspan= 1, columnspan=3)
    root.update()


# Eliminates labels of errors, result title, searching-process label and more.
# It does not clear the results!
def communicateDestroyer():
    for communicate_label in constants.communicate_array:
        communicate_label.destroy()

# Prints prompts about on-going searching process or successful completion of this process.
# If there are more than 10 auctions found, the rest of the results is kept in the searching_results.txt file.
def processSygnaliser(full_array):
    if not constants.results_token:
        communicateDestroyer()
        constants.search_obect_input = search_object_field.get()
        constants.price_input = price_field.get()
        constants.promoted_results_input = checkbox_value.get()
        seleniumDriver.userInputReception()
        consent_sum = constants.input_consent[0] and constants.input_consent[1] and constants.input_consent[2]
        if consent_sum != True:
            inputErrorPrinter()
            return False
        wait_for_searching_text = Label(root, text=f"Searching for \"{constants.search_obect_input}\"...\n\t"
                                                   f"Do not interrupt the browser!\n")
        constants.communicate_array.append(wait_for_searching_text)
        constants.results_title_label_array.append(wait_for_searching_text)
        wait_for_searching_text.config(font=(font_type, font_size))
        wait_for_searching_text.grid(row=wait_for_searching_row, column=wait_for_searching_column, pady=5, rowspan= 1, columnspan=3)
        root.update()
        return True
    else:
        if len(full_array) > 10:
            wait_for_searching_text = Label(root, text= f"Done!\nFirst 10 auctions out of {len(full_array)} total for \"{constants.object_searched}\":")
        else:
            wait_for_searching_text = Label(root, text= f"Done!\nFound {len(full_array)} auctions total for \"{constants.object_searched}\":")
        constants.communicate_array.append(wait_for_searching_text)
        constants.results_title_label_array.append(wait_for_searching_text)
        wait_for_searching_text.config(font=(font_type, font_size+2), fg="#00CD00")
        wait_for_searching_text.grid(row=wait_for_searching_row, column=wait_for_searching_column, pady=5, rowspan=1, columnspan=3)
        root.update()
        return True

# Starts the process of searching if all input fields are filled up correctly
# and the process of searching haven't started already.
# It clears older results, thus initial view of the programme window is displayed.
# Searching and result-clearing buttons remain disabled until the searching process finishes.
def confirmButton():
    constants.results_token = False
    successful_input = processSygnaliser([])
    if successful_input:
        autoResultsClearing()
        root.update()
        confirm_button1.configure(state='disabled')
        processSygnaliser([])
        full_table = base.backend_core()
        constants.results_token = True
        drawResults(full_table)
        confirm_button1.configure(state='normal')
        clear_button.configure(state='normal')
    else:
        constants.results_token = True

# Clears current results from in GUI, does not check the presence of the recent results (results_token).
# Does not delete all communicates as in clearOldResults()
def autoResultsClearing():
    for label_insert in constants.results_array:
        label_insert.destroy()
    for labels in constants.results_title_label_array:
        labels.destroy()
    clear_button.configure(state='disabled')
    constants.results_token = False


# Clears results and communicates in the GUI. Used when the clearing_button is pressed.
def clearOldResults():
    if constants.results_token == True:
        # clear_button.configure(state='normal')
        for label_insert in constants.results_array:
            label_insert.destroy()
        for labels in constants.communicate_array:
            labels.destroy()
        clear_button.configure(state='disabled')
    constants.results_token = False


# Creates separate labels for up to 10 results found. If no results are found, an appropriate message is displayed.
# Provided there are more than 10 results, only first 10 are shown, the rest is kept in the searching_results.txt file.
# Also, it prints the information about the cheapes auction within the lower limit given by the user
# (limit, auction name, price).
def drawResults(full_array):
    blankSpaceInserter(results_row, 5)
    if full_array == None:
        communicateDestroyer()
        label = Label(root, text=no_results_text)
        constants.communicate_array.append(label)
        label.config(font=(font_type, 20), fg="#FF0000")
        label.grid(row=constants.gui_row_controller, column=results_column, columnspan=column_span, padx=x_spacing)
    else:
        for element in seleniumDriver.fullTablePrinter(full_array, 2)[:10]:
            label = Label(root, text=element, relief="ridge", borderwidth=2, bg='#FFFFFF', padx=x_spacing, pady=y_spacing)
            constants.results_array.append(label)
            label.config(font=(font_type, results_font_size))
            label.grid(row=constants.gui_row_controller, column=results_column, columnspan=column_span)
            constants.gui_row_controller += 1
        constants.last_row = constants.gui_row_controller
        space_label = Label(root, text="\n")
        space_label.grid(row=constants.gui_row_controller, column=results_column, columnspan=column_span)
        try:
            price_str, name_str, auction_index, limit_imposed_by_the_user = constants.cheapest_auction_for_gui
            cheapest_auction_insert = cheapest_auction_text.format(name_str, price_str)
        except:
            cheapest_auction_insert = no_cheapest_auction_found
        if len(full_array) > 10:
            cheapest_auction_insert += txt_multiple_results_text
        else:
            cheapest_auction_insert += go_to_txt_text
        cheapest_auction_label = Label(root, text=cheapest_auction_insert, anchor=W)
        cheapest_auction_label.config(font=(font_type, 15))
        cheapest_auction_label.grid(row=constants.gui_row_controller+1, column=results_column, columnspan=column_span)
        constants.communicate_array.append(cheapest_auction_label)
        constants.communicate_array.append(space_label)
        constants.results_array.append(space_label)
        processSygnaliser(full_array)
        constants.results_token = True
        root.update()

# Introduces spacing between the results section and the input/communicate section.
def blankSpaceInserter(blankx,range_limit):
    for x in range(blankx, range_limit):
        linex = Label(root, text=" ")
        linex.grid(row=x, column=0)
        if x == range_limit-1:
            linex = Label(root, text=results_text, pady=10)
            constants.results_title_label_array.append(linex)
            constants.communicate_array.append(linex)
            linex.config(font=(font_type, 20))
            linex.grid(row=x, column=0, columnspan=column_span)
    constants.gui_row_controller = range_limit
    constants.initial_limit = range_limit


search_text_label = Label(root, text=search_text)
search_text_label.config(font=(font_type, font_size), relief="flat")
price_text_label = Label(root, text=price_text)
price_text_label.config(font=(font_type, font_size))
promotion_text_label = Label(root, text=promoted_text)
promotion_text_label.config(font=(font_type, font_size))
search_object_field = Entry(root)
search_object_field.config(width=fields_width)
price_field = Entry(root)
price_field.config(width=fields_width)
checkbox_value = IntVar()
promotion_checkbox = Checkbutton(root, variable=checkbox_value)
confirm_button1 = Button(root, text=confirm_button_text, command=confirmButton, padx=x_spacing, pady=y_spacing, borderwidth=5)
clear_button = Button(root, text=delete_button_text, command=clearOldResults, padx=x_spacing, pady=y_spacing, borderwidth=5)
clear_button.config(state='disabled')

search_text_label.grid(row=search_text_row, column=search_text_column, padx=x_spacing, pady=y_spacing)
price_text_label.grid(row=price_text_row, column=price_text_column, padx=x_spacing, pady=y_spacing)
promotion_text_label.grid(row=promotion_text_row, column=promotion_text_column, padx=x_spacing, pady=y_spacing)
search_object_field.grid(row=search_field_row, column=search_field_column, padx=x_spacing, pady=y_spacing)
price_field.grid(row=price_field_row, column=price_field_column, padx=x_spacing, pady=y_spacing)
promotion_checkbox.grid(row=promotion_field_row, column=promotion_field_column, padx=x_spacing, pady=y_spacing)
confirm_button1.grid(row=button_field_row, column=button_field_column, padx=x_spacing, pady=y_spacing)
clear_button.grid(row=0, column=2, padx=x_spacing, pady=y_spacing)

root.mainloop()
