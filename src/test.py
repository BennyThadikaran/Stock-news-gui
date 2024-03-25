import tkinter as tk
from tkinter import ttk


class App(tk.Tk):
    """Class to render the GUI window"""

    def __init__(self) -> None:
        super().__init__()

        self.title = "Stock News"

        # Maximize window at start
        self.attributes("-zoomed", True)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Temporary background colors for checking grid sizing
        s = ttk.Style()
        s.configure("red.TFrame", background="#AFEEEE")
        s.configure("yellow.TFrame", background="#FFFD74")

        self.create_widgets()

    def create_widgets(self) -> None:
        # Wrapper frame for all widgets
        root_frame = ttk.Frame(self, padding="3 12")
        root_frame.grid(column=0, row=0, sticky=tk.NSEW)
        root_frame.columnconfigure(0, weight=1)
        root_frame.rowconfigure(0, weight=1)

        # Notebook widget with 2 tabs in the root frame
        tab = ttk.Notebook(root_frame)
        tab.grid(column=0, row=0, sticky=tk.NSEW)

        tab.add(self.get_news_frame(), text="News")
        tab.add(self.get_options_frame(), text="Configure")

    def get_news_frame(self) -> ttk.Frame:
        """
        News frame is divided into 2 sections - main and side
        Main displays all stock announcements
        Side displays board meetings and corporate actions
        """

        frame = ttk.Frame(self)
        frame.grid(column=0, row=0, sticky=tk.NSEW)

        # It has 2 columns and 1 row
        frame.columnconfigure(0, weight=2)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)

        main_frame = ttk.Frame(frame, padding="12", style="red.TFrame")
        main_frame.grid(column=0, row=0, sticky=tk.NSEW)

        side_frame = ttk.Frame(frame, padding="12", style="yellow.TFrame")
        side_frame.grid(column=1, row=0, sticky=tk.NSEW)

        ttk.Label(main_frame, text="Main").grid(column=0, row=0, sticky=tk.E)
        ttk.Label(side_frame, text="Side").grid(column=0, row=0, sticky=tk.E)

        return frame

    def get_options_frame(self) -> ttk.Frame:
        """Options frame holds all application configuration"""

        frame = ttk.Frame(self)
        frame.grid(column=0, row=0, sticky=tk.NSEW)
        frame.columnconfigure(0, weight=2)
        frame.rowconfigure(0, weight=1)

        opt_frame = ttk.Frame(frame, padding="3 12", style="yellow.TFrame")
        opt_frame.grid(column=0, row=0, sticky=tk.NSEW)

        ttk.Label(opt_frame, text="Options").grid(column=0, row=0, sticky=tk.W)

        return frame


if __name__ == "__main__":
    app = App()
    app.mainloop()
