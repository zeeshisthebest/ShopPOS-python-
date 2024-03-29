import tkinter as tk
from tkinter import *
from datetime import date
from customerinfo import CustomerInfo as ci
import popups
from itemsrow import ItemsRow as iT
import savefile as sf

CUSTOMER_BG = "#c6c6c6"
PAD_HOR = 5


def root():
    def reset_all():
        ui_root.destroy()
        main()

    def add_row(frame, total):
        rows = len(all_entries) + 1
        itemRowFrame = iT(frame, entries=all_entries, index=rows, header=False, total=total)
        itemRowFrame.grid(columnspan=5, sticky=W + E)
        all_entries.append(itemRowFrame)

    def warning_popup(msg, method):
        popups.PopUps(msg, method=method)

    def rem_all():
        while all_entries:
            all_entries[0].grid_remove()
            all_entries[0].destroy()
            del all_entries[0]
        add_row(itemFrame, totalVar)

    def save_file(btnType):
         # data_dict['invoice'] = invoice  # stores the invoice number

        info = customer.get_info()  # Get Name and Number
        if not info:
            popups.showinfo(message="Phone number is not correct!!")
            return False  # Stopping the file from saving

        data_dict.update(info)

        for index, each_row in enumerate(all_entries):
            print(each_row.total.get())
            tot = float(each_row.total.get())
            print(tot != 0, tot != 0.0)
            if tot != 0 or tot != 0.0:
                data_dict[index] = {
                    "serial": float(each_row.serial1.get()),
                    "item": each_row.item.get(),
                    "unit": float(each_row.unit.get()),
                    "quantity": float(each_row.quantity.get()),
                    "measure": each_row.option_menu.get(),
                    "total": each_row.total.get()
                }
        print(len(data_dict))
        data_dict['grand_total'] = totalVar.get()
        sf.SaveFile(dictionary=data_dict, pdf=btnType)

    APP_NAME = "Customer Invoicing - Saleem Chemicals"
    # INVOICE = "00000"
    DATE = date.today()
    all_entries = []
    data_dict = dict()

    ui_root = tk.Tk()
    ui_root.title(APP_NAME)
    ui_root.columnconfigure(0, weight=1)

    totalVar = tk.StringVar()

    # These two lines add the padding
    padding_label = tk.Label(master=ui_root, text=" ")
    padding_label.grid(row=0)

    # INFORMATION FRAME ---------------------------------------------------------------------------
    # customer = ci(parent=ui_root, DATE=DATE, INVOICE=INVOICE)
    customer = ci(parent=ui_root, DATE=DATE)
    customer.grid(padx=PAD_HOR, sticky=E + W)
    # INFORMATION END ----------------------------------------------------------------------------

    tk.Label(master=ui_root).grid(row=5, sticky=E + W)  # An empty Row

    # Item's List Holder--------------------------------------------------------------------------
    # Header row for the items
    header_row = iT(ui_root, header=True)
    header_row.grid(row=6, columnspan=5, sticky=W + E, padx=PAD_HOR)

    itemFrame = tk.Frame(ui_root)
    itemFrame.grid(row=7, columnspan=5, column=0, sticky=W + E + N + S, padx=PAD_HOR)

    itemFrame.columnconfigure(0, weight=1)
    itemFrame.columnconfigure(1, weight=3)
    itemFrame.columnconfigure(2, weight=1)
    itemFrame.columnconfigure(3, weight=1)
    itemFrame.columnconfigure(4, weight=1)

    # scrollar = scrollcanvas.ScrollableFrame(itemFrame, itemsrow)
    # canvas_scroll_region = scrollar.frame #Getting the region inside canvas where i have to place rows
    # add_row(canvas_scroll_region)  #this is the function that add new row upon the button click

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
                                                                                      "remove all the items?", rem_all))
    rmBtn.grid(row=1, column=0, sticky=E, padx=5)

    addBtn = Button(totalFrame, text="Add New Item", command=lambda: add_row(itemFrame, totalVar))
    addBtn.grid(row=1, column=1, sticky=W, padx=5)
    # TOTAL FRAME ENDS --------------------------------------------------------------------------------

    # SAVING BUTTONS FRAME ----------------------------------------------------------------------------
    buttonFrame = tk.Frame(master=ui_root)
    buttonFrame.grid(sticky=E + W)

    saveExcelBtn = tk.Button(master=buttonFrame, text="Save in Excel", command=lambda: save_file(False))
    saveExcelBtn.pack(side="right", padx=PAD_HOR, pady=5)

    savePdfBtn = tk.Button(master=buttonFrame, text="Save in PDF/Print", command=lambda: save_file(True))
    savePdfBtn.pack(side="right", padx=PAD_HOR, pady=5)

    # Exit Button
    tk.Button(master=buttonFrame, text="EXIT",
              command=lambda: warning_popup("Do you really want to exit?", ui_root.destroy)) \
        .pack(side='left', padx=PAD_HOR, pady=5, anchor='center')
    tk.Button(master=buttonFrame, text='Reset All', command=lambda: warning_popup("Reset all?", reset_all)) \
        .pack(side='left', padx=PAD_HOR, pady=5, anchor='center')

    # SAVING BUTTONS FRAME END ------------------------------------------------------------------------

    # tk.Label(master=ui_root).grid()

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
