import re
import tkinter as tk
from tkinter import ttk

import floatvalidate
import intvalidate

E = tk.E
W = tk.W
WIDE = 5
HEADER_COLOR = "#c6c6c6"
ROW_COLOR = "#e6e1e1"


class ItemsRow(tk.Frame):
    def __init__(self, parent, total=None, entries=None, index=0, header=False):
        tk.Frame.__init__(self, parent)
        self.index = index
        self.list = entries
        self.totalVar = total

        self.configure_column()

        self.unitVar = tk.StringVar()
        self.unitVar.set(0)
        self.qVar = tk.StringVar()
        self.qVar.set(0)
        self.unitVar.trace_add("write", self.total)
        self.qVar.trace_add("write", self.total)

        if header:
            self.make_header()
        else:
            self.make_item_row()

        self.add_to_grid()

    def configure_column(self):
        for i in range(0, 11):
            self.columnconfigure(i, weight=1)

    def make_header(self):
        self.serial = tk.Entry(self, justify="center", bg=HEADER_COLOR, width=WIDE + 1)
        self.serial.insert(0, "#")
        self.serial.configure(state="disabled")

        self.item = tk.Entry(self, justify="center", bg=HEADER_COLOR)
        self.item.insert(0, "Items")
        self.item.configure(state="disabled")

        self.unit = tk.Entry(self, justify="center", bg=HEADER_COLOR, width=WIDE)
        self.unit.insert(0, "Unit")
        self.unit.configure(state="disabled")

        self.quantity = tk.Entry(self, justify="center", bg=HEADER_COLOR, width=WIDE)
        self.quantity.insert(0, "Quant.")
        self.quantity.configure(state="disabled")

        self.measure = tk.Entry(self, justify="center", bg=HEADER_COLOR, width=WIDE)
        self.measure.insert(0, "Measure")
        self.measure.configure(state="disabled")

        self.total = tk.Entry(self, justify="center", bg=HEADER_COLOR, width=WIDE)
        self.total.insert(0, "Total")
        self.total.configure(state="disabled")

    def make_item_row(self):
        self.serial = tk.Frame(self, width=WIDE + 1, bg=ROW_COLOR)
        self.serial.columnconfigure(0, weight=1)
        self.serial.columnconfigure(1, weight=2)

        self.serial1 = tk.Entry(self.serial, justify="center", bg=ROW_COLOR, width=2)
        self.serial1.insert(0, self.index)
        self.serial1.grid(row=0, column=1, sticky=E + W)
        self.serial1.configure(state="disabled")

        self.button = tk.Button(self.serial, bg=ROW_COLOR, width=2, text="REM", command=self.remove_self)
        self.button.grid(row=0, column=0, sticky=W + E)

        self.item = tk.Entry(self, justify="left", bg=ROW_COLOR)

        self.unit = tk.Entry(self, justify="center", bg=ROW_COLOR, width=WIDE, textvar=self.unitVar)
        # self.unit.insert(0, 0)
        intvalidate.int_validate(self.unit, from_=0, to=999999)

        self.quantity = tk.Entry(self, justify="center", bg=ROW_COLOR, width=WIDE, textvar=self.qVar)
        # self.quantity.insert(0, 0)
        floatvalidate.float_validate(self.quantity, from_=0, to=999999)

        # self.measure = tk.Entry(self, justify="center", bg=ROW_COLOR, width=WIDE)
        self.option_menu = tk.StringVar()
        options = ["mg", "grams", "KG", "Litre", "ml", "Bag", "Drum", "Can", "Gallon", "-", "pack"]
        # self.measure = ttk.OptionMenu(self, self.option_menu, options[2], *options, direction="below")
        self.measure = ttk.Combobox(self, textvariable=self.option_menu)
        self.measure['values'] = options
        self.measure['state'] = "readonly"
        self.measure.configure(width=WIDE-3)
        self.measure.set(options[2])

        self.total = tk.Entry(self, justify="center", bg=ROW_COLOR, width=WIDE)
        self.total.insert(0, 0)
        self.total.configure(state="disabled")

    def add_to_grid(self):
        self.serial.grid(row=0, column=0, sticky=E + W, columnspan=1)
        self.item.grid(row=0, column=1, sticky=E + W, columnspan=6)
        self.unit.grid(row=0, column=7, sticky=E + W, columnspan=1)
        self.quantity.grid(row=0, column=8, sticky=E + W, columnspan=1)
        self.measure.grid(row=0, column=9, sticky=E + W, columnspan=1, padx=0)
        self.total.grid(row=0, column=10, sticky=E + W, columnspan=1)

    def remove_self(self):
        self.grid_forget()
        self.destroy()
        currentIndex = self.list.index(self)
        del self.list[currentIndex]
        for i in range(currentIndex, len(self.list)):
            widget = self.list[i]
            widget.serial1.configure(state="normal")
            widget.serial1.delete(0, tk.END)
            widget.serial1.insert(0, currentIndex + 1)
            widget.serial1.configure(state="disabled")
            currentIndex += 1
        self.calculate_total()

    def total(self, var, index, mode):
        self.total.configure(state="normal")
        self.total.delete(0, tk.END)
        q = self.quantity.get()
        u = self.unit.get()

        if q == "":
            q = 0.0
        if u == "":
            u = 0.0

        q = float(q)
        u = float(u)

        self.total.insert(0, float("{:.2f}".format(q * u)))

        self.total.configure(state="disabled")
        self.calculate_total()

    def calculate_total(self):
        total_sum = 0.0
        for wid in self.list:
            total_sum += float(wid.total.get())
        self.totalVar.set(f'Rs /= {total_sum}')
