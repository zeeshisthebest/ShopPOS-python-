import tkinter.filedialog as fd
from datetime import date

import generatereceipt as gr
import tkinter as tk
from tkinter.messagebox import showinfo, showerror


class SaveFile(tk.Toplevel):
    def __init__(self, dictionary, pdf=False, **kw):
        super().__init__(**kw)
        self.grab_set()
        self.dictionary = dictionary
        self.pdf = pdf
        self.title("Select Location")
        self.path = ""

        tk.Label(self, text="Please select the location where you want to save the file",
                 justify='center').grid(row=0, columnspan=2, sticky="we")

        self.pathEntry = tk.Entry(self, text="", width=100)
        self.pathEntry.grid(row=1, padx=5, pady=10, column=0, sticky='we')

        tk.Button(self, text="Choose Location", command=self.get_path).grid(row=1, padx=10, pady=10, column=1)
        tk.Button(self, text="Save Invoice", command=self.save_file) \
            .grid(row=2, padx=10, pady=10, columnspan=2)

        self.resizable(width=False, height=False)

    def get_path(self):
        self.path = fd.askdirectory()
        if self.path is None:
            return
        self.pathEntry.delete(0, tk.END)
        self.pathEntry.insert(0, f"{self.path}/Invoice {self.dictionary['invoice']} {date.today()}.xlsx")

    def save_file(self):
        if self.pathEntry.get() == "":
            showinfo("Error", "Couldn't save file: No path selected")
            return

        receipt = gr.GenerateReceipt(self.dictionary['invoice'], self.pathEntry.get())
        receipt.set_customer_name(self.dictionary['name'], self.dictionary['cell'])
        receipt.print_list(self.dictionary)
        receipt.print_the_total(self.dictionary['grand_total'])
        try:
            receipt.save_excel()
            if self.pdf:
                receipt.print_to_pdf()
            self.destroy()
            showinfo("Saved", "Invoice saved successfully")
        except Exception:
            showinfo("Error", "Couldn't save invoice please try again")


class Success:
    def __init__(self, title, msg):
        showinfo(title, msg)


class ShowWarning:
    def __init__(self, msg):
        showerror(self, msg)
