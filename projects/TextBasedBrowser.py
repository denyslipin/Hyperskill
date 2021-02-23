import os
import requests
from sys import argv
from bs4 import BeautifulSoup
from colorama import Fore


class TextBasedBrowser:
    def __init__(self):
        self.directory_name = argv[1]
        self.my_stack = []
        self.create_directory()
        self.main()

    def main(self):
        while True:
            user_input = input()
            if user_input == 'exit':
                break
            elif user_input == 'back':
                self.back()
            else:
                self.check(user_input)

    def back(self):
        if len(self.my_stack) > 0:
            self.my_stack.pop()
            if len(self.my_stack) > 0:
                file_name = self.my_stack.pop()
                self.read_from_file(file_name)
            else:
                return 0
        else:
            return 0

    def check(self, user_input):
        if os.path.exists(f"{self.directory_name}/{user_input}"):
            self.read_from_file(user_input)
        elif "." in user_input:
            url = user_input
            if "http://" not in url:
                url = "http://" + url
            r = requests.get(url)
            soup = BeautifulSoup(r.content, 'html.parser')
            to_print = ""
            for tag in soup.find_all(["a", "p", "head", "ul", "ol", "li"]):
                if tag.name == "a":
                    to_print += tag.text.strip() + "\n"
                    print(Fore.BLUE + to_print)
                else:
                    to_print += tag.text.strip() + "\n"
            file_name = '.'.join(user_input.split('.')[:-1])
            if 'www.' in file_name:
                file_name = file_name[4:]
            self.write_to_file(file_name, to_print)
            self.my_stack.append(file_name)
            print(to_print)
        else:
            print("Error: Incorrect URL")

    def create_directory(self):
        if not os.path.isdir(self.directory_name):
            os.mkdir(self.directory_name)

    def write_to_file(self, file_name, content):
        with open(f"{self.directory_name}/{file_name}", "w",
                  encoding="utf-8") as file:
            file.write(content)

    def read_from_file(self, file_name):
        with open(f"{self.directory_name}/{file_name}") as file:
            print(file.read())


if __name__ == '__main__':
    program = TextBasedBrowser()
