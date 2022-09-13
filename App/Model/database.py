
import base64
import os
import time
import sqlite3
import json
import random
from datetime import datetime
import asyncio
from functools import cache, lru_cache, reduce, _make_key
import hashlib
from cryptography.fernet import Fernet

from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, TextColumn
import typer 

console = Console()
app = typer.Typer()

# excrypting the passwords and any sensitive data
def crypt_detail(det) -> str:

    encoded_pswd = hashlib.sha265()
    encoded_pswd.update(det.encode())

    return encoded_pswd.hexdigest()

# mail validator
def mail_validation(email: str):

    # currently valid mails
    mails = [
        "@gmail.com",
        "@zohomail.com",
        "@yahoo.com",
        "@protonmail.com"
    ]

    for mail in mails:
        
        mail_provider = email.endswith(mail)

        try:

            if mail_provider not in mails:
                return False
            elif mail_provider in mails and len(email) > 5:
                return True

            elif len(email) == 0:
                return None

        except:
            return None

# creating the database
class Database:

    # creating new files
    def create_new_files(self):
        
        def archive():
            
            con = sqlite3.connect("Model/archaive.db")

            con.execute("""
                CREATE TABLE Download_list(
                    id INTEGER PRIMARY KEY,
                    Movie_name VACHAR(500),
                    Genre VARCHAR(500),
                    Release_date DATETIME)
            """)
            try:
                return con
            except EEXIST:
                console.print("Database already exist", style="bold red")
        
        def downloads():
            
            con = sqlite3.connect("Model/downloads.db")

            con.execute("""
                CREATE TABLE Download_list(
                    id INTEGER PRIMARY KEY,
                    Movie_name VACHAR(500),
                    Genre VARCHAR(500),
                    Release_date DATETIME   
                )
            """)
            return con
        
        def watch_list():
            
            con = sqlite3.connect("Model/watch_list.db")

            con.execute("""
                CREATE TABLE Download_list(
                    id INTEGER PRIMARY KEY,
                    Movie_name VACHAR(500)   
                )
            """)
            return con
        
        # creating a user data database
        def users():

            con = sqlite3.connect("Model/inWatch_users.db")
            con.execute("""CREATE TABLE AllUsers(
                id INTEGER PRIMARY KEY,
                name VACHAR(500) NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL UNIQUE
                )""")
            return con
        
        try:
            # initilizing the files
            dbs = ["Archaive", "Downloads", "Watch list", "users"]
            
            with Progress(SpinnerColumn(),TextColumn("[progress.description]{task.description}"),transient=True,) as progress:
                progress.add_task(description="Creating database files...", total=100)

                archive()
                downloads()
                watch_list()
                users()
                console.log("[green]Database files created[/green]\n")
        except sqlite3.OperationalError as e:
            console.log(f"[bold red]{e}[/bold red]")

    def __str__(self) -> str:
        exist = Table()
        console.print("-- Database actions Runnig --", new_line_start=True, style="green")
    
# writing data

class DBWrite(Database):

    # adding new users
    def adding_users(self, 
        name, email: str, phone, password
        ):

        # hasing the password
        Password = crypt_detail(str(password))

        # creating the user database for new users
        con = sqlite3.connect("Model/inWatch_users.db")

        try:
            con.execute("INSERT INTO AllUsers(name, email, phone, password)VALUES ('{}', '{}', '{}', '{}')".format(name, email, phone, Password))
            con.commit()
            return con
        except sqlite3.IntegrityError as e:
            return "User exists"


    # adding into  download
    def downloads(self, Movie_name, Genre, release_date):

        # creating the user database for new users
        con = sqlite3.connect("Model/downloads.db")
        con.execute("""INSERT INTO downloads(Movie_name, Genre, release_date) 
                    VALUES (?, ?, ?)""", 
                    (Movie_name, Genre, release_date)
                    )

        return con
    
    # adding into archaive 
    def archive(self, Movie_name, Genre, release_date):

        # creating the user database for new users
        con = sqlite3.connect("Model/archaive.db")
        con.execute("""
            INSERT INTO archaive(Movie_name, Genre, release_date)
            VALUES (?, ?, ?, ?)
        """, 
        (Movie_name, Genre, release_date))

        return con
    
    # adding to 
    def watchList(self, Movie_name):
        
        con = sqlite3.connect("Model/watch_list.db")
        con.execute("""
            INSERT INTO watch_list(
                id INTEGER PRIMARY KEY,
                Movie_name VACHAR(500)   
            )
            VALUES (?)
        """, (Movie_name))

        return con

# getting the user data from the APP
class AppDetails:
    pass

