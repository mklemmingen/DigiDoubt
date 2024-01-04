
import logging
from datetime import datetime
import os

from src.search_engine import get_trending_websites, clean_website_list
from src.website_scraper import scrape_that_article_pls

from judge import judge

# creating a new log file in data/log with the current date and time
# Get current date and time for the log filename
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"data/log/log_{current_time}.log"

# Configure logging
logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def printInfo(string):
    print(f"[INFO] {string}")
    logging.info(string)

printInfo("Getting trending websites...")
to_check = get_trending_websites()
printInfo("Got trending websites.\n")
logging.info(f"Trending websites: {to_check} \n")

# import the whitelist.txt that is in src/whitelist.txt, with reading and make it a list
with open('src/whitelist.txt', 'r') as f:
    whitelist = f.readlines()

cleaned = clean_website_list(to_check, whitelist)

print(cleaned)

# use the functions from article_scraper to scrape the articles from the websites
# then immediately use the functions from judge to judge the articles

for website in cleaned:
    article_text = scrape_that_article_pls(website)
    judge(website, article_text)

print("The program has run through completely.\n")
# end of script
