# Report Superpy

Please include a short, 300-word report that highlights three technical elements of your implementation that you find notable, explain what problem they solve and why you chose to implement it in this way. 

1) Voorkom dat je iets verkoopt wat je niet meer hebt/ weergave voorraad tabel
> Extra bestand gemaakt inventory.csv

Dit bestand wordt ge-update bij het inkopen van producten, verkopen van producten en voordat een rappot opgevraagd wordt filterd deze de verlopen producten naar een bestand loss.

Op deze manier gedaan, zodat data overzichtelijk is en herbruikbaar

2) Bijhouden hoeveel winst je gemaakt hebt
> Extra bestand gemaakt loss.csv

Dit bestand wordt ge-update bij het aanmaken van een raport van de voorraadlijst, aanvragen van raport winst, en voor de verkoop. Op deze manier staan er geen producten op voorraad die verlopen zijn, kunnen er geen verlopen producten verkocht worden en wordt er bij het berekenen van de winst het verlies van de verlopen producten meegenomen.

functie gemaakt en deze op diverse plaatsen ingezet
```python
inventory_expiration_update(today)
```

3) Bijhouden wat de nieuwe datum is met advance_time
> Extra tekst file gemaakt waar de nieuwe datum in opgeslagen is
Hierdoor kan ik de nieuwe datum (advance-time) makkelijk opslaan en hergebruiken

- Tekstfile i.p.v. csv file, omdat er maar 1 string in opgeslagen wordt. 

- Aparte file i.p.v. opnieuw aanroepen van de functie. Je mist in de andere functie een argument, en je wilt deze functies los van elkaar kunnen gebruiken. Dus meest logische was om de nieuwe datum ergens op te slaan, zodat ik hem indien nodig kan bijwerken en oproepen.

```python
def advance():
    new_date = date.today() + timedelta(advance_time)
    print("Inventory/ report from date", new_date)
    date_file = open ('date.txt', 'w') 
    date_file.write(str(new_date))
    date_file.close()
```
```python
def report_revenue():
    get_revenue = pandas.read_csv('sold.csv')                                   
    get_revenue['sell_date'] = pandas.to_datetime(get_revenue['sell_date']) 
   
   ...................................................

       elif yesterday:
        date_file = open('date.txt', 'r')
        new_date = datetime.strptime((date_file.read()), '%Y-%m-%d') - timedelta(1)
        mask = get_revenue['sell_date'] <= new_date 
        revenue = sum((get_revenue.loc[mask]).get('sell_price'))
        print("Revenue until yesterday from new_date", new_date.date(),": €", round(revenue,2))

```