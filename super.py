# Imports
import argparse
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

# Your code below this line.
def main():
    # create the top-level parser
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    #create parser for the "advance time" command
    advance = subparsers.add_parser('advance')
    advance.add_argument('-time', '--time', type=int, help='move time from today', required=True)  

    # create parser for the "buy" command
    buy = subparsers.add_parser('buy')
    buy.add_argument('-pro', '--product_name', type=str, help='enter productname', required=True)
    buy.add_argument('-e', '--price', type=float, help='enter price', required=True)
    buy.add_argument('-exp', '--expiration_string', type= str, help='enter expiration date YYYY-MM-DD', required=True)

    # create parser for the "sell" command
    sell = subparsers.add_parser('sell')
    sell.add_argument('-pro', '--product_name', type=str, help='enter productname', required=True)
    sell.add_argument('-e', '--price', type=float, help='enter price', required=True)

    # create parser for the "report" command
    report = subparsers.add_parser('report')
    report.add_argument('-yes', '--yesterday', help='report from yesterday', action='store_true')

    # create parser for the "revenue" command
    revenue = subparsers.add_parser('revenue')
    revenue.add_argument('-date', '--date', type=str, help='date from report "2022-06"')
    revenue.add_argument('-today', '--today',  help='report from today', action='store_true')
    revenue.add_argument('-now', '--now',  help='report from new_date', action='store_true')
    revenue.add_argument('-yes', '--yesterday', help='report from yesterday', action='store_true')

    # create parser for the "profit" command
    profit = subparsers.add_parser('profit')
    profit.add_argument('-date', '--date', type=str, help='date from report "2022-06"')
    profit.add_argument('-today', '--today',  help='report from today', action='store_true')
    profit.add_argument('-now', '--now',  help='report from new_date', action='store_true')
    profit.add_argument('-yes', '--yesterday', help='report from yesterday', action='store_true')

    # create parser for the "graphic" command
    subparsers.add_parser('graphic')

    # create parser for the "custom" command
    custom = subparsers.add_parser('custom')
    custom.add_argument('-b', '--bought', help='report from bought products', action='store_true')
    custom.add_argument('-s', '--sold', help='report from sold products', action='store_true')
    custom.add_argument('-ex', '--expired', help='report from expired products', action='store_true')
   

    # Parse the argument
    args = parser.parse_args()
    
    if args.command == 'advance':
        advance_time(args)
    if args.command == 'buy':
        buy_products(args)
    if args.command == 'sell':
        sell_products(args)
    if args.command =='revenue':
        report_revenue(args)
    if args.command == 'profit':
        report_profit(args)
    if args.command == 'report':
        report_inventory(args)
    if args.command == 'graphic':
        graphic()
    if args.command =='custom':
        custom_report(args)
    

if __name__ == "__main__":
    main()

