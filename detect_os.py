import nmap

nm = nmap.PortScanner()
nm.scan(hosts='192.168.100.1/24', arguments='-O')

for host in nm.all_hosts():
    if nm[host]['status']['state'] == 'up':
        # Print the hostname, IP address, and MAC address
        print('----------------------------------------------------')
        print('Host : %s (%s)' % (host, nm[host]['hostnames'][0]['name']))
        print('State : %s' % nm[host]['status']['state'])
        print('MAC Address : %s' % nm[host]['addresses']['mac'])
        print('IP Address : %s' % nm[host]['addresses']['ipv4'])
        
        # Check if the host has an operating system detected
        if 'osmatch' in nm[host]:
            # Print the operating system details
            print('Operating System : %s' % nm[host]['osmatch'][0]['name'])
            print('Vendor : %s' % nm[host]['osmatch'][0]['osclass'][0]['vendor'])
        else:
            print('No operating system detected.')
