# write your code here
import itertools
import sys
import socket
import string


def password_generator():
    letters_list = list(string.ascii_lowercase)
    numbers_list = list(range(10))
    the_list = letters_list + numbers_list
    for i in range(1, len(the_list) + 1):
        combinations = itertools.product(the_list, repeat=i)
        for j in combinations:
            password = ''
            for k in j:
                password += str(k)
            yield password


args = sys.argv
hostname = args[1]
port = int(args[2])

with socket.socket() as client_socket:
    address = (hostname, port)
    client_socket.connect(address)
    attempt = password_generator()

    for j in attempt:
        data = j.encode('utf-8')
        client_socket.send(data)
        response = client_socket.recv(1024)
        response = response.decode('utf-8')
        if response == 'Connection success!':
            print(j)
            client_socket.close()
            break
