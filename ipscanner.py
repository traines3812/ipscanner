import socket

# Set the IP address range to scan
start_ip = "192.168.0.1"
end_ip = "192.168.0.255"

# Convert the start and end IP addresses to integers
start_int = int(socket.inet_aton(start_ip).hex(), 16)
end_int = int(socket.inet_aton(end_ip).hex(), 16)

# Loop through the IP addresses
for i in range(start_int, end_int + 1):
    # Convert the IP address to a string
    ip = socket.inet_ntoa(i.to_bytes(4, byteorder='big'))
    
    # Try to connect to each IP address
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((ip, 22))
    
    # If the connection was successful, scan the ports
    if result == 0:
        print(f"{ip} is active.")
        for port in range(1, 65535):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                result = s.connect_ex((ip, port))
                if result == 0:
                    print(f"Port {port} is open.")
                s.close()
            except:
                pass
    s.close()
