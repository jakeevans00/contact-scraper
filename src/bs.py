from urllib.parse import urlparse, parse_qs, urlencode, urlunparse, unquote
from bs4 import BeautifulSoup
import html
import re

class BSParser:
    def __init__(self, html):
        self.html = html
        
    def run(self):
        result = self.extract_page_data()
        return result
        
    def extract_page_data(self):
        soup = BeautifulSoup(self.html, 'html.parser')
        sidebar_section = soup.find('div', {'id': 'rl_ist0'})
        maps_cards = sidebar_section.find_all('div', id=True)
        
        all_cards_data = []
        
        for card in maps_cards:
            card_data = self.get_card_details(card)
            if card_data:  # Only add if we got valid data
                all_cards_data.append(card_data)
                
        return all_cards_data
        
    def get_card_details(self, card):
        card_data = {
            'name': '',
            'rating': '',
            'review_count': '',
            'phone': '',
            'address': '',
            'maps_url': ''
        }
        
        # Extract business name
        name_span = card.find('span')
        if name_span:
            card_data['name'] = name_span.text.strip()
        
        # Extract rating
        rating_label_span = card.find('span', attrs={'aria-label': lambda value: value and 'Rated' in value})
        if rating_label_span:
            card_data['rating'] = rating_label_span['aria-label'].split()[1]
            review_count_span = rating_label_span.find_next_sibling('span', class_='RDApEe YrbPuc')
            if review_count_span:
                card_data['review_count'] = review_count_span.text.strip('()')
        
        # Extract phone number
        details_div = card.find('div', class_='rllt__details')
        if details_div and len(details_div.find_all('div')) > 3:
            phone_text = details_div.find_all('div')[3].get_text(strip=True)
            if '(' in phone_text:
                card_data['phone'] = '(' + phone_text.split('(')[1]
        
        # Extract directions link/address
        all_a_tags = card.find_all('a')
        for a_tag in all_a_tags:
            directions_div = a_tag.find('div', string='Directions')
            if directions_div:
                href_content = a_tag.get('href', '')
                card_data['maps_url'] = href_content
                
                # Use the flexible URL parser that detects the format
                url_info = self.parse_maps_url(href_content)
                card_data['address'] = url_info['address']
                if url_info['place_id']:
                    card_data['place_id'] = url_info['place_id']
                
                break
        
        return card_data
    
    def parse_maps_url(self, original_url):
        # First, decode HTML entities
        decoded_url = html.unescape(original_url)
        
        # Parse the URL
        parsed_url = urlparse(decoded_url)
        query_params = parse_qs(parsed_url.query)
        
        result = {
            'original_url': decoded_url,
            'address': '',
            'place_id': ''
        }
        
        # Detect URL pattern
        if 'daddr' in query_params:
            # Old style URLs with daddr parameter
            result['address'] = query_params.get('daddr', [''])[0]
            result['url_type'] = 'daddr'
            
        elif parsed_url.path.startswith('/maps/dir/'):
            # New style URLs with address in path
            path_parts = parsed_url.path.split('/')
            # For URLs like /maps/dir//Address/data=...
            if len(path_parts) >= 4 and path_parts[3]:
                result['address'] = unquote(path_parts[3])
                result['url_type'] = 'dir_path'
                
                # Extract place_id if available
                place_id_match = re.search(r'1s([^:]+)', decoded_url)
                if place_id_match:
                    result['place_id'] = place_id_match.group(1)
        
        # Common parameters for both URL types
        for param in ['sa', 'hl', 'gl']:
            if param in query_params:
                result[param] = query_params[param][0]
        
        return result