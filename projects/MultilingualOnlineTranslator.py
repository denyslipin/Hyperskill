import sys
import requests
from bs4 import BeautifulSoup


class MultilingualOnlineTranslator:
    def __init__(self):
        self.languages = {'0': 'All', '1': 'Arabic', '2': 'German', '3': 'English', '4': 'Spanish', '5': 'French',
                          '6': 'Hebrew', '7': 'Japanese', '8': 'Dutch', '9': 'Polish', '10': 'Portuguese',
                          '11': 'Romanian', '12': 'Russian', '13': "Turkish"}
        self.language1 = ""
        self.language2 = ""
        self.word = ""
        self.soup = None
        self.main()

    def main(self):
        args = sys.argv
        self.language1 = args[1].title()
        x = args[2].title()
        self.word = args[3]
        if self.language1 not in self.languages.values():
            print(f"Sorry, the program doesn't support {self.language1.lower()}")
            exit()
        elif x not in self.languages.values():
            print(f"Sorry, the program doesn't support {x.lower()}")
            exit()
        elif self.language1 in self.languages.values() and x == "All":
            self.all_languages()
        elif self.language1 in self.languages.values() and x in self.languages.values():
            self.language2 = x
            self.connection()
            self.translations()
            print()
            self.examples()
            print()
            with open(f'{self.word}.txt', 'r') as f:
                lines = f.readlines()
                lines = lines[:-1]
            with open(f'{self.word}.txt', 'w') as f:
                f.writelines(lines)

    def main1(self):
        print("Hello, you're welcome to the translator.")
        print("Translator supports:\n1. Arabic\n2. German\n3. English\n4. Spanish\n5. French\n6. Hebrew")
        print("7. Japanese\n8. Dutch\n9. Polish\n10. Portuguese\n11. Romanian\n12. Russian\n13. Turkish")
        self.language1 = self.languages[input("Type the number of your language:\n")]
        x = input("Type the number of a language you want to translate to or '0' to translate to all languages:\n")
        self.word = input("Type the word you want to translate:\n")
        if x == "0":
            print()
            self.all_languages()
        else:
            self.language2 = self.languages[x]
            self.connection()
            self.translations()
            print()
            self.examples()
            print()
            with open(f'{self.word}.txt', 'r') as f:
                lines = f.readlines()
                lines = lines[:-1]
            with open(f'{self.word}.txt', 'w') as f:
                f.writelines(lines)

    def all_languages(self):
        for language in self.languages.values():
            if language != self.language1 and language != "All":
                self.language2 = language
                self.connection()
                self.translations()
                print()
                self.examples()
                print()
        with open(f'{self.word}.txt', 'r') as f:
            lines = f.readlines()
            lines = lines[:-1]
        with open(f'{self.word}.txt', 'w') as f:
            f.writelines(lines)

    def connection(self):
        language1, language2 = self.language1.lower(), self.language2.lower()
        url = f"https://context.reverso.net/translation/{language1}-{language2}/{self.word}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        page = requests.get(url, headers=headers)
        self.soup = BeautifulSoup(page.content, 'html.parser')
        trans = self.soup.find_all('a', class_='translation')
        example = self.soup.find_all('div', class_='ltr')
        if len(trans) == 1 and len(example) == 1:
            print(f"Sorry, unable to find {self.word}")
            exit()

    def translations(self):
        word_file = open(f'{self.word}.txt', 'a', encoding='utf-8')
        word_file.write(f"{self.language2} Translations:\n")
        print(f"{self.language2} Translations:")
        trans_tags = self.soup.find_all('a', class_='translation')
        trans_tags_list = []
        for i in trans_tags:
            i = i.get_text()
            trans_tags_list.append(i.strip())
        for i in range(len(trans_tags_list)):
            word_file.write(trans_tags_list[i] + "\n")
            print(trans_tags_list[i])
        word_file.write("\n")
        word_file.close()

    def examples(self):
        word_file = open(f'{self.word}.txt', 'a', encoding='utf-8')
        word_file.write(f"{self.language2} Examples\n")
        print(f"{self.language2} Examples")
        example_tags = self.soup.find_all('div', class_='ltr')
        example_tags_list = []
        for i in example_tags:
            i = i.get_text()
            example_tags_list.append(i.strip())
        for i in range(len(example_tags_list)):
            word_file.write(example_tags_list[i] + "\n")
            print(example_tags_list[i])
        word_file.write("\n")
        word_file.close()


if __name__ == '__main__':
    program = MultilingualOnlineTranslator()
