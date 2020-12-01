# write your code here
import itertools
import sys
import socket

list_of_passwords = []
with open('/Users/alyona/PycharmProjects/Password Hacker/Password Hacker/task/hacking/passwords.txt', 'r', encoding='utf-8') as f:
    for line in f:
        list_of_passwords.append(line.strip())


def password_generator(the_list):
    for word in the_list:
        if not word.isdigit():
            combinations = itertools.product(*([letter.lower(), letter.upper()] for letter in word))
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
    attempt = password_generator(list_of_passwords)

    for j in attempt:
        data = j.encode('utf-8')
        client_socket.send(data)
        response = client_socket.recv(1024)
        response = response.decode('utf-8')
        if response == 'Connection success!':
            print(j)
            client_socket.close()
            break
