
# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk
import tkinter as tk


from build.gui2 import show_page_menu


def start():
    window = Tk()
    window.geometry("600x400")
    window.configure(bg = "#FFFFFF")
    window.title("Stegano Application")

    main_frame = tk.Frame(window)

    page_hide_frame = tk.Frame(main_frame)

    show_page_menu(window, main_frame)

    page_hide_frame.pack(pady=20)

    main_frame.pack(fill=tk.BOTH, expand=True)

    window.resizable(False, False)
    window.mainloop()