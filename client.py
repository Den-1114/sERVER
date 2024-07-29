import socket
import threading

HEADER = 4096
HOST = 'green-mixing.gl.at.ply.gg'
PORT = 36217
ADDR = (HOST, PORT)
DISCONNECT_MESSAGE = '!DISCONNECT'
MINECRAFT_LOCAL_IP_COMMAND = '!IP'
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
            client.close()
            break

def write():
    while True:
        message = input()
        send(message)
        if message == DISCONNECT_MESSAGE:
            break

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

receive_thread = threading.Thread(target=receive)
write_thread = threading.Thread(target=write)

receive_thread.start()
write_thread.start()
