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

# database library
from Model import *
from Mode.database import *
from Model.API import * 

# custom hex colours
_theme = {
    "custom_background" : "#010922" ,
    "custom_widget_colour" :"#8080D7",
    "custom_accents" : "#AAD9D9"
}