import logging
from datetime import datetime
import os

from src.search_engine import google_search, get_questions

# Setting up the path for the log file
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log_directory = os.path.join(project_root, 'data', 'logs')
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# Get current date and time for the log filename
current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
log_filename = os.path.join(log_directory, f"log_{current_time}.log")

# Configure logging
logging.basicConfig(filename=log_filename, level=logging.INFO,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')


def print_info(string):
    print(f"[INFO] {string}")
    logging.info(string)


print_info("Getting trending websites...")

# Replace 'your_api_key' with your actual API key
api_key = os.environ.get('GOOGLE_API_KEY')

# Replace 'your_cse_id' with your actual Custom Search Engine ID
cse_id = os.environ.get('GOOGLE_CSE_ID')

questions = get_questions()

results = []
for question in questions:
    results.append(google_search(question, api_key, cse_id))

# Extracting and printing URLs
for item in results:
    logging.info(item)

print_info("Got websites.")

# ----------------------------------------------------------------

print_info("The program has run through completely with no errors.")
# end of script
