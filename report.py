# Imports
import csv
from datetime import timedelta, datetime
from rich.console import Console
from rich.table import Table
import os
import pandas
from dateutil.relativedelta import relativedelta

from rich.console import Console
console = Console()

from super import *
from inventory import *

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# get date from text file - function copy because otherwise circular import error
def get_date():
    date_file_txt = open('date.txt', 'r')
    file_date = datetime.strptime((date_file_txt.read()),'%Y-%m-%d')
    return file_date

# get date from given month
def data_print(args):
    date_date = datetime.strptime(args.date, '%Y-%m')
    return date_date.strftime('%B %Y')

# get start date from given month
def start_date(args):
    start_date = datetime.strptime(args.date, '%Y-%m')
    return start_date

# get end date from given month
def end_date(args):
    date_date = datetime.strptime(args.date, '%Y-%m')
    end_date = date_date + relativedelta(months=+1)
    return end_date

# read sold file if exists else print statement
def read_sold_file():
    file_exists = os.path.isfile('sold.csv')
    if file_exists:
        return (pandas.read_csv('sold.csv'))   
    else:
        return

# get selling date from sold file
def get_selling_date():
    sold_file = read_sold_file()
    sold_file['sell_date'] = pandas.to_datetime(sold_file['sell_date']) 
    return sold_file['sell_date']

# read loss file if exists else print statement
def read_loss_file():
    file_exists = os.path.isfile('loss.csv')
    if file_exists:
        return (pandas.read_csv('loss.csv'))   
    else:
        console.print('Profit report without loss', style = "bold red")

# get expiration date from loss file
def get_expiration_date():
    loss_file = read_loss_file()
    loss_file['expiration_date'] = pandas.to_datetime(loss_file['expiration_date']) 
    return loss_file['expiration_date']

# get round revenue from that month
def get_round_revenue(args):
    mask = (get_selling_date()>= start_date(args)) & (get_selling_date() <= end_date(args))
    revenue = sum((read_sold_file().loc[mask]).get('sell_price'))
    return (round(revenue,2))

# get round profit_sold from that month
def get_round_profit_sold(args):
    mask = (get_selling_date()>= start_date(args)) & (get_selling_date() <= end_date(args))
    profit_sold = sum((read_sold_file().loc[mask]).get('profit'))
    return ((round(profit_sold,2)))

# get round loss from that month
def get_round_loss(args):
    mask = (get_expiration_date()> start_date(args)) & (get_expiration_date() <= end_date(args))
    loss = sum((read_loss_file().loc[mask]).get('expired_loss'))
    return ((round(loss,2)))


# date-report: make report revenue from given month
# now: make report revenue from new date in date.txt
# yesterday: make report revenue from one day before new date in date.txt
# today: make report revenue from actually date 
def report_revenue(args):   
    if args.date:
        try:
            return console.print('Revenue from',data_print(args),': €', get_round_revenue(args), style = "bold cyan")
        except:
            return console.print('Report not possibe, there is nothing sold yet', style = "bold red")

    try:
        if args.now:
            revenue_date = get_date()
                
        elif args.yesterday:
            revenue_date = get_date() - timedelta(1)  

        elif args.today:
            revenue_date = datetime.today()

        else:
            revenue_date = get_date()

        mask = get_selling_date() <= revenue_date
        revenue = sum((read_sold_file().loc[mask]).get('sell_price'))
        console.print("Revenue until", revenue_date.date(),": €", round(revenue,2), style = "bold cyan")
    except:
        console.print('Report not possibe, there is nothing sold yet', style = "bold red")


# update inventory - expired products give less profit
# date-report: make report profit from given month 
# now: make report profit from new date in date.txt
# yesterday: make report profit from one day before new date in date.txt
# today / nothing: make report profit from actually date 
def report_profit(args): 
        inventory_expiration_update()
        if args.date:
            try:
                try:
                    return console.print("Profit from", data_print(args),": €", (get_round_profit_sold(args) - get_round_loss(args)), style = "bold cyan")
                except:
                    return console.print("Profit from", data_print(args),": €", get_round_profit_sold(args), style = "bold cyan")
            except:
                return console.print('Report not possibe, there is nothing sold yet', style = "bold red")

        try:
            if args.now:
                profit_date = get_date()

            elif args.yesterday:
                profit_date = get_date() - timedelta(1)
            
            elif args.today:
                profit_date = datetime.today()

            else:
                profit_date = get_date()

            mask = get_selling_date() <= profit_date 
            profit_sold = sum((read_sold_file().loc[mask]).get('profit'))
            try:
                mask_loss = get_expiration_date() <= profit_date 
                loss = sum((read_loss_file().loc[mask_loss]).get('expired_loss'))
                console.print("Profit until", profit_date.date(),": €", round(profit_sold - loss,2),style = "bold cyan")
            except:
                console.print("Profit until", profit_date.date(),": €", round(profit_sold,2),style = "bold cyan")
        except:
            console.print('Report not possibe, there is nothing sold yet', style = "bold red")


