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


# other pages
from Model.database import UserDetails

# ctk initilization
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")


# main splash screen entry point
class LogIn:

    # all splash screen constructor
    def __init__(self):

        self.WIDTH, self.HEIGHT = 900, 600
        self.app = ctk.CTk()
        self.app.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.app.title("in-watch")

        # frame

        self.frame = ctk.CTkFrame(master=self.app,
                                       width=500,
                                       height=400,
                                       corner_radius=10)
        self.frame.pack(padx=20, pady=100)
        # initilizer
        self.user_login()


# reset user password
    def reset_password(self):
        name = str(_user_name.get())
        print("Password reset for: {}".format(name))

    # registering the new user
    def _login(self):

        use_det = UserDetails()
        name = self.user_name.get()
        password = self.user_password.get()
        user_present = use_det.in_database(name, password) #the user name can also be an email address and the background checks are made from the database

        return user_present

    def user_login(self):
        
        # getting user data
        __company = ctk.CTkLabel(self.app, text="in-watch", text_font=("tahoma", 60))
        __company.place(x=330, y=10)

        # username
        __name = ctk.CTkLabel(self.frame, text="username / mail")
        __name.place(x=80, y=100)

        self.user_name = ctk.CTkEntry(self.frame, placeholder_text="username / mail")
        self.user_name.place(x=220, y=100) 

        # password
        __password = ctk.CTkLabel(self.frame, text="password")
        __password.place(x=100, y=150)

        self.user_password = ctk.CTkEntry(self.frame, show="*", placeholder_text="password")
        self.user_password.place(x=220, y=150) 

        register = ctk.CTkButton(self.frame, text="LOG IN", command=self._login)
        register.place(x=190, y=220)


    # splash screen initilizer
    def run(self):
        return self.app.mainloop()