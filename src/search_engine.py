"""
This document contains methods that get questions from stackoverflow that are a week or two old.

Created by Marty Lauterbach on the 31st of July 2023, Warsaw, Poland.
"""

import requests
from datetime import datetime, timedelta

import requests


def get_questions() -> list:
    """
    returns a list of questions from stackoverflow that are a week or two old
    :rtype: list
    :return: returns a list of the trending topics of the day
    """
    # Calculate the date range
    end_date = datetime.now() - timedelta(days=7)  # 1 week ago
    start_date = end_date - timedelta(days=7)  # 2 weeks ago

    # Convert dates to Unix timestamps
    end_date_unix = int(end_date.timestamp())
    start_date_unix = int(start_date.timestamp())

    # Stack Overflow API endpoint for questions
    url = "https://api.stackexchange.com/2.3/questions"

    # API parameters
    params = {
        'fromdate': start_date_unix,
        'todate': end_date_unix,
        'order': 'desc',
        'sort': 'creation',
        'site': 'stackoverflow'
    }

    # Make the request
    response = requests.get(url, params=params)
    data = response.json()

    questions = []

    # Extract and print question titles
    for question in data['items']:
        questions.append(question['title'])

    return questions


# Function to perform a search
def google_search(search_term, api_key, cse_id, **kwargs):
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'q': search_term,
        'key': api_key,
        'cx': cse_id
    }
    params.update(kwargs)
    response = requests.get(search_url, params=params)

    return response.json()
