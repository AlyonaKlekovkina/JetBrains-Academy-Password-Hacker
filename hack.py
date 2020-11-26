# write your code here
import sys
import socket

args = sys.argv
hostname = args[1]
port = int(args[2])
msg_to_send = args[3]

with socket.socket() as client_socket:
    address = (hostname, port)

    client_socket.connect(address)

    data = msg_to_send.encode()

    client_socket.send(data)

    response = client_socket.recv(1024)

    response = response.decode()
    print(response)
