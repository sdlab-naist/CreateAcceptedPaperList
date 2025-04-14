# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# URL of the page containing accepted papers
url = "https://2024.msrconf.org/track/msr-2024-technical-papers?"

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.content, 'html.parser')

    tag = soup.find('div', id='event-overview')

    table = tag.find('table', class_='table table-condensed')

    # Find all paper titles on the page
    paper_links = table.find_all('a', {'data-event-modal': True})

    # Extract and print the paper titles
    papers = [link.contents[0].strip() for link in paper_links]

    # print("Accepted Papers:")
    for paper in papers:
        print(paper)
else:
    print("Failed to retrieve the page. Status code:", response.status_code)

