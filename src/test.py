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

        self.create_widgets()

    def create_widgets(self):
        root_frame = ttk.Frame(self, padding="3 12")
        root_frame.grid(column=0, row=0, sticky=tk.NSEW)
        root_frame.columnconfigure(0, weight=1)
        root_frame.rowconfigure(0, weight=1)

        tab = ttk.Notebook(root_frame)

        tab.grid(column=0, row=0, sticky=tk.NSEW)

        tab.add(self.get_news_frame(), text="News")
        tab.add(self.get_options_frame(), text="Configure")

    def get_news_frame(self):
        frame = ttk.Frame(self)
        frame.grid(column=0, row=0, sticky=tk.NSEW)
        frame.columnconfigure(0, weight=2)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)

        main_frame = ttk.Frame(frame, padding="12", style="red.TFrame")
        main_frame.grid(column=0, row=0, sticky=tk.NSEW)

        side_frame = ttk.Frame(frame, padding="12", style="yellow.TFrame")
        side_frame.grid(column=1, row=0, sticky=tk.NSEW)

        ttk.Label(main_frame, text="Blog").grid(column=0, row=0, sticky=tk.W)
        ttk.Label(side_frame, text="Side").grid(column=0, row=0, sticky=tk.W)

        return frame

    def get_options_frame(self):
        frame = ttk.Frame(self)
        frame.grid(column=0, row=0, sticky=tk.NSEW)
        frame.columnconfigure(0, weight=2)
        frame.rowconfigure(0, weight=1)

        opt_frm = ttk.Frame(frame, padding="3 12", style="yellow.TFrame")
        opt_frm.grid(column=0, row=0, sticky=tk.NSEW)

        ttk.Label(opt_frm, text="Options").grid(column=0, row=0, sticky=tk.W)

        return frame


app = App()
app.mainloop()
