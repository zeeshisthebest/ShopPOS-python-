import tkinter as tk
from tkinter import *
from datetime import date
from customerinfo import CustomerInfo as ci
import itemsrow
import popups
import scrollcanvas
from itemsrow import ItemsRow as iT

CUSTOMER_BG = "#c6c6c6"


def root():
    def add_row(frame, total):
        rows = len(all_entries) + 1
        itemRowFrame = iT(frame, entries=all_entries, index=rows, header=False, total=total)
        itemRowFrame.grid(columnspan=5, sticky=W + E)
        all_entries.append(itemRowFrame)

    def warning_popup(msg):
        popups.PopUps(msg, rem_all)

    def rem_all():
        while all_entries:
            all_entries[0].grid_remove()
            all_entries[0].destroy()
            del all_entries[0]
        add_row(itemFrame, totalVar)

    APP_NAME = "Customer Invoicing - Saleem Chemicals"
    INVOICE = "00000"
    DATE = date.today()
    all_entries = []

    ui_root = tk.Tk()
    ui_root.title(APP_NAME)
    ui_root.columnconfigure(0, weight=1)

    totalVar = tk.StringVar()

    # These two lines add the padding
    padding_label = tk.Label(master=ui_root, text=" ")
    padding_label.grid(row=0)

    # INFORMATION FRAME ---------------------------------------------------------------------------
    customer = ci(parent=ui_root, DATE=DATE, INVOICE=INVOICE)
    customer.grid()
    # INFORMATION END ----------------------------------------------------------------------------
    tk.Label(master=ui_root).grid(row=5, sticky=E + W)  # An empty Row
    # Item's List Holder--------------------------------------------------------------------------
    # Header row for the items
    header_row = iT(ui_root, header=True)
    header_row.grid(row=6, columnspan=5, sticky=W + E, padx=10)

    itemFrame = tk.Frame(ui_root)
    itemFrame.grid(row=7, columnspan=5, column=0, sticky=W + E + N + S, padx=10)

    itemFrame.columnconfigure(0, weight=1)
    itemFrame.columnconfigure(1, weight=3)
    itemFrame.columnconfigure(2, weight=1)
    itemFrame.columnconfigure(3, weight=1)
    itemFrame.columnconfigure(4, weight=1)

    for i in range(0, 5):
        add_row(itemFrame, total=totalVar)

    # ITEM FRAMES END ------------------------------------------------------------------------------------

    # After items frames
    totalFrame = tk.Frame(master=ui_root)
    totalFrame.grid(sticky=E + W)
    totalFrame.columnconfigure(0, weight=1)
    totalFrame.columnconfigure(1, weight=1)

    # Total Row
    totalLabel = tk.Label(master=totalFrame, font=('bold', 15), text="TOTAL. ")
    totalLabel.grid(row=0, columnspan=1, column=1)

    totalVar.set("Rs /= 0.0")
    totalSum = tk.Label(master=totalFrame, textvar=totalVar, font=15, anchor=E, width=15)
    totalSum.grid(row=0, columnspan=1, column=1, padx=20, sticky=E)

    # Button to remove all and add the new rows
    rmBtn = Button(totalFrame, text="Remove All Items", command=lambda: warning_popup("Are you sure you want to "
                                                                                      "remove all the items?"))
    rmBtn.grid(row=1, column=0, sticky=E, padx=5)

    addBtn = Button(totalFrame, text="Add New Item", command=lambda: add_row(itemFrame, totalVar))
    addBtn.grid(row=1, column=1, sticky=W, padx=5)
    # TOTAL FRAME ENDS --------------------------------------------------------------------------------

    tk.Label(master=ui_root).grid()

    def check(e):
        WIDTH = ui_root.winfo_width()
        HEIGHT = ui_root.winfo_height() + 10
        ui_root.minsize(WIDTH, HEIGHT)
        ui_root.unbind("<Configure>", ui_bind)

    ui_bind = ui_root.bind("<Configure>", check)
    ui_root.mainloop()


def main():
    root()


if __name__ == '__main__':
    main()
