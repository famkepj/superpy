# Imports
import csv
import os
import pandas

from super import *
from inventory import *
from date_file import get_date

from rich.console import Console
console = Console()

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# make unique id - count rows (headrow has no id so -1)
# update inventory with function: inventory_expiration_update() - because you don't want to sell expired products
# check if required product is in inventory
# if product is in inventory write sold product to sold.csv with calculated profit and update inventory with function: inventory_update()
# if product is not in inventory: print('not in stock')
def sell_products(args):                     
    product_stock = False      

    file_exists = os.path.isfile('sold.csv')
    if file_exists:
        id_sell = 0
        with open('sold.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                row 
                id_sell +=1
        id_sell-1
    else:
        id_sell = 1
        
    inventory_expiration_update()

    with open ('inventory.csv', 'r', newline='') as inventory_file:
        dict_reader_inventory_file = csv.DictReader(inventory_file)
        for stock in dict_reader_inventory_file:
            if args.product_name.lower() == stock['product_name'].lower():
                product_stock = True
                console.print(f"Sold {args.product_name}, price: €{args.price}", style = "bold green")
                stock.update({'sell_price': args.price})
                stock.update({'sell_date': get_date().date()})
                stock.update({'revenue': args.price})
                stock.update({'profit': round((args.price - float(stock['buy_price'])),2)})
                stock['count'] = 0
                id_product = (stock['id'])
                inventory_update(id_product)
                
                rownumber = int(id_product)-1
                bought_file = pandas.read_csv('bought.csv')
                bought_file.loc[rownumber, 'date_sold_or_expired'] = get_date().date()
                bought_file.to_csv('bought.csv', index=False)
   
                file_exists = os.path.isfile('sold.csv')
                with open ('sold.csv', 'a', newline='') as file:
                    writer_sold = csv.DictWriter(file, fieldnames= ['id','bought_id','product_name', 'sell_date' ,'sell_price','profit'])
                    if not file_exists:
                        writer_sold.writeheader()
                    writer_sold.writerow({'id': id_sell, 'bought_id': stock['id'], 'product_name': stock['product_name'],'sell_date': get_date().date(), 'sell_price':args.price, 'profit':stock['profit']}) 
                break
            else:
                continue 
        if product_stock == False:
            console.print('Not in stock', style = "bold red")