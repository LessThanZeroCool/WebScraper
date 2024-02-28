import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URLs of the pages to scrape
urls = [
    'https://www.mideastoffers.com/all-shows-list/',
    'https://www.mideastoffers.com/all-shows-list/page/2/',
    'https://www.mideastoffers.com/all-shows-list/page/3/',
    'https://www.mideastoffers.com/all-shows-list/page/4/',
    'https://www.mideastoffers.com/all-shows-list/page/5/',
    'https://www.mideastoffers.com/all-shows-list/page/6/',
    'https://www.mideastoffers.com/all-shows-list/page/7/',
    'https://www.mideastoffers.com/all-shows-list/page/8/',
    'https://www.mideastoffers.com/all-shows-list/page/9/',
    'https://www.mideastoffers.com/all-shows-list/page/10/'
]

# Headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

concerts = []  # Initialize the list to store concert data

for url in urls:
    # Delay to prevent blocking
    time.sleep(1)
    
    # Fetch the page
    response = requests.get(url, headers=headers)
    
    # Proceed only if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Loop through each event section
        for event_section in soup.find_all('div', class_='tw-section'):
            # Extract the venue name, event name, date, time, and price
            venue_name = event_section.find('span', class_='tw-venue-name').get_text(strip=True)
            event_name = event_section.find('div', class_='tw-name').get_text(strip=True)
            event_date = event_section.find('span', class_='tw-event-date').get_text(strip=True)
            event_time = event_section.find('span', class_='tw-event-time').get_text(strip=True)
            price_info = event_section.find('span', class_='tw-price')
            event_price = price_info.get_text(strip=True) if price_info else "Not Listed"
            
            concerts.append({
                'Venue Name': venue_name,
                'Date': event_date,
                'Band': event_name,
                'Time': event_time,
                'Price': event_price
            })

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(concerts)

# Save the DataFrame to a CSV file
df.to_csv('upcoming_concerts.csv', index=False)

print("CSV file has been created successfully.")


