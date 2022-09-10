import customtkinter as ctk
import tkinter as tk

# calling the main library file 
from BASE import *


# ctk initilization
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# main splash screen entry point
class Home:

    # all splash screen constructor
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("900x600")
        self.app.title("in-watch")

    def screen1(self):
        pass

    def screen2(self):
        pass

    # splash screen initilizer
    def run(self):
        return self.app.mainloop()