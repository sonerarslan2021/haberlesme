"""
https://www.youtube.com/watch?v=5VQpMTN0aL4

"""


import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 4444))

while True:
    data, addr = server.recvfrom(64)
    print(f"client {addr} ; ", data)
    server.sendto(b"merhaba client", addr)
