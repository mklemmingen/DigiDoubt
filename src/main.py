
import logging
from datetime import datetime
import os

from src.search_engine import google_search, get_questions


# creating a new log file in data/log with the current date and time
# Get current date and time for the log filename
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = f"data/log/log_{current_time}.log"

# Configure logging
logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def print_info(string):
    print(f"[INFO] {string}")
    logging.info(string)

print_info("Getting trending websites...")

# Replace 'your_api_key' with your actual API key
api_key = 'your_api_key'

# Replace 'your_cse_id' with your actual Custom Search Engine ID
cse_id = 'your_cse_id'

questions = get_questions()

results = []
for question in questions:
    results.append(google_search('example search', api_key, cse_id))

# Extracting and printing URLs
for item in results:
    logging.info(item)

print_info("Got websites.\n")

# import the whitelist.txt that is in src/whitelist.txt, with reading and make it a list
with open('src/whitelist.txt', 'r') as f:
    whitelist = f.readlines()

# ----------------------------------------------------------------

print("The program has run through completely.\n")
# end of script
