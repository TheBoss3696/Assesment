from tkinter import *
from tkinter import messagebox
from tkinter import ttk

global bg

# quit subroutine
def quit():
    mw.destroy()


def print_store_details():
   global item_count, total_entries
   item_count = 0
   # Main labels
   Label(mw, font='bold', bg=bg, text="Row").grid(column=0, row=7)
   Label(mw, font='bold', bg=bg, text="Name").grid(column=1, row=7)
   Label(mw, font='bold', bg=bg, text="Receipt Number").grid(column=2, row=7)
   Label(mw, font='bold', bg=bg, text="Item Hired").grid(column=3, row=7)
   Label(mw, font='bold', bg=bg, text="Num. Items Hired").grid(column=4, row=7)

   while item_count < total_entries:
      Label(mw, text=item_count, bg=bg).grid(column=0, row=item_count + 8)
      Label(mw, text=(store_details[item_count][0]), bg=bg).grid(column=1, row=item_count + 8)
      Label(mw, text=(store_details[item_count][1]), bg=bg).grid(column=2, row=item_count + 8)
      Label(mw, text=(store_details[item_count][2]), bg=bg).grid(column=3, row=item_count + 8)
      Label(mw, text=(store_details[item_count][3]), bg=bg).grid(column=4, row=item_count + 8)
      item_count += 1


# This allows the user to Append the details

def append_name():
    global store_details, entry_customer_name, entry_receipt_number, entry_item_hired, entry_number_items_hired, total_entries, entries

    # Lists all possible boxes able to be filled and adds it to the rows
    entries = str([entry_customer_name, entry_receipt_number, entry_item_hired, entry_number_items_hired])
    store_details.append(
        [entry_customer_name.get(), entry_receipt_number.get(), entry_item_hired.get(), entry_number_items_hired.get()])
    # This clears out the old information after the details have been appended
    entry_customer_name.delete(0, 'end')
    entry_receipt_number.delete(0, 'end')
    entry_item_hired.delete(0, 'end')
    entry_number_items_hired.delete(0, 'end')
    total_entries += 1


def invis_text():
    entry_customer_name.insert(0, "Full Name")  # text inside entry box
    entry_receipt_number.insert(0, "Reciept number")
    entry_number_items_hired.insert(0, "1-500")

    entry_customer_name.bind("<FocusIn>", temp_text1)  # Deletes the temporary text once clicked on
    entry_number_items_hired.bind("<FocusIn>", temp_text2)  # Deletes the temporary text once clicked on
    entry_receipt_number.bind("<FocusIn>", temp_text3)  # Deletes the temporary text once clicked on


# This removes the temporary text

def temp_text1(e):  # function to delete text in entry box
    (entry_customer_name).delete(0, END)


def temp_text2(e):  # function to delete text in entry box
    (entry_number_items_hired).delete(0, END)


def temp_text3(e):  # function to delete text in entry box
    (entry_receipt_number).delete(0, END)


def check_inputs():
    # these are the global variables that are used
    global entry_customer_name, entry_receipt_number, entry_item_hired, entry_number_items_hired, total_entries
    input_check = 0
    Label(mw, text="                                  ",bg=bg).grid(column=2, row=2)
    Label(mw, text="                                  ",bg=bg).grid(column=2, row=3)
    Label(mw, text="                                  ",bg=bg).grid(column=5, row=3)
    Label(mw, text="                                  ",bg=bg).grid(column=2, row=5)
    # Check that customer name is not blank, set error text if blank
    if (entry_customer_name.get()) == "Full Name":
        Label(mw, fg="red", text="Required",bg=bg).grid(column=2, row=2,sticky="w")
        input_check = 1
    if (entry_customer_name.get().isdigit()) == True:
        Label(mw, fg="red", text="Text required",bg=bg).grid(column=2, row=2,sticky="w")
        input_check = 1
    # Check that receipt number is not blank, set error text if blank
    if entry_receipt_number.get().isdigit():
        if len(entry_receipt_number.get()) == 6:
            Label(mw, fg="red", text="Required",bg=bg).grid(column=2, row=3,sticky="w")
            input_check = 1
    else:
        Label(mw, fg="red", text="6 digits only",bg=bg).grid(column=2, row=3,sticky="w")
        input_check = 1

    # Check the number of hired items is not blank and between 1 and 200, set error text if blank
    if entry_number_items_hired.get().isdigit():
        if int(entry_number_items_hired.get()) < 1 or int(entry_number_items_hired.get()) > 500:
            Label(mw, fg="red", text="1-500 only",bg=bg).grid(column=5, row=3,sticky="w")
            input_check = 1
    else:
        Label(mw, text="            ").grid(column=5, row=3)
        Label_a = Label(mw, fg="red", text="Numbers Requires",bg=bg).grid(column=5, row=3,sticky="w")
        input_check = 1
    if input_check == 0:
        append_name()
        invis_text()


