from tkinter import *
import constants
import base
import seleniumDriver

root = Tk()
root.title("Olx Browser 1.0")
root.anchor(NW)

results_font_size = 11
font_size = 13
font_type = "Calibri"
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

def inputErrorPrinter():
    error_text = ""
    communicateDestroyer()
    # constants.communicate_array = []
    for error in constants.input_error_warnings:
        error_text += constants.errors_dictionary[str(error)] + "\n"
        errorlabel = Label(root, text=error_text)
        constants.communicate_array.append(errorlabel)
    errorlabel.config(font=(font_type, font_size), foreground="red")
    errorlabel.grid(row=wait_for_searching_row, column=wait_for_searching_column, pady=5, rowspan= 1, columnspan=3)
    root.update()

def communicateDestroyer():
    for communicate_label in constants.communicate_array:
        communicate_label.destroy()

def processSygnaliser(full_array):
    if not constants.results_token:

        #wipe all communicates
        communicateDestroyer()

        constants.search_obect_input = search_object_field.get()
        constants.price_input = price_field.get()
        constants.promoted_results_input = promoted_field.get()
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
        wait_for_searching_text = Label(root, text= f"Done!\n\nFound {len(full_array)} auctions total for \"{constants.object_searched}\"\n")
        constants.communicate_array.append(wait_for_searching_text)
        constants.results_title_label_array.append(wait_for_searching_text)
        wait_for_searching_text.config(font=(font_type, font_size))
        wait_for_searching_text.grid(row=wait_for_searching_row, column=wait_for_searching_column, pady=5, rowspan=1, columnspan=3)
        root.update()
        return True

def sliderAction1(place_holder):
    slider_position = slider.get()
    root.geometry("100x100")
    width = root.winfo_reqwidth()
    root.geometry(f"{width}x{slider_position}")


def confirmButton1():
    constants.results_token = False
    successful_input = processSygnaliser([])
    if successful_input:
        autoResultsDelete()
        root.update()
        confirm_button1.configure(state='disabled')
        processSygnaliser([])
        full_table = base.my_main()
        constants.results_token = True
        drawResults(full_table)
        confirm_button1.configure(state='normal')
        delete_button.configure(state='normal')
    else:
        constants.results_token = True

def autoResultsDelete():
    for label_insert in constants.results_array:
        label_insert.destroy()
    for labels in constants.results_title_label_array:
        labels.destroy()
    delete_button.configure(state='disabled')
    constants.results_token = False

def deleteOldResults():
    if constants.results_token == True:
        delete_button.configure(state='normal')
        for label_insert in constants.results_array:
            label_insert.destroy()
        for labels in constants.communicate_array:
            labels.destroy()
        delete_button.configure(state='disabled')
    constants.results_token = False


def drawResults(full_array):
    blankSpaceInserter(results_row, 6)
    if full_array == None:
        communicateDestroyer()
        label = Label(root, text="No results found!\n")
        constants.communicate_array.append(label)
        label.config(font=(font_type, results_font_size))
        label.grid(row=constants.gui_row_controller, column=results_column, columnspan=column_span, padx=5)
    else:
        for element in seleniumDriver.fullTablePrinter(full_array, 2):
            label = Label(root, text=element)
            constants.results_array.append(label)
            label.config(font=(font_type, results_font_size))
            label.grid(row=constants.gui_row_controller, column=results_column, columnspan=column_span)
            constants.gui_row_controller += 1
        constants.last_row = constants.gui_row_controller
        space_label = Label(root, text="\n")
        space_label.grid(row=constants.gui_row_controller, column=results_column, columnspan=column_span)

        price_str, name_str, auction_index, limit_imposed_by_the_user = constants.cheapest_auction_for_gui
        cheapest_auction_insert = "\nThe lowest-price limit imposed by the user: {} zł\n\nThe chapest auction:\t ---->  \"{}\"  <----\n\nPrice:\t{} zł\n\nLink:\t{}\n".format(limit_imposed_by_the_user, name_str, price_str, constants.cheapest_auction_url)
        cheapest_auction_label = Label(root, text=cheapest_auction_insert, anchor=W)
        cheapest_auction_label.grid(row=constants.gui_row_controller+1, column=results_column, columnspan=column_span)
        constants.communicate_array.append(cheapest_auction_label)
        constants.communicate_array.append(space_label)
        constants.results_array.append(space_label)
        processSygnaliser(full_array)
        constants.results_token = True
        root.update()

def blankSpaceInserter(blankx,range_limit):
    for x in range(blankx, range_limit):
        linex = Label(root, text=" ")
        linex.grid(row=x, column=0)
        if x == range_limit-1:
            linex = Label(root, text="Results:\n")
            constants.results_title_label_array.append(linex)
            constants.communicate_array.append(linex)
            linex.config(font=(font_type, font_size))
            linex.grid(row=x, column=0, columnspan=column_span)
    constants.gui_row_controller = range_limit
    constants.initial_limit = range_limit


search_text = Label(root, text="Search for:")
search_text.config(font=(font_type, font_size), relief="flat")
price_text = Label(root, text="Minimal price:")
price_text.config(font=(font_type, font_size))
promotion_text = Label(root, text="Search for promoted ONLY (y\\n): ")
promotion_text.config(font=(font_type, font_size))
search_object_field = Entry(root)
price_field = Entry(root)
promoted_field = Entry(root)
confirm_button1 = Button(root, text="Search", command=confirmButton1, padx=5, pady=5, borderwidth=5)
delete_button = Button(root, text="Clear Results", command=deleteOldResults, padx=5, pady=5, borderwidth=5)
delete_button.configure(state='disabled')
slider = Scale(root, from_=300, to=800, command=sliderAction1)

search_text.grid(row=search_text_row, column=search_text_column, padx=5, pady=5)
price_text.grid(row=price_text_row, column=price_text_column, padx=5, pady=5)
promotion_text.grid(row=promotion_text_row, column=promotion_text_column, padx=5, pady=5)
search_object_field.grid(row=search_field_row, column=search_field_column, padx=5, pady=5)
price_field.grid(row=price_field_row, column=price_field_column, padx=5, pady=5)
promoted_field.grid(row=promotion_field_row, column=promotion_field_column, padx=5, pady=5)
confirm_button1.grid(row=button_field_row, column=button_field_column, padx=5, pady=5)
delete_button.grid(row=0, column=2, padx=5, pady=5)
# slider.grid(row=0, column=4, padx=5, pady=5, columnspan=4)

root.mainloop()
