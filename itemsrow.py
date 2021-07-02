import tkinter as tk

E = tk.E
W = tk.W
WIDE = 5
HEADER_COLOR = "#c6c6c6"
ROW_COLOR = "#e6e1e1"


class ItemsRow(tk.Frame):
    def __init__(self, parent, total=None, entries=None, index=0, header=False):
        tk.Frame.__init__(self, parent)
        self.parent = parent
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
        for i in range(0, 10):
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

        self.quantity = tk.Entry(self, justify="center", bg=ROW_COLOR, width=WIDE, textvar=self.qVar)
        # self.quantity.insert(0, 0)

        self.total = tk.Entry(self, justify="center", bg=ROW_COLOR, width=WIDE)
        self.total.insert(0, 0)
        self.total.configure(state="disabled")

    def add_to_grid(self):
        self.serial.grid(row=0, column=0, sticky=E + W, columnspan=1)
        self.item.grid(row=0, column=1, sticky=E + W, columnspan=6)
        self.unit.grid(row=0, column=7, sticky=E + W, columnspan=1)
        self.quantity.grid(row=0, column=8, sticky=E + W, columnspan=1)
        self.total.grid(row=0, column=9, sticky=E + W, columnspan=1)

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

        if q == '':
            q = 0.0
        elif not q.isnumeric():
            self.qVar.set(0)
            q = 0.0
        else:
            q = float(q)
        if u == '':
            u = 0.0
        elif not u.isnumeric():
            self.unitVar.set(0)
            u = 0.0
        else:
            u = float(u)

        self.total.insert(0, q * u)
        self.total.configure(state="disabled")
        self.calculate_total()

    def calculate_total(self):
        total_sum = 0.0
        for wid in self.list:
            total_sum += float(wid.total.get())
        self.totalVar.set(f'Rs /= {total_sum}')
