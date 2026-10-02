import socket

# Enter the system address
host = input("Enter system/IP address: ")

# Enter the port number
port = int(input("Enter port number: "))

# Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(2)

# Check the port
result = sock.connect_ex((host, port))

print("\n--- Port Status ---")

if result == 0:
    print("Port", port, "is OPEN")
else:
    print("Port", port, "is CLOSED or FILTERED")

sock.close()
