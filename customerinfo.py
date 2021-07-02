import tkinter as tk
from tkinter import *
from datetime import date

CUSTOMER_TITLE = "Customer Name: "
PHONE_TITLE = "Enter the Number:"
CUSTOMER_BG = "#c6c6c6"


class CustomerInfo(tk.Frame):
    def __init__(self, parent, **kw):
        super().__init__(master=parent)

        # To show the voice number
        invoiceLabel = tk.Label(master=self, text="INVOICE # ", width=len("INVOICE # ") + 1)
        invoiceLabel.grid(row=1, column=0)

        invoiceEntry = tk.Entry(master=self, justify='center')
        invoiceEntry.grid(row=1, column=1)
        invoiceEntry.insert(0, kw['INVOICE'])
        invoiceEntry['state'] = "disabled"

        # To show the date
        dateLabel = tk.Label(master=self, text=f"Date: {kw['DATE']}")
        dateLabel.grid(row=1, column=2, padx=200)

        # Padding after invoice number
        padding_label2 = tk.Label(master=self).grid(row=2)

        # Customer name views
        customerLabel = tk.Label(master=self, text=CUSTOMER_TITLE, bg=CUSTOMER_BG
                                 , width=len(CUSTOMER_TITLE) + 2)
        customerLabel.grid(row=3, padx=10, sticky=E)

        self.customerEntry = Entry(master=self, width=40)
        self.customerEntry.grid(row=3, column=1)
        self.customerEntry.insert(0, "unknown")

        # Phone number max length restriction
        self.codeVar = tk.StringVar()
        self.extensionVar = tk.StringVar()
        self.codeVar.set("03xx")
        self.extensionVar.set("xxxxxxx")

        # binding the text variable for tracing
        self.codeVar.trace_variable("w", self.on_code_write)
        self.extensionVar.trace_variable("w", self.on_extension_write)

        # Phone number Views
        phoneLabel = tk.Label(master=self, text=PHONE_TITLE, bg=CUSTOMER_BG, width=len(CUSTOMER_TITLE) + 2)
        phoneLabel.grid(row=4, padx=10)
        # Frame to hold code and extension
        phoneFrame = tk.Frame(self)
        phoneFrame.grid(row=4, column=1, sticky="W", columnspan=5)
        # Code
        self.phoneEntryCode = Entry(master=phoneFrame, width=7, textvariable=self.codeVar, justify="right")
        self.phoneEntryCode.grid(row=0, column=0)
        self.on_code_click_id = self.phoneEntryCode.bind('<Button-1>', self.on_code_click)

        separatorLabel = tk.Label(master=phoneFrame, width=4, justify='center', text='-')
        separatorLabel.grid(row=0, column=1)

        # Extension
        self.phoneEntryExtension = Entry(master=phoneFrame, width=14, textvariable=self.extensionVar)
        self.phoneEntryExtension.grid(row=0, column=2)
        self.on_ext_click_id = self.phoneEntryExtension.bind('<Button-1>', self.on_ext_click)

    def on_code_write(self, *args):
        code = self.codeVar.get()
        code_string = ""

        for num in code:
            if code != "" and num.isnumeric():
                code_string += num;
            elif code != "" and not num.isnumeric():
                self.codeVar.set(code)
                break

        if len(code_string) > 4:
            code_string = code_string[:4]

        self.codeVar.set(code_string)

    def on_extension_write(self, *args):
        ext = self.extensionVar.get()
        extension_string = ""

        for num in ext:
            if ext != "" and num.isnumeric():
                extension_string += num;
            elif ext != "" and not num.isnumeric():
                self.extensionVar.set(ext)
                break

        if len(extension_string) > 7:
            extension_string = extension_string[:7]

        self.extensionVar.set(extension_string)

    def on_code_click(self, e):
        self.phoneEntryCode.delete(0, END)
        self.phoneEntryCode.unbind('<Button-1>', self.on_code_click_id)

    def on_ext_click(self, e):
        self.phoneEntryExtension.delete(0, END)
        self.phoneEntryExtension.unbind('<Button-1>', self.on_ext_click_id)

    def get_customer_info(self):
        info = {
            "name": self.customerEntry.get(),
            "cell": f'{self.phoneEntryCode.get()}-{self.phoneEntryExtension}'
        }

        return info


