# Userguide _Superpy_

SuperPy is a command-line tool that a supermarket will use to keep track of their inventory. The core functionality is about keeping track and producing reports on various kinds of data:

- Which products the supermarket offers;
- How many of each type of product the supermarket holds currently;
- How much each product was bought for, and what its expiry date is;
- How much each product was sold for or if it expired, the fact that it did;

In the commandline you can:
- [Advance time](#advance-time)
- [Buy products](#buy-product)
- [Sell products](#sell-product)
- [Get inventory report](#report-inventory)
- [Get revenue](#report-revenue)
- [Get profit](#report-profit)
- [Get graphic](#show-graphic)
- [Get custom report](#custom-report)

## Arguments
- ### Advance time 

Get inventory/ report form different day and store this in date.txt

Example: two days ahead from Today
```python
python super.py advance -time 2
```
Example: seven days ago from Today
```python
python super.py advance -time -7
```

- ### Buy product
Use command **buy** and give productname, price and expiration date
- product_name: string
- price: float
- expiration_string: string & format YYYY-MM-DD

Example: buy banaan for € 0,75 with expiration date 02-07-2022
```python
python super.py buy -pro "banaan" -e 0.75 -exp "2022-07-02"
# or
python super.py buy --product_name "banaan" --price 0.75 --expiration_string "2022-07-02"
```

- ### Sell product
Use command **sell** and give productname and sell price
- product_name: string
- price: float

Example: sell banaan for € 1,45 
```python
python super.py sell -pro "banaan" -e 1.45 
# or
python super.py sell --product_name "banaan" --price 1.45
```

- ### Report revenue
Use command **revenue** 
optional | short command | command|description|
|:--:|--|--|--|
|date |-date| --date | report from given month|    
|today |-today| --today| report today|
|now |-now |--now| report new date _ advance time
|yesterday|-yes|--yesterday| report day before new date

Example: revenue from May
```python
python super.py revenue -date '2022-05'
# or
python super.py revenue --date '2022-05'
```
Example: give revenue from today
```python
python super.py revenue -today 
```

- ### Report profit
Use command **profit** 
optional | short command | command|description|
|--|--|--|--|
|date |-date| --date | report from given month|    
|today |-today| --today| report today|
|now |-now |--now| report new date _ advance time
|yesterday|-yes|--yesterday| report day before new date

Example: profit from May
```python
python super.py profit -date '2022-05'
# or
python super.py profit --date '2022-05'
```
Example: give revenue from yesterday
```python
python super.py revenue -yes 
```

- ### Report inventory
Use command **report** 

Example: report new date
```python


```
Example: report yesterday - day before new date
```python
python super.py report -yes
```


- ### Show graphic 
Use command **graphic**
```python
python super.py graphic
```

- ### Custom report
Use command **custom_report**

You can export your own report, choose bought products, sold products or expired products
short command | command|description|
|--|--|--|
|-b |--bought| report from bought products|    
|-s |--sold| report from sold products|
|-ex |--expired| report from expired products|

Example: report from bought products
```python
python super.py custom -b
```
---


