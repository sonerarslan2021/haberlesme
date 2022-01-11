import socket

SIZE = 50
SERVER = 'localhost'
PORT = 4444
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send():
    send_data = input("[client] veri girin : ")
    send_lenght = len(send_data)
    client.send(send_data.encode() + (b'' * (50 - send_lenght)))
    get_data = client.recv(50)
    print(f"[Data] GET Data : {get_data} ")


send()
