import socket
import threading

HOST = "localhost"
PORT = 8000
separator_token = "..."

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

def receive_messages():
    while True:
        try:
            message = client.recv(1024).decode()
            print(message)
        except:
            print("An error occurred!")
            client.close()
            break

def write_messages():
    while True:
        message = f"{input('')} {separator_token}"
        client.send(message.encode())

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

write_thread = threading.Thread(target=write_messages)
write_thread.start()

