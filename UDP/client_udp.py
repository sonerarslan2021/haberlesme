import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b'merhaba server', ('localhost', 4444))
data, addr = client.recvfrom(64)
print(f"server {addr} : ", data)
