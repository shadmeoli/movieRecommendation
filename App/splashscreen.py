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

# calling the main library file 
from .BASE import *


# ctk initilization
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


# main splash screen
class SplashScreen:

    # all splash screen constructor
    def __init__(self):

        self.screen = 1

        self.app = ctk.CTk()
        self.app.geometry("900x600")
        self.app.title("in-watch")

        # splash image
        self.photo_1 = Image.open("/home/shad/Desktop/Binar Projects/movieRecommendation/assets/renders/Other 12.png")
        self.photo_2 = Image.open("/home/shad/Desktop/Binar Projects/movieRecommendation/assets/renders/Other 18.png") 

        self.change()
    
    def registering_new_user(self):
        print("Now in home")

    # changing screens
    def change(self):

        __first_screen = self.screen1()
        try:
            if self.screen == 1:
                self.screen += 1
                
                __first_screen
                self.photo_1 = self.photo_2
                
                
            elif self.screen == 2:
                self.screen += 1
                self.screen2()
                
        except EOFError as e:
            print(e)
            

    # image rendering
    def image(self):
        __splash = ctk.CTkLabel(self.app, image=self.render_photo)
        __splash.place(x=230, y=5)
        
        return __splash
    
    # second image
    def second_image(self):

        __splash = ctk.CTkLabel(self.app, image=self.second_render_photo)
        __splash.place(x=250, y=5)

        return __splash

    # the first screen
    def screen1(self):

        self.render_photo = ImageTk.PhotoImage(self.photo_1)

        __image = self.image()
        __image

        __movies = ctk.CTkLabel(self.app, text="A great range of movies.")
        __movies.place(x=300, y=480)

        __next=  ctk.CTkButton(text='NEXT', hover=True, command=self.change)
        __next.place(x=750, y=550)

        return __movies

    # the second screen
    def screen2(self):
        self.second_render_photo = ImageTk.PhotoImage(self.photo_2)
        __image = self.second_image()
        __image

        __movies = ctk.CTkLabel(self.app, text="Fast download and watch speed.")
        __movies.place(x=300, y=480)

        __next=  ctk.CTkButton(text='Create Account', command=self.registering_new_user)
        __next.place(x=750, y=550)

        return __movies

    # splash screen initilizer
    def run(self):
        return self.app.mainloop()


