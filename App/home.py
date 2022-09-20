# all the imports
from ast import Pass
import os
import sys
from datetime import datetime
import time
from random import randint

# -- UI libraries
from tkinter import *
import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
from PIL import Image, ImageTk

# API libraries
from fastapi import *
import httpx
import customtkinter as ctk
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

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

        # container frames for the different pages
        self.pages_frame = ctk.CTkFrame(master=self.app,
                                       width=900,
                                       height=600)
        self.pages_frame.pack(padx=20, pady=100)
    
    # where to display all the movies and 
    def main_screen(self):
        pass

    # all archaived movies
    def archaives(self):
        pass

    # the list of downloaded movies
    def downloads(self):
        pass

    # movies added on the watch
    def waiting_list(self):
        pass

    # splash screen initilizer
    def run(self):
        return self.app.mainloop()