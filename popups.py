import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import main


class PopUps(tk.Toplevel):
    def __init__(self, msg, method, **kw):
        super().__init__(**kw)
        self.grab_set()
        self.title("Warning")
        message = tk.Label(self, text=msg)
        message.pack(side='top', fill='x', pady=20, padx=5)

        yesBtn = tk.Button(master=self, text="Yes", width=15, bg=main.CUSTOMER_BG, relief="raised", bd=2,
                           command=lambda: self.remove(method))
        yesBtn.pack(side="right", padx=5, pady=5)

        noBtn = tk.Button(master=self, text="No", bg=main.CUSTOMER_BG,
                          command=self.destroy, width=15)
        noBtn.pack(side="right", padx=5, pady=5)
        self.resizable(width=False, height=False)

    def remove(self, method):
        self.grab_release()
        self.destroy()
        method()


class ConfirmWarning:
    def __init__(self, title, msg):
        showinfo(title, PopUps(msg))
