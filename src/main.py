# this will be the main file for the project, using the functions from the other files

# here we import the other files

from src.search_engine import get_trending_websites, clean_website_list
from src.article_scraper import scrape_that_article_pls
from judge import judge

# start of script

to_check = get_trending_websites()

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
