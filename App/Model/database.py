
import base64
import os
import re
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

    encoded_pswd = hashlib.sha256()
    encoded_pswd.update(det.encode())

    return encoded_pswd.hexdigest()

# mail validator
def is_mail(email: str):

    # iterating thourgh out database in my case a list
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if re.fullmatch(regex, email):
        return True
    else:
        return False


# creating the database
class Database:

    # creating new files
    def create_new_files(self):
        
        def archive():
            
            con = sqlite3.connect("App/Model/archaive.db")

            con.execute("""
                CREATE TABLE Download_list(
                    id INTEGER PRIMARY KEY,
                    Movie_name VACHAR(500),
                    Genre VARCHAR(500),
                    Release_date DATETIME)
            """)
            try:
                return con
            except:
                console.print("Database already exist", style="bold red")
        
        def downloads():
            
            con = sqlite3.connect("App/Model/downloads.db")

            con.execute("""
                CREATE TABLE Download_list(
                    id INTEGER PRIMARY KEY,
                    Movie_name VARCHAR(500),
                    Genre VARCHAR(500),
                    Release_date DATETIME   
                )
            """)
            return con
        
        def watch_list():
            
            con = sqlite3.connect("App/Model/watch_list.db")

            con.execute("""
                CREATE TABLE Download_list(
                    id INTEGER PRIMARY KEY,
                    Movie_name VARCHAR(500)   
                )
            """)
            return con
        
        # creating a user data database
        def users():

            con = sqlite3.connect("App/Model/inWatch_users.db")
            con.execute("""CREATE TABLE AllUsers(
                id INTEGER PRIMARY KEY,
                name VARCHAR(500) NOT NULL UNIQUE,
                email TEXT NOT NULL UNIQUE,
                phone TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL UNIQUE
                )""")
            return con
        
        try:
            # initilizing the files
            
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
        console.print("-- Database actions Runnig --", new_line_start=True, style="green")
    
# writing data

class DBWrite:

    # adding new users
    def adding_users(self, 
        name, email: str, phone, password
        ):

        if is_mail(email):

            # hasing the password
            Password = crypt_detail(str(password))

            # creating the user database for new users
            con = sqlite3.connect("App/Model/inWatch_users.db")

            try:
                con.execute("INSERT INTO AllUsers(name, email, phone, password)VALUES ('{}', '{}', '{}', '{}')".format(name, email, phone, Password))
                con.commit()
                return con
            except sqlite3.IntegrityError as e:
                return "User exists"
        else:
            return "Invalid email"


    # adding into  download
    def downloads(self, Movie_name, Genre, release_date):

        # creating the user database for new users
        con = sqlite3.connect("App/Model/downloads.db")
        con.execute("""INSERT INTO downloads(Movie_name, Genre, release_date) 
                    VALUES (?, ?, ?)""", 
                    (Movie_name, Genre, release_date)
                    )

        return con
    
    # adding into archaive 
    def archive(self, Movie_name, Genre, release_date):

        # creating the user database for new users
        con = sqlite3.connect("archaive.db")
        con.execute("""
            INSERT INTO archaive(Movie_name, Genre, release_date)
            VALUES (?, ?, ?, ?)
        """, 
        (Movie_name, Genre, release_date))

        return con
    
    # adding to 
    def watchList(self, Movie_name):
        
        con = sqlite3.connect("watch_list.db")
        con.execute("""
            INSERT INTO watch_list(
                id INTEGER PRIMARY KEY,
                Movie_name VACHAR(500)   
            )
            VALUES (?)
        """, (Movie_name))

        return con

# getting the user data from the APP
class UserDetails:


    # cheack user
    def in_database(self, user_login_option, password): # if the password entered by use matches the database we approve the user

        # hash the new entered password to compare the hashes
        entered_password = crypt_detail(password)

        # getting passwords,username and email
        conn = sqlite3.connect("Model/inWatch_users.db")

        # runnung queries depending on the way the user wants to login either by email or password
        if is_mail(user_login_option):
            cursor = conn.execute(f"SELECT password FROM AllUsers WHERE email='{user_login_option}'")
            data = cursor.fetchall()

            password_in_db = data[0][0]

            if entered_password == password_in_db:
                return True
            elif entered_password != password_in_db:
                return False

        else:
            cursor = conn.execute(f"SELECT password FROM AllUsers WHERE name='{user_login_option}'")
       
            data = cursor.fetchall()

            password_in_db = data[0][0]

            if entered_password == password_in_db:
                return True
            elif entered_password != password_in_db:
                return False

if __name__ == '__main__':
    use_det = UserDetails()
    print(use_det.in_database("stacy", "minoo"))