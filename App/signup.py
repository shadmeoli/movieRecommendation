# all the imports
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
class SignUp:

    # all splash screen constructor
    def __init__(self):
        self.app = ctk.CTk()
        self.app.geometry("900x600")
        self.app.title("in-watch")

    def user_signup(self):
        pass


    # splash screen initilizer
    def run(self):
        return self.app.mainloop()