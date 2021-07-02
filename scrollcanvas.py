import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, initial, *args, **kwargs):
        super().__init__(container, **kwargs)
        canvas = tk.Canvas(self)
        scroll = ttk.Scrollbar(self, orient='vertical', command=canvas.yview)
        self.frame = ttk.Frame(canvas)
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=3)
        self.frame.columnconfigure(2, weight=1)
        self.frame.columnconfigure(3, weight=1)
        self.frame.columnconfigure(4, weight=1)

        self.frame.grid(columnspan=5, sticky="ew")

        initial.ItemsRow(self.frame, header=False)
        self.frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window(0, 0, anchor='nw', window=self.frame)
        # canvas.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox('all'),
                         yscrollcommand=scroll.set)

        canvas.pack(side="left", fill="both", expand="true")
        scroll.pack(side="right", fill="y")
