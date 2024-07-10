import requests
from bs4 import BeautifulSoup
import json
import os
import sys
from urllib.parse import urlparse
from tqdm import tqdm

def scrape_url(url, output_dir):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    topic = soup.find("h1", class_="blog-post__title").get_text(strip=True)

    points_list = []

    def extract_points(section, section_name):
        accordion_items = section.find_next_sibling('div', class_='accordion').find_all('div', class_='accordion__item')
        for item in accordion_items:
            point_subtitle = item.find('h4', class_='accordion__subtitle').get_text().strip()
            point_body = item.find('div', class_='accordion__body').find('p').get_text().strip()
            points_list.append({
                "topic": topic,
                "section": section_name,
                "context": f"**{point_subtitle}**\n{point_body}"
            })

    points_for_section = soup.find('div', class_='points-vote points-vote--for')
    if points_for_section:
        extract_points(points_for_section, "Points For")

    points_against_section = soup.find('div', class_='points-vote points-vote--against')
    if points_against_section:
        extract_points(points_against_section, "Points Against")

    # Generate a unique filename based on the URL
    parsed_url = urlparse(url)
    filename = f"{parsed_url.path.strip('/').replace('/', '_')}.json"
    output_path = os.path.join(output_dir, filename)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(points_list, f, ensure_ascii=False, indent=4)

    return output_path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <json_file> <output_dir>")
        sys.exit(1)

    json_file = sys.argv[1]
    output_dir = sys.argv[2]

    os.makedirs(output_dir, exist_ok=True)

    with open(json_file, 'r') as f:
        url_data = json.load(f)

    total_urls = sum(len(urls) for urls in url_data.values())
    
    with tqdm(total=total_urls, desc="Scraping Progress") as pbar:
        for category, urls in url_data.items():
            for url in urls:
                try:
                    output_path = scrape_url(url, output_dir)
                    pbar.set_postfix_str(f"Saved: {output_path}")
                    pbar.update(1)
                except Exception as e:
                    pbar.set_postfix_str(f"Error: {url}")
                    print(f"\nError scraping {url}: {str(e)}")
                    pbar.update(1)

    print("\nScraping completed. All data saved to the output directory.")