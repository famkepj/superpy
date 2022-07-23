# Imports
from datetime import timedelta, datetime
from rich.console import Console
import typer

from buy import *
from sell import *
from report import *
from grafic import *
from inventory import *

console = Console()
app = typer.Typer()

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# get date from text file
def get_date():
    date_file_txt = open('date.txt', 'r')
    file_date = datetime.strptime((date_file_txt.read()),'%Y-%m-%d')
    return file_date

# get_date + timedelta  -   print date without time -   store the new_date in text file without time
def advance_time(args):
    date_new = get_date() + timedelta(args.time)
    print("Inventory/ report from date", date_new.date())
    date_file = open ('date.txt', 'w') 
    date_file.write(str(date_new.date()))
    date_file.close()

