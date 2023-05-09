# Try and grab the IP hidden behind cloudflare proxy service
import socket
import requests

target_url = "https://example.com"

# Get the Cloudflare cookie
r = requests.get(target_url)
cookie = r.cookies.get_dict()['__cfduid']

# Send a request to Cloudflare's API to get the real IP
cf_url = f"https://www.cloudflare.com/api/v4/enterprise/firewall/events?&per_page=1&direction=desc&match=all&search={cookie}"
cf_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer <YOUR_API_KEY>"
}
cf_response = requests.get(cf_url, headers=cf_headers)
cf_json = cf_response.json()
real_ip = cf_json['result'][0]['data']['source']['ip']

# Print the real IP
print("The real IP behind Cloudflare is:", real_ip)
