# import all libraries needed to scrape an article body from a website

from newspaper import Article


def scrape_that_article_pls(website):
    """
    this will be a function that scrapes the article from a website
    :param website: the website that the article is on
    :return: returns the article body
    """
    # here we create an article object
    article = Article(website)

    # here we download and parse the article
    article.download()
    article.parse()

    # here we return the article body
    return article.text
