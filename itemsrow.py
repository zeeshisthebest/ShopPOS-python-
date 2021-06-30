import tkinter as tk

E = tk.E
W = tk.W

HEADER_COLOR = "#c6c6c6"
ROW_COLOR = "#e6e1e1"


class ItemsRow(tk.Frame):
    def __init__(self, parent, values, header=False):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.values = values
        self.configure_column()

        if header:
            self.make_header()
        else:
            self.make_item_row()
            self.put_values()

        self.add_to_grid()

    def configure_column(self):
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=10)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.columnconfigure(4, weight=1)

    def make_header(self):
        self.serial = tk.Label(self, justify="center", bg=HEADER_COLOR, text=self.values[0])
        self.item = tk.Label(self, justify="center", bg=HEADER_COLOR, text=self.values[1])
        self.unit = tk.Label(self, justify="center", bg=HEADER_COLOR, text=self.values[2])
        self.quantity = tk.Label(self, justify="center", bg=HEADER_COLOR, text=self.values[3])
        self.total = tk.Label(self, justify="center", bg=HEADER_COLOR, text=self.values[4])

    def make_item_row(self):
        self.serial = tk.Label(self, justify="center", bg=HEADER_COLOR, text=self.values[0])
        self.item = tk.Entry(self, justify="center", bg=ROW_COLOR)
        self.unit = tk.Entry(self, justify="center", bg=ROW_COLOR)
        self.quantity = tk.Entry(self, justify="center", bg=ROW_COLOR)
        self.total = tk.Entry(self, justify="center", bg=ROW_COLOR)
        self.put_values()

    def add_to_grid(self):
        self.serial.grid(row=0, column=0, sticky=E + W, columnspan=1)
        self.item.grid(row=0, column=1, sticky=E + W, columnspan=1)
        self.unit.grid(row=0, column=2, sticky=E + W, columnspan=1)
        self.quantity.grid(row=0, column=3, sticky=E + W, columnspan=1)
        self.total.grid(row=0, column=4, sticky=E + W, columnspan=1)

    def put_values(self):
        self.item.insert(0, self.values[1])
        self.unit.insert(0, self.values[2])
        self.quantity.insert(0, self.values[3])
        self.total.insert(0, self.values[4])
