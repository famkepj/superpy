# Imports
import csv
import os

from rich.console import Console
console = Console()

from super import *
from date_file import *

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# make unique id - count rows (headrow has no id so -1)
# write bought product to bought.csv & inventory.csv
def buy_products(args): 
    file_exists = os.path.isfile('bought.csv')
    if file_exists:
        id_bought = 0
        with open('bought.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row 
                id_bought +=1
        id_bought-1
    else:
        id_bought = 1 

    console.print(f"Adding to bought: {args.product_name}, price: €{args.price}, expiration_date: {args.expiration_string}", style="bold green")

    fieldnames = ['id','product_name' ,'count','buy_date', 'buy_price', 'expiration_date', 'date_sold_or_expired']

    def write_data():
        if not file_exists:
            writer.writeheader()
        writer.writerow({'id': id_bought, 'product_name': args.product_name, 'count': 1, 'buy_date':get_date().date(), 'buy_price':args.price, 'expiration_date':args.expiration_string, 'date_sold_or_expired':args.expiration_string})

    file_exists = os.path.isfile('bought.csv')
    with open ('bought.csv', 'a', newline='') as file_bought:
        writer = csv.DictWriter(file_bought, fieldnames=fieldnames)
        write_data()

    file_exists = os.path.isfile('inventory.csv')
    with open ('inventory.csv', 'a', newline='') as file_inventory: 
        writer = csv.DictWriter(file_inventory, fieldnames=fieldnames)
        write_data()

