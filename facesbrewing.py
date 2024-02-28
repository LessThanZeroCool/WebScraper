import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# URL of the page to scrape
url = 'https://www.facesbrewing.com/store/events/'

# Headers to mimic a browser visit
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

# Delay to prevent blocking
time.sleep(1)

venue = 'Faces Brewing Co.'  # Venue name

# Fetch the page
response = requests.get(url, headers=headers)

# Proceed only if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

events = []

# Loop through each event card
for card in soup.find_all('li', class_='card'):
    # Extract the event name
    event_name = card.find('h3', class_='card__heading').get_text(strip=True)
    
    # Extract the event date and time
    event_date_time = card.find('h2', class_='card__subheading').get_text(strip=True)
    
    # Extract the event type if available
    event_type = card.find_all('h2', class_='card__subheading')[1].get_text(strip=True) if len(card.find_all('h2', class_='card__subheading')) > 1 else "Not Listed"
    
    # Extract the event description
    event_description = card.find('p').get_text(strip=True) if card.find('p') else "Not Listed"

    events.append({
        'Venue Name': venue,  # Add the venue name to the dictionary
        'Event Name': event_name,
        'Date and Time': event_date_time,
        'Type': event_type,
        'Description': event_description
    })

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(events)

# Save the DataFrame to a CSV file
df.to_csv('faces_brewing_events.csv', index=False)

print("CSV file has been created successfully.")
