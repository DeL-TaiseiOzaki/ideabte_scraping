#!/bin/bash

# Set default paths
JSON_FILE="ideabte_scraping/Get_URL_list/output/debate_topic_urls.json"
OUTPUT_DIR="ideabte_scraping/scraping_idebate/output"

# Check if the JSON file exists
if [ ! -f "$JSON_FILE" ]; then
    echo "Error: JSON file '$JSON_FILE' does not exist."
    exit 1
fi

# Create the output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

# Run the Python script
python3 ideabte_scraping/scraping_idebate/src/scraping.py "$JSON_FILE" "$OUTPUT_DIR"

echo "Scraping completed. Output files are stored in $OUTPUT_DIR"