import os
import sys
import time
import json
import asyncio
from datetime import datetime
from functools import lru_cache

import httpx
import requests
from rich import *
from typer import *

url = "https://streaming-availability.p.rapidapi.com/search/basic"


def all_movies() -> dict:
	querystring = {"country":"us","service":"netflix","type":"movie","genre":"18","page":"1","output_language":"en","language":"en"}

	headers = {
		"X-RapidAPI-Key": "683b435bd8mshe2e9806278fe2c3p1efd19jsndfbf4d74fe54",
		"X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
	}

	response = requests.request("GET", url, headers=headers, params=querystring)

	return response.text

def detailed_results():
	res = json.loads(all_movies())
	details = res['results']
	return details

def server_error():
	return "[bold red]Server Error[/bold red]"


# if __name__ == '__main__':
# 	print(detailed_results())