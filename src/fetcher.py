import os
from inputs import load_txt_file
from scraper import Scraper

def get_data_from_local():
    print("Using local data...")
    return load_txt_file("temp/results.txt")

def get_data_from_api(query, num_pages):
    scraper = Scraper()
    results_raw = scraper.search_google(query, num_pages)
    
    with open('temp/results.txt', 'w') as file:
        file.write(str(results_raw))
    
    return results_raw