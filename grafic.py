# Imports
import csv
from rich.console import Console
import typer
import os
import pandas
import matplotlib.pyplot as plt

console = Console()
app = typer.Typer()

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"

# graphic revenue & profit
# get data and store in graphic.csv
# set up graphic & show
def graphic():
    file_exists = os.path.isfile('graphic.csv')
    if file_exists:
        os.remove('graphic.csv')

    with open ('sold.csv', 'r', newline='') as sold_file:
            dict_reader_sold_file = csv.DictReader(sold_file)
            for graphic_revenue in dict_reader_sold_file:
                file_exists = os.path.isfile('graphic.csv')
                with open ('graphic.csv', 'a', newline='') as report_file:
                        dict_reader_report_file = csv.DictWriter(report_file, fieldnames= ['bought_id', 'date', 'sell_price', 'profit', 'expired_loss'])
                        if not file_exists:
                            dict_reader_report_file.writeheader()
                        dict_reader_report_file.writerow({'bought_id':graphic_revenue['bought_id'],'date':graphic_revenue['sell_date'], 'sell_price': graphic_revenue['sell_price'], 'profit':graphic_revenue['profit']})      
    try:
        with open ('loss.csv', 'r', newline='') as loss_file:
                dict_reader_loss_file = csv.DictReader(loss_file)
                for graphic_profit in dict_reader_loss_file:  
                    with open ('graphic.csv', 'a', newline='') as report_file: 
                        dict_reader_report_file = csv.DictWriter(report_file, fieldnames= ['bought_id','date', 'sell_price', 'profit', 'expired_loss'])
                        dict_reader_report_file.writerow({'bought_id':graphic_profit['bought_id'],'date':graphic_profit['expiration_date'],'expired_loss':graphic_profit['expired_loss']})  
        read_sorted_data = pandas.read_csv('graphic.csv')
        plt.bar(read_sorted_data['bought_id'],read_sorted_data['sell_price'],label='revenue', width = 0.2)
        plt.bar(read_sorted_data['bought_id'],read_sorted_data['profit'],label='profit_sale', width = 0.2)
        plt.bar(read_sorted_data['bought_id'],read_sorted_data['expired_loss'],label='expired_loss', width = 0.2, color='red')
        plt.title('Graphic')
        plt.ylabel('euro')
        plt.xlabel('bought_id')
        plt.legend(loc = 'best')
        plt.show()

    except:
        read_sorted_data = pandas.read_csv('graphic.csv')
        plt.bar(read_sorted_data['bought_id'],read_sorted_data['sell_price'],label='revenue', width = 0.2)
        plt.bar(read_sorted_data['bought_id'],read_sorted_data['profit'],label='profit_sale', width = 0.2)
        console.print('Grafic without loss, because no loss in this period', style = 'bold')
        plt.title('Graphic')
        plt.ylabel('euro')
        plt.xlabel('bought_id')
        plt.legend(loc = 'best')
        plt.show()




