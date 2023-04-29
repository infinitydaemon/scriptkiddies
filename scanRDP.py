import socket

def scan_ports(ip, start_port, end_port):
    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} is open on {ip}!")
        sock.close()

def scan_ips(start_ip, end_ip, start_port, end_port):
    start_ip_parts = start_ip.split(".")
    end_ip_parts = end_ip.split(".")
    for a in range(int(start_ip_parts[0]), int(end_ip_parts[0]) + 1):
        for b in range(int(start_ip_parts[1]), int(end_ip_parts[1]) + 1):
            for c in range(int(start_ip_parts[2]), int(end_ip_parts[2]) + 1):
                for d in range(int(start_ip_parts[3]), int(end_ip_parts[3]) + 1):
                    ip = f"{a}.{b}.{c}.{d}"
                    scan_ports(ip, start_port, end_port)

scan_ips("10.0.0.1", "10.0.0.255", 3389, 3389)
print("Here is the list from specifed range")
