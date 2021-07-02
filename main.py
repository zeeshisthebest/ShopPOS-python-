import tkinter as tk
from tkinter import *
from datetime import date

import itemsrow
import popups
import scrollcanvas
from itemsrow import ItemsRow as iT

CUSTOMER_BG = "#c6c6c6"


def root():
    def on_code_write(*args):
        code = codeVar.get()
        if len(code) > 4:
            codeVar.set(code[:4])

    def on_extension_write(*args):
        ext = extensionVar.get()
        if len(ext) > 7:
            extensionVar.set(ext[:7])

    def on_code_click(e):
        phoneEntryCode.delete(0, END)
        phoneEntryCode.unbind('<Button-1>', on_code_click_id)

    def on_ext_click(e):
        phoneEntryExtension.delete(0, END)
        phoneEntryExtension.unbind('<Button-1>', on_ext_click_id)

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
    CUSTOMER_TITLE = "Customer Name: "
    PHONE_TITLE = "Enter the Number:"
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
    informationFrame = tk.Frame(ui_root)
    informationFrame.grid()

    # To show the voice number
    invoiceLabel = tk.Label(master=informationFrame, text="INVOICE # ", width=len("INVOICE # ") + 1)
    invoiceLabel.grid(row=1, column=0)

    invoiceEntry = Entry(master=informationFrame, justify='center')
    invoiceEntry.grid(row=1, column=1)
    invoiceEntry.insert(0, INVOICE)
    invoiceEntry['state'] = "disabled"

    # To show the date
    dateLabel = tk.Label(master=informationFrame, text=f"Date: {DATE}")
    dateLabel.grid(row=1, column=2, padx=200)

    # Padding after invoice number
    padding_label2 = tk.Label(master=informationFrame).grid(row=2)

    # Customer name views
    customerLabel = tk.Label(master=informationFrame, text=CUSTOMER_TITLE, bg=CUSTOMER_BG
                             , width=len(CUSTOMER_TITLE) + 2)
    customerLabel.grid(row=3, padx=10, sticky=E)

    customerEntry = Entry(master=informationFrame, width=40)
    customerEntry.grid(row=3, column=1)
    customerEntry.insert(0, "unknown")

    # Phone number max length restriction
    codeVar = tk.StringVar()
    extensionVar = tk.StringVar()
    codeVar.set("03xx")
    extensionVar.set("xxxxxxx")

    # binding the text variable for tracing
    codeVar.trace_variable("w", on_code_write)
    extensionVar.trace_variable("w", on_extension_write)

    # Phone number Views
    phoneLabel = tk.Label(master=informationFrame, text=PHONE_TITLE, bg=CUSTOMER_BG, width=len(CUSTOMER_TITLE) + 2)
    phoneLabel.grid(row=4, padx=10)

    # Frame to hold code and extension
    phoneFrame = tk.Frame(informationFrame)
    phoneFrame.grid(row=4, column=1, sticky="W", columnspan=5)

    # Code
    phoneEntryCode = Entry(master=phoneFrame, width=7, textvariable=codeVar, justify="right")
    phoneEntryCode.grid(row=0, column=0)
    on_code_click_id = phoneEntryCode.bind('<Button-1>', on_code_click)

    separatorLabel = tk.Label(master=phoneFrame, width=4, justify='center', text='-')
    separatorLabel.grid(row=0, column=1)

    # Extension
    phoneEntryExtension = Entry(master=phoneFrame, width=14, textvariable=extensionVar)
    phoneEntryExtension.grid(row=0, column=2)
    on_ext_click_id = phoneEntryExtension.bind('<Button-1>', on_ext_click)
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

    for i in range(0,5):
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
