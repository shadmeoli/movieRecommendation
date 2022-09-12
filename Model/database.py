from errno import EEXIST
import os
import sqlite3
import json
import random
from datetime import datetime
import asyncio
from functools import lru_cache, reduce, _make_key
import hashlib

from rich.console import Console
import typer 

console = Console()

# excrypting the passwords and any sensitive data
def crypt_detail(det: str):

    sha = hashlib.md5(det)
    return sha

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
                    Release_date DATETIME   
                )
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
            try:
                return con
            except EEXIST:
                console.print("Database already exist", style="bold red")
        
        def watch_list():
            
            con = sqlite3.connect("Model/wathc_list.db")

            con.execute("""
                CREATE TABLE Download_list(
                    id INTEGER PRIMARY KEY,
                    Movie_name VACHAR(500)   
                )
            """)
            try:
                return con
            except EEXIST:
                console.print("Database already exist", style="bold red")
        
        # creating a user data database
        def users():

            con = sqlite3.connect("Model/inWatch_users.db")

            con.execute("""
                CREATE TABLE Users(
                    id INTEGER PRIMARY KEY,
                    name VACHAR(500) NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    phone TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL UNIQUE,
                )
            """)
            try:
                return con
            except EEXIST:
                console.print("Database already exist", style="bold red")

        
        # initilizing the files
        archive()
        downloads()
        watch_list()
        users()

    def __str__(self) -> str:
        console.print("-- Database actions Runnig --", new_line_start=True, style="green")
    

# writing data
class DBWrite(Database):

    # adding new users
    def adding_users(self,  name, email, phone, password):

        # hasing the password
        Password = crypt_detail(str(password))

        # creating the user database for new users
        con = sqlite3.connect("Model/inWatch_users.db")
        con.execute("""
            INSERT INTO inWatch_users(name, email, phone, password)
            VALUES (%s, %s, %s, %s)
        """, 
        (name, email, phone, Password))

        return con


if __name__ == '__main__':
    db = Database()
    db.create_new_files()