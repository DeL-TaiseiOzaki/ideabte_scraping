import json
import requests
from bs4 import BeautifulSoup

# Load URLs from JSON file
with open('ideabte_scraping/Get_URL_list/URL_json_output/debate_urls.json', 'r') as f:
    json_urls = json.load(f)

# Function to get sub-page URLs from a main theme URL
def get_debate_topic_urls(main_url):
    response = requests.get(main_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all links from the main URL page
    links = soup.find_all('a', href=True)
    
    # Filter for links that are debate topics
    topic_urls = [link['href'] for link in links if link['href'].startswith('/')]
    
    # Make URLs absolute
    full_urls = [f"https://idebate.net{url}" for url in topic_urls if "~b" in url]
    
    return full_urls

# Dictionary to store all debate topic URLs for each main theme URL
all_debate_topic_urls = {}
for theme_url in json_urls:
    theme_name = theme_url.split("/")[-2].replace("~", "_")
    all_debate_topic_urls[theme_name] = get_debate_topic_urls(theme_url)

# Output the results
with open('ideabte_scraping/Get_URL_list/output/debate_topic_urls.json', 'w') as f:
    json.dump(all_debate_topic_urls, f, indent=4)

print("Debate topic URLs have been saved to debate_topic_urls.json")