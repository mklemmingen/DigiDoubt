"""
This document contains the judging algorithms for the scraped articles.
Created by Marty Lauterbach on the 31st of July 2023, Warsaw, Poland.
"""


def judge(website: str, body_of_text):
    """
    this function judges a body of text by if certain phrases from ai_phrases.py are in it, as well as runs
    a nlp over it and judges it by the result.
    The website is then either put onto whitelist if negative, neutral_urls.txt if unsure and
    positive_urls.txt if very sure that an AI was used.
    If the body of text was judged to be neutral, a request is made to the url with the about-it/contact page, and
    if one was found, it is put onto the neutral_urls.txt. If one was found, a print is made to the user
    saying that this page was suspect, but not fully positive for AI usage.
    :return: in the form of a appending to whitelist.txt , neutral_urls.txt or positive_urls.txt
    """

