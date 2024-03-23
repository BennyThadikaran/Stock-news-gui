import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    def __init__(self) -> None:
        super().__init__()

        self.title = "News"
        self.attributes("-zoomed", True)
        self.grid_columnconfigure(0, weight=2)

        s = ttk.Style()
        s.configure("red.TFrame", background="red")
        s.configure("yellow.TFrame", background="yellow")

        main_frm = ttk.Frame(self, padding="3 12")
        main_frm.grid(column=0, row=0, sticky=tk.NSEW)
        main_frm.columnconfigure(0, weight=2)
        main_frm.columnconfigure(1, weight=1)

        blog_frm = ttk.Frame(main_frm, padding="3 12", style="red.TFrame")
        blog_frm.grid(column=0, row=0, sticky=tk.NSEW)

        side_frm = ttk.Frame(main_frm, padding="3 12", style="yellow.TFrame")
        side_frm.grid(column=1, row=0, sticky=tk.NSEW)

        ttk.Label(blog_frm, text="Blog").grid(column=0, row=0, sticky=tk.W)
        ttk.Label(side_frm, text="Side").grid(column=0, row=0, sticky=tk.W)


app = App()
app.mainloop()
