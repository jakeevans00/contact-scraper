import requests
import os
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

class Scraper:
    def __init__(self):
        pass

    def search_google(self, query = 'Beauty salon, Sonora CA', page_count = 1):
       
        # Structure payload.
        payload = {
            'source': 'google_maps',
            'query': query,
            'pages': int(page_count)
        }

        # Get response.
        response = requests.request(
            'POST',
            'https://realtime.oxylabs.io/v1/queries',
            auth=(os.getenv("USERNAME"), os.getenv("PASSWORD")), 
            json=payload,
        )
        
        return response.json()