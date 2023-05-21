# Obtain the ID from the Google Cloud Console (https://console.cloud.google.com

import requests
from tabulate import tabulate

def search_file_on_search_engine(file_name, search_engine, api_key=None):
    search_results = []

    if search_engine == 'google':
        search_url = 'https://www.googleapis.com/customsearch/v1'
        params = {'q': f'"{file_name}"', 'cx': 'your_search_engine_id', 'key': api_key}

        try:
            response = requests.get(search_url, params=params)
            data = response.json()

            if 'items' in data:
                for item in data['items']:
                    title = item.get('title', '')
                    link = item.get('link', '')
                    search_results.append([title, link])
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while searching on Google: {str(e)}")

    # Add more search engines here with their respective APIs

    return search_results

def format_search_results(search_results):
    headers = ['Title', 'Link']
    return tabulate(search_results, headers, tablefmt='pipe')

def main():
    file_name = 'file.zip'
    search_engine = 'google'
    api_key = 'your_api_key'  # Provide your API key here

    search_results = search_file_on_search_engine(file_name, search_engine, api_key)
    formatted_results = format_search_results(search_results)
    print(formatted_results)

if __name__ == '__main__':
    main()
