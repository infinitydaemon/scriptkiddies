import nmap

# Define the IP range to scan
ip_range = '192.168.1.1/24'

# Initialize the nmap scanner
nm = nmap.PortScanner()

# Scan the network range
nm.scan(hosts=ip_range, arguments='-p 22 --open')

# Check the scan results for Raspberry Pi devices
for host in nm.all_hosts():
    if 'raspberry pi' in nm[host]['vendor'].lower():
        print(f"Found Raspberry Pi at {host}")
