#!/usr/bin/python3.8
# coding:u8


from requests import get
from scrapy import Selector


# RESSOURCES __________________________________________________________________________
# https://ledatascientist.com/introduction-au-web-scraping-avec-python/


def scrap_an_url(url):
    response = get(url)
    source = None
    if response.status_code == 200 :
        source = response.text

    if source :
        selector = Selector(text=source)
        title = selector.css("head > title")
        text_to_read = title.css("title::text").extract_first()
        # All sites are different it seems hard to use this way
        # to read a whole site.

    return text_to_read

