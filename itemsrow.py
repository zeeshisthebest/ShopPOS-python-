import tkinter as tk

E = tk.E
W = tk.W
WIDE = 5
HEADER_COLOR = "#c6c6c6"
ROW_COLOR = "#e6e1e1"


class ItemsRow(tk.Frame):
    def __init__(self, parent, entries=None, index=0, header=False):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.index = index
        self.configure_column()
        self.list = entries

        if header:
            self.make_header()
        else:
            self.make_item_row()

        self.add_to_grid()

    def configure_column(self):
        for i in range(0, 10):
            self.columnconfigure(i, weight=1)

    def make_header(self):
        self.serial = tk.Entry(self, justify="center", bg=HEADER_COLOR, width=WIDE+1)
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

        self.total = tk.Entry(self, justify="center", bg=HEADER_COLOR, width=WIDE)
        self.total.insert(0, "Total")
        self.total.configure(state="disabled")

    def make_item_row(self):
        self.serial = tk.Frame(self, width=WIDE+1, bg=ROW_COLOR)
        self.serial.columnconfigure(0, weight=1)
        self.serial.columnconfigure(1, weight=2)

        self.serial1 = tk.Entry(self.serial, justify="center", bg=ROW_COLOR, width=2)
        self.serial1.insert(0, self.index)
        self.serial1.grid(row=0, column=1, sticky=E+W)
        self.serial1.configure(state="disabled")

        self.button = tk.Button(self.serial, bg=ROW_COLOR, width=2, text="REM", command=self.remove_self)
        self.button.grid(row=0, column=0, sticky=W+E)

        self.item = tk.Entry(self, justify="left", bg=ROW_COLOR)

        self.unit = tk.Entry(self, justify="center", bg=ROW_COLOR, width=WIDE)

        self.quantity = tk.Entry(self, justify="center", bg=ROW_COLOR, width=WIDE)

        self.total = tk.Entry(self, justify="center", bg=ROW_COLOR, width=WIDE)

    def add_to_grid(self):
        self.serial.grid(row=0, column=0, sticky=E + W, columnspan=1)
        self.item.grid(row=0, column=1, sticky=E + W, columnspan=6)
        self.unit.grid(row=0, column=7, sticky=E + W, columnspan=1)
        self.quantity.grid(row=0, column=8, sticky=E + W, columnspan=1)
        self.total.grid(row=0, column=9, sticky=E + W, columnspan=1)

    def remove_self(self):
        self.pack_forget()
        self.destroy()
        del self.list[self.index-1]
