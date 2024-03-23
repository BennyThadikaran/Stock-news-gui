import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title = "News"
        self.attributes("-zoomed", True)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        s = ttk.Style()
        s.configure("red.TFrame", background="red")
        s.configure("yellow.TFrame", background="yellow")

        root_frm = ttk.Frame(self, padding="3 12")
        root_frm.grid(column=0, row=0, sticky=tk.NSEW)
        root_frm.columnconfigure(0, weight=1)
        root_frm.rowconfigure(0, weight=1)

        tab1_frm = ttk.Frame(self)
        tab1_frm.grid(column=0, row=0, sticky=tk.NSEW)
        tab1_frm.columnconfigure(0, weight=2)
        tab1_frm.columnconfigure(1, weight=1)
        tab1_frm.rowconfigure(0, weight=1)

        tab2_frm = ttk.Frame(self)
        tab2_frm.grid(column=0, row=0, sticky=tk.NSEW)
        tab2_frm.columnconfigure(0, weight=2)
        tab2_frm.rowconfigure(0, weight=1)

        tab = ttk.Notebook(root_frm)

        tab.grid(column=0, row=0, sticky=tk.NSEW)

        blog_frm = ttk.Frame(tab1_frm, padding="12", style="red.TFrame")
        blog_frm.grid(column=0, row=0, sticky=tk.NSEW)

        side_frm = ttk.Frame(tab1_frm, padding="12", style="yellow.TFrame")
        side_frm.grid(column=1, row=0, sticky=tk.NSEW)

        opt_frm = ttk.Frame(tab2_frm, padding="3 12", style="yellow.TFrame")
        opt_frm.grid(column=0, row=0, sticky=tk.NSEW)

        ttk.Label(blog_frm, text="Blog").grid(column=0, row=0, sticky=tk.W)
        ttk.Label(side_frm, text="Side").grid(column=0, row=0, sticky=tk.W)
        ttk.Label(opt_frm, text="Options").grid(column=0, row=0, sticky=tk.W)

        tab.add(tab1_frm, text="Main")
        tab.add(tab2_frm, text="Configure")


app = App()
app.mainloop()
