import requests


class CurrencyConverter:
    def __init__(self):
        self.code = ""
        self.page = None
        self.cache = {}
        self.currency_code()
        self.exchange()

    def currency_code(self):
        self.code = input().lower()
        self.page = requests.get(f"http://www.floatrates.com/daily/{self.code}.json")
        self.page = self.page.json()
        if self.code == "usd":
            self.cache["eur"] = self.page["eur"]["rate"]
        elif self.code == "eur":
            self.cache["usd"] = self.page["usd"]["rate"]
        else:
            self.cache["usd"] = self.page["usd"]["rate"]
            self.cache["eur"] = self.page["eur"]["rate"]

    def exchange(self):
        while True:
            currency = input().lower()
            if currency != "":
                amount = int(input())
                if currency in self.cache:
                    print("Checking the cache…")
                    print("Oh! It is in the cache!")
                    received = round(amount * self.cache[currency], 2)
                    print(f"You received {received} {self.code.upper()}.")
                else:
                    print("Checking the cache…")
                    print("Sorry, but it is not in the cache!")
                    self.cache[currency] = self.page[currency]["rate"]
                    received = round(amount * self.cache[currency], 2)
                    print(f"You received {received} {self.code.upper()}.")
            else:
                break


if __name__ == '__main__':
    program = CurrencyConverter()
