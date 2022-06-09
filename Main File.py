
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import ttk


# quit subroutine
def quit():
    mw.destroy()



def print_store_details():
    global item_count, total_entries
    item_count = 0
    Label(mw, font='bold', text="Row").grid(column=0, row=7)
    Label(mw, font='bold', text="Name").grid(column=1, row=7)
    Label(mw, font='bold', text="Reciept Number").grid(column=2, row=7)
    Label(mw, font='bold', text="Item Hired").grid(column=3, row=7)
    Label(mw, font='bold', text="Num. Items Hired").grid(column=4, row=7)

    while item_count < total_entries:
        Label(mw, text=item_count).grid(column=0, row=item_count + 8)
        Label(mw, text=(store_details[item_count][0])).grid(column=1, row=item_count + 8)
        Label(mw, text=(store_details[item_count][1])).grid(column=2, row=item_count + 8)
        Label(mw, text=(store_details[item_count][2])).grid(column=3, row=item_count + 8)
        Label(mw, text=(store_details[item_count][3])).grid(column=4, row=item_count + 8)
        item_count += 1



def append_name():
    global store_details, entry_cname, entry_rnumber, entry_ihired, entry_numhired, total_entries, entries

    # Lists all possible boxes able to be filled and adds it to the rows
    entries = str([entry_cname, entry_rnumber, entry_ihired, entry_numhired])
    store_details.append([entry_cname.get(), entry_rnumber.get(), entry_ihired.get(), entry_numhired.get()])
    entry_cname.delete(0, 'end')
    entry_rnumber.delete(0, 'end')
    entry_ihired.delete(0, 'end')
    entry_numhired.delete(0, 'end')
    total_entries += 1




# delete a row from the list
def delete_row():
    global store_details, delete_item, total_entries, item_count
    del store_details[int(delete_item.get())]
    total_entries = total_entries - 1
    delete_item.delete(0, 'end')
    Label(mw, text="       ").grid(column=0, row=item_count + 7)
    Label(mw, text="       ").grid(column=1, row=item_count + 7)
    Label(mw, text="       ").grid(column=2, row=item_count + 7)
    Label(mw, text="       ").grid(column=3, row=item_count + 7)
    Label(mw, text="       ").grid(column=4, row=item_count + 7)
    print_store_details()


# create the buttons and labels
def setup_buttons():
    global store_details, entry_cname, entry_rnumber, entry_ihired, entry_numhired, total_entries, delete_item, Combobox
    Button(mw, text="Quit", command=quit).grid(column=3, row=1)
    Button(mw, text="Reciept Print", command=items_selected).grid(column=3, row=2)
    Button(mw, text="Append Details", command=append_name).grid(column=0, row=1)
    Button(mw, text="Print Details", command=print_store_details).grid(column=1, row=1)
    Label(mw, text="Name").grid(column=0, row=2)
    entry_cname = Entry(mw)
    entry_cname.grid(column=1, row=2)
    Label(mw, text="Reciept Number").grid(column=0, row=3)
    entry_rnumber = Entry(mw)
    entry_rnumber.grid(column=1, row=3)
    Label(mw, text="Item Hired").grid(column=0, row=4)
    item = StringVar()
    entry_ihired = ttk.Combobox(mw, textvariable = item, state = "readonly", values =("BBQ LED_lights Balloons Party_animals"),width = 17)
    entry_ihired.grid(column=1, row=4)
    Label(mw, text="NO. Hired").grid(column=0, row=5)
    entry_numhired = Entry(mw)
    entry_numhired.grid(column=1, row=5)
    Label(mw, text="Row #").grid(column=0, row=6)
    delete_item = Entry(mw)
    delete_item.grid(column=1, row=6)
    Button(mw, text="Delete", command=delete_row).grid(column=2, row=6)

def items_selected():
    """ handle item selected event
    """
    # get selected items

    msg = f'You selected: '+ (entries)

    showinfo(
        title='Your Reciept',
        message=msg)


# start the program running
def main():
    global mw
    global store_details, total_entries
    store_details = []
    total_entries = 0
    mw = Tk()
    mw.title("Julies Party Hire Store")
    setup_buttons()
    mw.resizable(False, False)
    mw.mainloop()


main()
