import tkinter as tk
E = tk.E
W = tk.W

class ItemsRow:
    def __init__(self, parent, values, state="enabled", color=""):
        self.parent = parent
        self.frame = tk.Frame(parent)
        self.configure_column()
        self.serial = tk.Entry(self.frame, justify="center", bg=color, text=values[0])
        self.item = tk.Entry(self.frame, justify="center", text=values[1])
        self.unit = tk.Entry(self.frame, justify="center", bg=color, text=values[2])
        self.quantity = tk.Entry(self.frame, justify="center", text=values[3])
        self.total = tk.Entry(self.frame, justify="center", bg=color, text=values[4])

    def configure_column(self):
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=3)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)
        self.frame.columnconfigure(5, weight=1)

    def add_to_grid(self):
        self.serial.grid(row=0, column=0, sticky=E + W, columnspan=1)
        self.item.grid(row=0, column=1, sticky=E + W, columnspan=1)
        self.unit.grid(row=0, column=2, sticky=E + W, columnspan=1)
        self.quantity.grid(row=0, column=3, sticky=E + W, columnspan=1)
        self.total.grid(row=0, column=4, sticky=E + W, columnspan=1)