# delete a row from the list
def delete_row():
    global store_details, delete_item, total_entries, item_count
    del store_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0, 'end')
    # This deletes each items label
    Label(mw, text="              ").grid(column=0, row=item_count + 7)
    Label(mw, text="              ").grid(column=1, row=item_count + 7)
    Label(mw, text="              ").grid(column=2, row=item_count + 7)
    Label(mw, text="              ").grid(column=3, row=item_count + 7)
    Label(mw, text="              ").grid(column=4, row=item_count + 7)
    print_store_details()


# create the buttons and labels
def setup_buttons():
    global store_details, entry_customer_name, entry_receipt_number, entry_item_hired, entry_number_items_hired, total_entries, delete_item, Combobox
    Button(mw, text="Quit", command=quit, width=10, bg='red').grid(column=5, row=0, pady=pady_entries)
    # Button(mw, text="Receipt Print", command=new_window()).grid(column=3, row=3)
    Button(mw, text="Append Details", command=check_inputs).grid(column=1, row=5, pady=pady_entries)
    Button(mw, text="Print Details", command=print_store_details).grid(column=3, row=5, pady=pady_entries)

    Label(mw, text="Name").grid(column=0, row=2, padx=padx_entries)
    entry_customer_name = Entry(mw)
    entry_customer_name.grid(column=1, row=2, pady=pady_entries)
    Label(mw, text="Receipt Number").grid(column=0, row=3, padx=padx_entries)
    entry_receipt_number = Entry(mw)
    entry_receipt_number.grid(column=1, row=3, pady=pady_entries)

    Label(mw, text="Item Hired").grid(column=3, row=2, padx=padx_entries)
    item = StringVar()
    # Combo box to allow the user to scroll and choose different items
    entry_item_hired = ttk.Combobox(mw, textvariable=item, state="readonly",
                                    values=("BBQ LED_lights Balloons Party_animals"), width=17)
    entry_item_hired.grid(column=4, row=2, pady=pady_entries)

    Label(mw, text="NO. Hired").grid(column=3, row=3, padx=padx_entries)
    entry_number_items_hired = Entry(mw)
    entry_number_items_hired.grid(column=4, row=3, pady=pady_entries)

    Label(mw, text="Row #").grid(column=0, row=4, padx=padx_entries)
    delete_item = Entry(mw)
    delete_item.grid(column=1, row=4, pady=pady_entries)
    Button(mw, text="Delete", command=delete_row, padx=8).grid(column=2, row=4,sticky="W")

    Label(mw, text="Julies Store",font="bold",width = 12).grid( column=2, row=0,padx=20, pady=20)



# Creating a new window for receipt (Testing phase)
# def new_window():
#   global entry_receipt_number
#  # get selected items
# new = Toplevel(mw)
# new.geometry("500x500")
# Label(new, text=("Your Reciept Number:" + entry_receipt_number))


# start the program running
def main():
    global mw
    global store_details, total_entries, bg, pady_entries, padx_entries
    store_details = []
    total_entries = 0
    mw = Tk()
    bg = "cyan"
    pady_entries = 2
    padx_entries = 2
    # The Title
    mw.title("Julies Party Hire Store")
    mw.configure(bg='cyan')
    setup_buttons()
    invis_text()
    # This stops the user from being able to make the window larger/smaller
    mw.resizable(False, False)
    mw.mainloop()


main()
