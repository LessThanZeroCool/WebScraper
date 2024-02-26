import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page to scrape
url = 'https://www.mideastoffers.com/all-shows-list/'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the page with BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Initialize an empty list to store concert information
concerts = []

# Loop through each event section in the HTML
for event_section in soup.find_all('div', class_='tw-section'):
    # Extract the event name
    event_name = event_section.find('div', class_='tw-name').get_text(strip=True)
    # Extract the venue name
    venue_name = event_section.find('span', class_='tw-venue-name').get_text(strip=True)
    # Extract the event date
    event_date = event_section.find('span', class_='tw-event-date').get_text(strip=True)
    # Extract the event time
    event_time = event_section.find('span', class_='tw-event-time').get_text(strip=True)
    
    # Append the extracted information as a dictionary to the concerts list
    concerts.append({
        'Venue Name': venue_name,
        'Date': event_date,
        'Band': event_name,
        'Time': event_time
    })

# Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(concerts)

# Save the DataFrame to a CSV file
df.to_csv('upcoming_concerts.csv', index=False)

print("CSV file has been created successfully.")
