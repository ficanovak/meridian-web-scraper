# Meridian Web Scraper  ![GitHub follow](https://img.shields.io/github/followers/ficanovak?label=Follow&style=social) ![GitHub repo size](https://img.shields.io/github/repo-size/ficanovak/meridian-web-scraper) ![GitHub](https://img.shields.io/github/license/ficanovak/meridian-web-scraper) ![GitHub](https://img.shields.io/badge/built%20with-Python3-green) ![GitHub](https://img.shields.io/badge/-bs4-blue)

 A web scraping script used for picking up NBA player's limits and odds from a [Meridian](https://meridianbet.rs/sr/kladjenje) betting company's website.
 
 ## How it works
 
 Python script used for scraping betting company's website and finalizing output into table on MsSQL server or, for the sake of the presentation, CSV file.
 Script is packing all info into several columns:
 - Player
 - Team
 - Game date
 - Points (Limit given by the betting company)
 - Date & time indicator of the scraper writing into table
 
 <p align="center">
  <img src="output_example.png"/>
</p>
 
 ## Python modules used    
 - pandas
 - requests
 - bs4
 - datetime
 - sqlalchemy


## What's included

Within the download you'll find common assets providing both compiled and minified variations. You should see something like this:

```text
meridian-web-scraper/
├── meridian-output.csv
├── meridian-scraper.py
└── output_example.png
```
