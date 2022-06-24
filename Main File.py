"""
This is Julies hire store
By:Giavin Moodley
"""
# This imports Tkinter
from tkinter import *
from tkinter import ttk


# quit subroutine
def quit():
    main_win.destroy()


"""
Print store details - This is when the user presses append and all the information gained from the entry boxes 
are printed into a receipt below the buttons. This definition includes the labels for each section such as the 
name receipt number, what they hired and how many. While also stating the row number so they can delete it.
"""
def print_store_details():
   global item_count, total_entries
   item_count = 0
   # Main labels to be printed
   Label(main_win, font='bold', bg=background_colour, text="Row").grid(column=0, row=7)
   Label(main_win, font='bold', bg=background_colour, text="Name").grid(column=1, row=7)
   Label(main_win, font='bold', bg=background_colour, text="Receipt Number").grid(column=2, row=7)
   Label(main_win, font='bold', bg=background_colour, text="Item Hired").grid(column=3, row=7)
   Label(main_win, font='bold', bg=background_colour, text="Num. Items Hired").grid(column=4, row=7)

   while item_count < total_entries:
      Label(main_win, text=item_count, bg=background_colour).grid(column=0, row=item_count + 8)
      Label(main_win, text=(store_details[item_count][0]), bg=background_colour, padx=20).grid(column=1, row=item_count + 8)
      Label(main_win, text=(store_details[item_count][1]), bg=background_colour, padx=20).grid(column=2, row=item_count + 8)
      Label(main_win, text=(store_details[item_count][2]), bg=background_colour, padx=20).grid(column=3, row=item_count + 8)
      Label(main_win, text=(store_details[item_count][3]), bg=background_colour, padx=20).grid(column=4, row=item_count + 8)
      item_count += 1


# This allows the user to Append the details

def append_name():
    # globalise the names so other definition functions can use them
    global store_details, entry_customer_name, entry_receipt_number, entry_item_hired, entry_number_items_hired, total_entries, entries
# Inorder to append all details each entry has been gotten(.get) and placed within a list function for easier appending
    store_details.append(
        [entry_customer_name.get(), entry_receipt_number.get(), entry_item_hired.get(), entry_number_items_hired.get()])
    # This clears out the old information after the details have been appended
    entry_customer_name.delete(0, 'end')
    entry_receipt_number.delete(0, 'end')
    # since this is a combo box the information cannot be deleted so it is set to blank ("")
    entry_item_hired.set("")
    entry_number_items_hired.delete(0, 'end')
    # add 1 to total entries
    total_entries += 1

# invis text is the temporary text which sits inside the entry boxes
def invis_text():
    entry_customer_name.insert(0, "Full Name")  # text inside entry box
    entry_receipt_number.insert(0, "Reciept number")  # text inside entry box
    entry_number_items_hired.insert(0, "1-500")  # text inside entry box

    entry_customer_name.bind("<FocusIn>", temp_text1)  # Deletes the temporary text once clicked on
    entry_number_items_hired.bind("<FocusIn>", temp_text2)  # Deletes the temporary text once clicked on
    entry_receipt_number.bind("<FocusIn>", temp_text3)  # Deletes the temporary text once clicked on


# This removes the temporary text

def temp_text1(e):  # function to delete text in entry box
    (entry_customer_name).delete(0, END)


# This removes the temporary text
def temp_text2(e):  # function to delete text in entry box
    (entry_number_items_hired).delete(0, END)


# This removes the temporary text
def temp_text3(e):  # function to delete text in entry box
    (entry_receipt_number).delete(0, END)


""" This function is the main constraints and check if the user had inputted the correct thing and if 
not it gives  an error.
"""
def label_remove():
    # To remove all labels
    Label(main_win, text="                                  ", bg=background_colour).grid(column=2, row=2, stick="W")
    Label(main_win, text="                                  ", bg=background_colour).grid(column=2, row=3, stick="W")
    Label(main_win, text="                                  ", bg=background_colour).grid(column=5, row=2, stick="W")
    Label(main_win, text="                                  ", bg=background_colour).grid(column=5, row=3, stick="W")

def check_inputs():
    # these are the global variables that are used
    global entry_customer_name, entry_receipt_number, entry_item_hired, entry_number_items_hired, total_entries
    input_check = 0
    label_remove()
    # Check that customer name is not blank, set error text if blank
    if (entry_customer_name.get()) == "Full Name" or len(entry_customer_name.get()) == 0:
        Label(main_win, fg="red", text="Required", bg=background_colour).grid(column=2, row=2, sticky="w")
        input_check = 1
        # To check if the user had inputted a number instead of text
    if (entry_customer_name.get().isdigit()) == True:
        Label(main_win, fg="red", text="Text required", bg=background_colour).grid(column=2, row=2, sticky="w")
        input_check = 1
    # Check that receipt number is a digit and is not blank, set error text if blank
    if entry_receipt_number.get().isdigit():
        if len(entry_receipt_number.get()) != 6:
            Label(main_win, fg="red", text="6 Digits Required", bg=background_colour).grid(column=2, row=3, sticky="w")
            input_check = 1
            # If the receipt number was incorrect
    else:
        Label(main_win, fg="red", text="Digits only", bg=background_colour).grid(column=2, row=3, sticky="w")
        input_check = 1

    # Check the number of hired items is not blank and between 1 and 500, set error text if blank
    if entry_number_items_hired.get().isdigit():
        if int(entry_number_items_hired.get()) < 1 or int(entry_number_items_hired.get()) > 500:
            Label(main_win, fg="red", text="1-500 only", bg=background_colour).grid(column=5, row=3, sticky="w")
            input_check = 1
            # if text was added instead of numbers
    else:
        Label(main_win, fg="red", text="Numbers Required", bg=background_colour).grid(column=5, row=3, sticky="w")
        input_check = 1
        # Check if anything has been selected for the combobox
    if len(entry_item_hired.get()) == 0:
        Label(main_win, fg="red", text="Select item", bg=background_colour).grid(column=5, row=2, sticky="w")
        input_check=1
        # If there are no errors it will let the program to continue
    if input_check == 0:
        append_name()
        invis_text()


