"""
This document contains the scraper for the search engine as well as a scraper of the currently biggest trends, that are
then put into the search engine.

Created by Marty Lauterbach on the 31st of July 2023, Warsaw, Poland.
"""

# here we import multiple libaries that we need for the search engine

# library that gets the biggest trends of the day of multiple categories and puts them into a list
from pytrends.request import TrendReq
# library that can be used to make a request for search engine searches and then scrape the results
# search engines include google, baidu, yahoo, duckduckgo
from pydork.engine import SearchEngine


def get_trends() -> list:
    """
    this will be a function that uses pytrends to get the overall trending topics
    :rtype: list
    :return: returns a list of the trending topics of the day
    """
    # here we create a pytrends object
    pytrends = TrendReq(hl='en-US', tz=360)

    # here we get the trending topics of the day
    trending_searches_df = pytrends.trending_searches(pn='united_states')

    # here we get the trending topics of the day
    trending_searches_df = pytrends.today_searches(pn='US')

    # here we return the trending topics of the day of the categories
    return trending_searches_df


# the following will be a function that creates one long list of all the websites that come up
# in all search engines when searching for the trending topics of the day
def get_trending_websites() -> list:
    """
    this will be a function that creates one long list of all the websites that come up
    :return: returns a list of websites
    """
    # here we create a list that will contain all the websites that come up in all search engines
    trending_websites = []

    # using the api libraries of the search engines one after another with each member of the get_trends() list
    # we append the results to the trending_websites list as a simple url-string
    for trend in list(get_trends()):
        search_engine = SearchEngine()
        powerhouses = ("google", "baidu", "yahoo", "duckduckgo")
        for engine in powerhouses:
            search_engine.set(engine)
            trending_websites.append(search_engine.search(trend))
    return trending_websites


def clean_website_list(websites: list, whitelist: list) -> list:
    """
    this will be a function that cleans the list of websites.
    We will be using a dynamic whitelist
    :param whitelist: list of urls that are not allowed in the list of websites
    :param websites: list of websites that were search engine scraped
    :return: returns a cleaned list
    """

    # here we iterate through the list of websites
    for website in websites:
        # here we iterate through the whitelist
        for url in whitelist:
            # here we check if the url is in the website
            if website == url:
                # here we append the website to the cleaned list
                websites.remove(website)
    return websites
