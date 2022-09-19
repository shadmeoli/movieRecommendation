# all the imports
import os
import sys
from datetime import datetime
import time
from random import randint

# -- UI libraries
from tkinter import *
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk, simpledialog
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


# pages and custom renders
from login import LogIn
from BASE import *
from Model.database import *

# ctk initilization
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")



# main splash screen entry point
class SignUp:

    # all splash screen constructor
    def __init__(self):
        # super tk.Tk__init__()

        self.WIDTH, self.HEIGHT = 900, 600
        self.app = ctk.CTk()
        self.app.geometry(f"{self.WIDTH}x{self.HEIGHT}")
        self.app.title("in-watch")

        # frame
        self.frame = ctk.CTkFrame(master=self.app,
                                       width=500,
                                       height=400,
                                       corner_radius=10)
        self.frame.pack(padx=20, pady=100)# reset user password

        # screen widget initlizer 
        self.user_signup()


    def reset_password(self):
        name = str(self._user_name.get())
        print("Password reset for: {}".format(name))
        # initilizer
        self.user_signup()

    # redirect to login
    def login_screen(self, redirect=False):
        redirect = True
        return redirect

    # registering the new user
    def user_registration(self):
        
       # reacing from the user form input
        name = str(self.new_user_name.get())
        email = str(self.new_user_email.get())
        phone = str(self.new_user_phone.get())
        password = str(self.new_user_password.get())

        # inserting values to the db database
        # attaching from the database file but validating the mail first
        add_user = DBWrite()
        add_user.adding_users(name, email, phone, password)

        return True

    def user_signup(self):
        
        # getting user data
        __company = ctk.CTkLabel(self.app, text="in-watch", text_font=("helvetica", 60))
        __company.place(x=330, y=10)

        # username
        __name = ctk.CTkLabel(self.frame, text="username")
        __name.place(x=100, y=50)

        self.new_user_name = ctk.CTkEntry(self.frame, placeholder_text="username")
        self.new_user_name.place(x=220, y=50) 

        # getting user data
        # email
        __email = ctk.CTkLabel(self.frame, text="email")
        __email.place(x=100, y=100)

        self.new_user_email = ctk.CTkEntry(self.frame, placeholder_text="email")
        self.new_user_email.place(x=220, y=100) 

        # phone
        __phone = ctk.CTkLabel(self.frame, text="Phone")
        __phone.place(x=100, y=150)

        self.new_user_phone = ctk.CTkEntry(self.frame, placeholder_text="phone number")
        self.new_user_phone.place(x=220, y=150) 

        # password
        __password = ctk.CTkLabel(self.frame, text="password")
        __password.place(x=100, y=200)

        self.new_user_password = ctk.CTkEntry(self.frame, placeholder_text="password", show="*")
        self.new_user_password.place(x=220, y=200) 

        # confirm password
        __confirm = ctk.CTkLabel(self.frame, text="confirm")
        __confirm.place(x=100, y=250)

        self.confirm_password = ctk.CTkEntry(self.frame, placeholder_text="confirm password", show="*")
        self.confirm_password.place(x=220, y=250) 

        register = ctk.CTkButton(self.frame, text="SIGN UP", command=self.user_registration)
        register.place(x=190, y=330)


        # redirect
        member = ctk.CTkLabel(self.app, text="Already a member?")
        member.place(x=self.WIDTH-250, y=self.HEIGHT-50)

        login = ctk.CTkButton(self.app, text="LOG IN", width=10, command=self.login_screen)
        login.place(x=self.WIDTH-100, y=self.HEIGHT-50)


    # splash screen initilizer
    def run(self):
        return self.app.mainloop()

# estup 
if __name__  == "__main__":
    sp = SignUp()
    sp.run()