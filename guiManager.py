from tkinter import *
import constants
import base
import seleniumDriver


results_font_size = 11
font_size = 13
font_type = "Calibri"
results_column = 0
results_row = 5
column_span = 4

root = Tk()
root.title("Olx Browser 1.0")
root.anchor(CENTER)

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

button_field_row = 4
button_field_column = 3

def processSygnaliser():
    constants.search_obect_input = search_object_field.get()
    search_object_label = Label(root, text=f"Will search for: \"{constants.search_obect_input}\"  ")
    search_object_label.config(font=(font_type, font_size))
    search_object_label.grid(row=search_label_row, column=search_label_column)
    constants.price_input = price_field.get()
    price_label = Label(root, text=f"Set minimal price limit: {constants.price_input}  ")
    price_label.config(font=(font_type, font_size))
    price_label.grid(row=price_label_row, column=price_label_column)
    constants.promoted_results_input = promoted_field.get()
    promoted_results_label = Label(root, text=f"Only promoted results: {constants.promoted_results_input}  ")
    promoted_results_label.config(font=(font_type, font_size))
    promoted_results_label.grid(row=promoted_label_row, column=promoted_label_column)
    wait_for_searching_text = Label(root, text=f"Searching for \"{constants.search_obect_input}\"...\n\t"
                                               f"Do not interrupt the browser!")
    wait_for_searching_text.config(font=(font_type, font_size))
    wait_for_searching_text.grid(row=wait_for_searching_row, column=wait_for_searching_column, pady=5, columnspan=2)
    root.update()

def confirmButton1():
    processSygnaliser()
    full_table = base.my_main()
    drawResults(full_table)


def drawResults(full_array):
    blankSpaceInserter(results_row,7)
    # print(f"constants.initial_limit= {constants.initial_limit}")
    # print(f"constants.last_row= {constants.last_row}")
    # for x in range(constants.initial_limit, 1111):
    #     print("czyszcze")
    #     clear_label = Label(root)
    #     clear_label.grid(row=x, column=results_column)
    #     clear_label.selection_clear()
    # constants.gui_row_controller = 7
    for element in seleniumDriver.fullTablePrinter(full_array, 2):
        insert_label = Label(root, text=element)
        insert_label.config(font=(font_type, results_font_size))
        insert_label.grid(row=constants.gui_row_controller, column=results_column, columnspan=column_span, padx=5)
        constants.gui_row_controller += 1
        constants.last_row = constants.gui_row_controller
        # print(constants.last_row)
    insert_label = Label(root, text="\n")
    insert_label.grid(row=constants.gui_row_controller, column=results_column, columnspan=column_span)
    root.update()


def blankSpaceInserter(blankx,range_limit):
    for x in range(blankx, range_limit):
        linex = Label(root, text=" ")
        linex.grid(row=x, column=0)
        if x == range_limit-1:
            linex = Label(root, text="Results:\n")
            linex.config(font=(font_type, font_size))
            linex.grid(row=x, column=0, columnspan=column_span)
    constants.gui_row_controller = range_limit
    constants.initial_limit = range_limit


search_text = Label(root, text="Search for:")
search_text.config(font=(font_type, font_size))
price_text = Label(root, text="Minimal price:")
price_text.config(font=(font_type, font_size))
promotion_text = Label(root, text="Look only for promoted (y\\n): ")
promotion_text.config(font=(font_type, font_size))
search_object_field = Entry(root)
price_field = Entry(root)
promoted_field = Entry(root)
confirm_button1 = Button(root, text="Confirm data", command=confirmButton1, padx=5, pady=5, borderwidth=5)

search_text.grid(row=search_text_row, column=search_text_column, padx=5, pady=5)
price_text.grid(row=price_text_row, column=price_text_column, padx=5, pady=5)
promotion_text.grid(row=promotion_text_row, column=promotion_text_column, padx=5, pady=5)
search_object_field.grid(row=search_field_row, column=search_field_column, padx=5, pady=5)
price_field.grid(row=price_field_row, column=price_field_column, padx=5, pady=5)
promoted_field.grid(row=promotion_field_row, column=promotion_field_column, padx=5, pady=5)
confirm_button1.grid(row=button_field_row, column=button_field_column, padx=5, pady=5)

root.mainloop()
