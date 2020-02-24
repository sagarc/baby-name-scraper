# Baby Name Scraper

This crawler crawls a popular Indian baby names website and dumps all names into a single file. It is written using the scrapy framework in Python.

This currently only crawls for boy names. For girl names, edit the url in `bachpandotcom/spiders/bachpan.py` and replace `indian-boy-names` with `indian-girl-names`.

## Requirements

* scrapy

## How to use it for your own scrape

`scrapy crawl bachpan -o bachpan.json` . This crawls the website and dumps the names into `bachpan.json`. `bachpan.json` can be processed using `parsejson.py`


## Results

The results of my scrape are present in `bachpan.json` and the text file dump is in `bachpan.txt`
