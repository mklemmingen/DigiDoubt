"""
This document contains the scraper for the search engine as well as a scraper of the currently biggest trends, that are then put into the search engine.

Created by Marty Lauterbach on the 31st of July 2023, Warsaw, Poland.
"""

from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=360)
