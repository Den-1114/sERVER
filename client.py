import socket
import threading
import time

HEADER = 4096
HOST = socket.gethostbyname('deniz-K56CM')
PORT = 5050
ADDR = (HOST, PORT)
DISCONNECT_MESSAGE = '!DISCONNECT'
FORMAT = 'utf-8'

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def receive():
    while True:
        try:
            message = client.recv(HEADER).decode(FORMAT)
            if message:
                print(message)
        except Exception as e:
            print(f'An error occurred: {e}\nClosing connection...')
            print('Connection closed...')
            client.close()
            client.send(DISCONNECT_MESSAGE.encode(FORMAT))
            break


receive_thread = threading.Thread(target=receive)

receive_thread.start()
