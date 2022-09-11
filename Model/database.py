from errno import EEXIST
import os
import sqlite3
import json
import random
from datetime import datetime
import asyncio
from functools import lru_cache, reduce, _make_key

from rich.console import Console
import typer 

console = Console()

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
        
        # initilizing the files
        archive()
        downloads()
        watch_list()
    
    # inserting values to the db


    def __str__(self) -> str:
        console.print("-- Database actions Runnig --", new_line_start=True, style="green")
    

if __name__ == '__main__':
    db = Database()
    db.create_new_files()