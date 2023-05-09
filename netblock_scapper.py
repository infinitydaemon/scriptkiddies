import requests
import re

def find_netblocks(country_code):
    response = requests.get(f'https://ipinfo.io/countries/{country_code}')
    html = response.content.decode('utf-8')

    pattern = r'<td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})</td>'
    matches = re.findall(pattern, html)

    return [match for match in matches]

country_code = 'US'
netblocks = find_netblocks(country_code)

for netblock in netblocks:
    print(netblock)
