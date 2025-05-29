# Africa Companies Scraper

This project scrapes data from the Wikipedia page listing the largest companies in Africa by revenue. It extracts the data from the HTML table on the page and saves it as a CSV file for further analysis or usage.

## Features

- Scrapes structured data from a Wikipedia table
- Cleans and stores the data in a Pandas DataFrame
- Exports the data to a CSV file (`africa_companies.csv`)

## How It Works

1. Sends a request to the Wikipedia page
2. Parses the HTML with BeautifulSoup
3. Locates the desired table
4. Extracts column headers and row data
5. Stores the data in a DataFrame
6. Exports the data as a CSV file

## Setup

1. Clone this repository or download the script.
2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python -m venv scraper_env
   source scraper_env/bin/activate  # On Windows: scraper_env\Scripts\activate
