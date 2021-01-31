import random
import sqlite3

conn = sqlite3.connect('card.s3db')
cur = conn.cursor()
# cur.execute('DROP TABLE card')
# conn.commit()
cur.execute("""CREATE TABLE IF NOT EXISTS card (id INTEGER PRIMARY KEY AUTOINCREMENT, number TEXT, pin TEXT,
            balance INTEGER DEFAULT 0);""")
conn.commit()


class SimpleBankingSystem:
    def __init__(self):
        self.card_number = None
        self.card_pin = None
        self.balance = 0
        self.login_number = None
        self.login_pin = None
        self.trans_card = None
        self.trans_amount = 0

    def chooses(self):
        print("1. Create an account\n2. Log into account\n0. Exit")
        x = int(input())
        print()
        if x == 1:
            return self.create()
        elif x == 2:
            return self.log()
        elif x == 0:
            return 0

    def luhn_algorithm(self, x):
        b = list(str(x)[:-1])
        c = int(str(x)[-1])
        b = [int(b[i]) * 2 if i % 2 == 0 else int(b[i]) for i in range(len(b))]
        b = sum([x - 9 if x > 9 else x for x in b])
        z = b + c
        if z % 10 != 0:
            return 0
        else:
            return x

    def create(self):
        print("Your card has been created\nYour card number:")
        x = random.randint(4000000000000000, 4000009999999999)
        while x != self.luhn_algorithm(x):
            x = random.randint(4000000000000000, 4000009999999999)
        self.card_number = x
        print(self.card_number)
        print("Your card PIN:")
        self.card_pin = random.randint(1000, 9999)
        print(self.card_pin)
        print()
        cur.execute("INSERT INTO card (number, pin) VALUES (?, ?);", (self.card_number, self.card_pin))
        conn.commit()

    def log(self):
        self.login_number = int(input("Enter your card number:\n"))
        self.login_pin = int(input("Enter your PIN:\n"))
        print()
        cur.execute(f'SELECT * FROM card WHERE number = {self.login_number} and pin = {self.login_pin}')
        conn.commit()
        if cur.fetchone() is not None:
            print("You have successfully logged in!")
            print()
            self.logged_in()
        else:
            print("Wrong card number or PIN!")

    def logged_in(self):
        print("1. Balance\n2. Add income\n3. Do transfer\n4. Close account\n5. Log out\n0. Exit")
        x = int(input())
        print()
        if x == 1:
            cur.execute(f'SELECT balance FROM card WHERE number = {self.login_number}')
            conn.commit()
            balance = cur.fetchone()
            print('Balance:', balance)
            self.logged_in()
        elif x == 2:
            money = int(input('Enter income:\n'))
            cur.execute(f'UPDATE card SET balance = balance + {money} WHERE number = {self.login_number}')
            conn.commit()
            print('Income was added')
            self.logged_in()
        elif x == 3:
            self.trans_card = input("Transfer\nEnter card number:\n")
            if self.trans_card != self.luhn_algorithm(self.trans_card):
                print('Probably you made mistake in the card number. Please try again!')
            if self.trans_card == self.login_number:
                print("You can't transfer money to the same account!")
            cur.execute(f'SELECT * FROM card WHERE number = {self.trans_card}')
            conn.commit()
            d = cur.fetchone()
            if d is None:
                print('Such a card does not exist.')
                self.logged_in()
            elif d is not None:
                self.trans_amount = int(input('Enter how much money you want to transfer:'))
                cur.execute(f'SELECT balance FROM card WHERE number = {self.login_number}')
                conn.commit()
                if int(cur.fetchone()[0]) < self.trans_amount:
                    print('Not enough money!')
                    self.logged_in()
                else:
                    cur.execute(
                        f'UPDATE card SET balance = balance + {self.trans_amount} WHERE number = {self.trans_card}')
                    conn.commit()
                    cur.execute(
                        f'UPDATE card SET balance = balance - {self.trans_amount} WHERE number = {self.login_number}')
                    conn.commit()
                    print('Success!')
        elif x == 4:
            cur.execute(f'DELETE FROM card WHERE number = {self.login_number};')
            conn.commit()
            print('The account has been closed!')
            self.logged_in()
        elif x == 5:
            self.login_number = 0
            self.login_pin = 0
            print("You have successfully logged out!")
        elif x == 0:
            print("Bye!")
            exit()

    def main(self):
        while True:
            if self.chooses() != 0:
                continue
            else:
                break
        print("Bye!")


simple_banking_system = SimpleBankingSystem()
simple_banking_system.main()
