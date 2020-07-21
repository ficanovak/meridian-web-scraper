import pandas as pd
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sqlalchemy as sa

engine = sa.create_engine('mssql+pyodbc://sa:INSERT USERNAME@INSERT SERVER ADDRESS?DRIVER={ODBC Driver 13 for SQL Server}',fast_executemany=True)

# parse stranice 
page = requests.get('https://oddscheck.meridianbet.com/prices?leagueID=593')
soup = BeautifulSoup(page.content, 'html.parser')

# selekcija html entiteta (igraca) za skrejpovanje
items = soup.select('ul')
broj_igraca = len(items)

players = []
points = []
teams = []
date = []

# formatiranje meseca u datumu, html vraca mesec u vidu "Jan", "Feb"
def mesec(string):
    return "01" if string == "Jan" else "02" if string == "Feb" else "03" if string == "Mar" else "04" if string == "Apr" else "05" if string == "May" else "06" if string == "Jun" else "07" if string == "Jul" else "08" if string == "Aug" else "09" if string == "Sep" else "10" if string == "Oct" else "11" if string == "Nov" else "12" if string == "Dec" else "Error"

# iteracija kroz svaki entitet (igrac)
for player in items:
    pdata = player.previous.strip().partition('-')[2]
    pdate = player.previous.strip().split(" ")
    # name = pdata.partition(' (')[0]
    players.append(pdata.partition(' (')[0])
    # team = pdata.partition(' (')[2].rstrip(")")
    teams.append(pdata.partition(' (')[2].rstrip(")"))
    limit1 = player.select('li')[0].text.partition(', OU : ')[2].replace(']','')
    limit2 = player.select('li')[1].text.partition(', OU : ')[2].replace(']','')
    limit3 = player.select('li')[2].text.partition(', OU : ')[2].replace(']','')
    limit4 = player.select('li')[3].text.partition(', OU : ')[2].replace(']','')
    limit = float(limit1) + float(limit2) + float(limit3) + float(limit4)
    points.append(limit)
    # date = mesec(pdate[2]) + "-" + pdate[3] + "-" + pdate[6].replace(",", "")
    date.append(mesec(pdate[2]) + "-" + pdate[3] + "-" + pdate[6].replace(",", ""))

    # print(f"{name} ({team}) : {date} : {limit}")

ct = datetime.today()

# output tabele
players_stuff = pd.DataFrame(
    {
        'player': players,
        'team': teams,
        'date': date,
        'points': points,
        'datetime' : ct,
    })


c = engine.connect()

# brisanje postojece tabele na serveru
sql_delete = (f"INSER YOUR SQL CODE FOR TABLE DELETION") 
deletion = c.execute(sql_delete)

# upis u tabelu na serveru
players_stuff.to_sql('meridian',con=engine)

# output kao csv fajl
# players_stuff.to_csv(r'meridian.csv')