# make empty report.csv file
# get date 
# get products from bought.csv - take in account the bought date and the date that products are sold/ expired depending on the requested report periode - write these to report.csv file
# make a nice table with rich from the report file
def report_inventory(args):
    if args.yesterday:
        new_date = get_date() - timedelta(1)  
    else:
        new_date = get_date() 
    file_exists = os.path.isfile('report.csv')
    if file_exists:
        os.remove('report.csv')

    with open ('bought.csv', 'r', newline='') as bought_file:
        dict_reader_bought_file = csv.DictReader(bought_file)
        for inventory_report in dict_reader_bought_file: 
            bought_date = pandas.to_datetime(inventory_report['buy_date']) 
            expiration_or_sold_date = pandas.to_datetime(inventory_report['date_sold_or_expired']) 
                     
            file_exists = os.path.isfile('report.csv')
            if bought_date <= new_date:
                if expiration_or_sold_date > new_date:
                    with open ('report.csv', 'a', newline='') as report_file:
                        dict_reader_report_file = csv.DictWriter(report_file, fieldnames= ['product_name','count', 'buy_price', 'buy_date', 'expiration_date'])
                        if not file_exists:
                            dict_reader_report_file.writeheader()
                        dict_reader_report_file.writerow({'product_name': inventory_report['product_name'], 'count':inventory_report['count'], 'buy_price': inventory_report['buy_price'], 'buy_date':inventory_report['buy_date'],'expiration_date':inventory_report['expiration_date']})                   
            else:
                continue     

        console.print("Inventory report", new_date.date(), style = "bold cyan")
        table = Table(show_header=True, header_style="bold green")
        table.add_column("Product Name")
        table.add_column("Buy Price")
        table.add_column("Buy Date")
        table.add_column("Expiration Date")
        try:
            with open('report.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    product = (row['product_name']).lower()
                    table.add_row(
                        product,
                        row['buy_price'],
                        row['buy_date'],
                        row['expiration_date']
                    )
            console.print(table)   
        except:
            console.print('Report not possibe, there is no inventory this period', style = "bold red")

# Make custom report - clear existing file
# bought / sold or expired
# get data - show table
def custom_report(args):
    if args.bought:
        console.print('You choosed bought report', get_date().date(), style = "bold magenta")

        table = Table(show_header=True, header_style="bold on green")
        table.add_column("ID")
        table.add_column("Product Name")
        table.add_column("Buy Date")
        table.add_column("Buy Price")
        table.add_column("Date expired")
        table.add_column("Date sold", style='green')

        try:
            with open('bought.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['expiration_date'] != row['date_sold_or_expired']:
                        table.add_row(
                            row['id'],
                            row['product_name'],
                            row['buy_date'],
                            row['buy_price'],
                            row['expiration_date'],
                            row['date_sold_or_expired']
                        )
                    else:
                        table.add_row(
                            row['id'],
                            row['product_name'],
                            row['buy_date'],
                            row['buy_price'],
                            row['expiration_date'],
                        )
            console.print(table) 

        except:
            console.print('No data to display', style='bold')
                
    elif args.sold:
        console.print('You choosed sold report', get_date().date(), style = "bold magenta")

        table = Table(show_header=True, header_style="bold on green")
        table.add_column("ID")
        table.add_column("Product Name")
        table.add_column("Date sold")
        table.add_column("Sell Price")
        table.add_column("Profit", style = 'green')

        try:
            with open('sold.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    table.add_row(
                            row['id'],
                            row['product_name'],
                            row['sell_date'],
                            row['sell_price'],
                            row['profit'],
                        )
            console.print(table) 

        except:
            console.print('No data to display', style='bold')

    elif args.expired:
        console.print('You choosed expired report', get_date().date(), style = "bold red")
    
        table = Table(show_header=True, header_style="bold on red")
        table.add_column("ID")
        table.add_column("Product Name")
        table.add_column("Expiration date")
        table.add_column("Expired loss", style = 'red')

        try:
            with open('loss.csv', 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    table.add_row(
                            row['bought_id'],
                            row['product_name'],
                            row['expiration_date'],
                            row['expired_loss'],
                        )
            console.print(table) 

        except:
            console.print('No data to display', style='bold')
    else:
        console.print('Choose: bought / sold or expired report', style='red')