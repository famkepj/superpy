# Imports
import csv
import os
import pandas

from super import *

from rich.console import Console
console = Console()

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# remove sold/ expired products from inventory
def inventory_update(id_product):
    number = int(id_product)
    updated_inventory = pandas.read_csv('inventory.csv')
    updated_inventory.drop(updated_inventory.index[(updated_inventory['id'] == number )],axis=0,inplace=True)
    updated_inventory.to_csv('inventory.csv', index= False)

# get new date form date.txt 
# mark expired products and remove them with function: inventory_update()
# write lost trough expiration in file loss.csv
def inventory_expiration_update():
    date_file = open('date.txt', 'r')
    new_date = date_file.read() 
    with open ('inventory.csv', 'r+', newline='') as inventory_file:
        dict_reader_inventory_file = csv.DictReader(inventory_file)
        for expiration_check in dict_reader_inventory_file:
            expiration_date = expiration_check['expiration_date']
            if new_date >= expiration_date:
                expiration_check.update({'expired': True})
                expiration_check.update({'expired_loss': (expiration_check['buy_price'])})
                id_product = (expiration_check['id'])
                inventory_update(id_product)
                loss_exists = os.path.isfile('loss.csv')
                with open ('loss.csv', 'a', newline='') as loss_file:                  
                    writer_loss = csv.DictWriter(loss_file, fieldnames= ['bought_id','product_name','expiration_date', 'expired_loss' ])
                    if not loss_exists:
                        writer_loss.writeheader() 
                    writer_loss.writerow({'bought_id': expiration_check['id'], 'product_name': expiration_check['product_name'], 'expiration_date':expiration_check['expiration_date'], 'expired_loss': expiration_check['buy_price']})     
            else:
                continue  