# delete a row from the list
def delete_row():
    global store_details, delete_item, total_entries, item_count
    # this is so that all previous error text is removed
    Label(main_win, text="                                        ", bg=background_colour).grid(column=2, row=4, padx=5, sticky="W")
    if delete_item.get().isdigit():
        if int(delete_item.get()) < total_entries:
            del store_details[int(delete_item.get())]
            total_entries = total_entries - 1
            delete_item.delete(0, 'end')
            # This deletes all of the labels for that row
            Label(main_win, text="                                    ", bg=background_colour).grid(column=0, row=item_count + 7)
            Label(main_win, text="                                    ", bg=background_colour).grid(column=1, row=item_count + 7)
            Label(main_win, text="                                    ", bg=background_colour).grid(column=2, row=item_count + 7)
            Label(main_win, text="                                    ", bg=background_colour).grid(column=3, row=item_count + 7)
            Label(main_win, text="                                    ", bg=background_colour).grid(column=4, row=item_count + 7)
            print_store_details()
            # This states that the row the user wants to delete does not exists
        else:
            Label(main_win, text="Row Does Not Exist", bg=background_colour, fg="red").grid(column=2, row=4, padx=padx_entries, sticky="W")
        # This states that a Row number is require
    else:
        Label(main_win, text="Row Number Required", bg=background_colour, fg="red").grid(column=2, row=4, padx=padx_entries, sticky="W")



# create the buttons and labels
def setup_buttons():
    global store_details, entry_customer_name, entry_receipt_number, entry_item_hired, entry_number_items_hired, item, total_entries, delete_item, Combobox
    item = StringVar()
    # Buttons with their commands which link back to the functions(def) and its location on the window
    Button(main_win, text="Quit", command=quit, width=10, bg='red', font="Times 12 bold").grid(column=5, row=0, pady=pady_entries, sticky="NW")
    Button(main_win, text="Append Details", command=check_inputs).grid(column=0, row=5, pady=pady_entries)
    Button(main_win, text="Print Details", command=print_store_details).grid(column=3, row=5, pady=pady_entries)

    # Label name and its location on the window
    Label(main_win, text="Name").grid(column=0, row=2, padx=padx_entries)
    entry_customer_name = Entry(main_win)
    entry_customer_name.grid(column=1, row=2, pady=pady_entries)

    # label receipt number and its location on the window
    Label(main_win, text="Receipt Number").grid(column=0, row=3, padx=padx_entries)
    entry_receipt_number = Entry(main_win)
    entry_receipt_number.grid(column=1, row=3, pady=pady_entries)

    # label item hired and its location on the window
    Label(main_win, text="Item Hired").grid(column=3, row=2, padx=padx_entries)

    # Combo box to allow the user to scroll and choose different items
    entry_item_hired = ttk.Combobox(main_win, textvariable=item, state="readonly", width=17)
    entry_item_hired["values"] = ("BBQ", "LED lights", "Balloons", "Party Animals", "Bar Fridge", "LED Bench Set",
                                  "Birthday Pack", "Confetti", "Cups", "Pool Toys", "Inflatable Pool", "Helium Balloons")
    entry_item_hired.grid(column=4, row=2, pady=pady_entries)

    # label for number hired and its location on the window
    Label(main_win, text="NO. Hired").grid(column=3, row=3, padx=padx_entries)
    entry_number_items_hired = Entry(main_win)
    entry_number_items_hired.grid(column=4, row=3, pady=pady_entries)

    # delete row and its labels and its location on the window
    Label(main_win, text="Row #").grid(column=0, row=4, padx=padx_entries)
    delete_item = Entry(main_win)
    delete_item.grid(column=1, row=4, pady=pady_entries)
    Button(main_win, text="Delete", command=delete_row, padx=8).grid(column=1, row=5)

    # Main store label
    Label(main_win, text="Julies Store", font="Times 20 bold", width=12).grid(column=2, row=0, padx=20, pady=20, sticky="N")

# start the program running
def main():
    global main_win
    global store_details, total_entries, background_colour, pady_entries, padx_entries
    store_details = []
    total_entries = 0
    # change the name of the main window
    main_win = Tk()
    # variables to help easily change small things such as colour and spacing for entries/labels
    background_colour = "seagreen1"
    pady_entries = 5
    padx_entries = 5
    # The Title of the window
    main_win.title("Julies Party Hire Store")
    # window colour (change from bg)
    main_win.configure(bg=background_colour)
    setup_buttons()
    invis_text()
    # This stops the user from being able to make the window larger/smaller
    main_win.resizable(False, False)
    main_win.mainloop()


main()
