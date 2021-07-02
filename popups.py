import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


# class PopUps(tk.Tk):
#     def __init__(self, parent, message):
#         super().__init__()
#         self.wm_title("Warning!")
#         msg = tk.Label(self, text=message)
#         msg.pack(side='top', fill='x', pady=15, padx=20)
#         self.grid()
#         self.mainloop()
import main


class PopUps(tk.Toplevel):
    def __init__(self, msg, method, **kw):
        super().__init__(**kw)
        self.grab_set()
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
        method()
        self.grab_release()
        self.destroy()


class ConfirmWarning:
    def __init__(self, title, msg):
        showinfo(title, PopUps(msg))
