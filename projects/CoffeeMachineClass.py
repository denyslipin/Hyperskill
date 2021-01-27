class CoffeeMachine:
    def __init__(self, water=400, milk=540, beans=120, cups=9, money=550):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

    def coffee_machine_has(self):
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")

    def write_action(self):
        action = input("Write action (buy, fill, take, remaining, exit):\n")
        print()
        if action == "remaining":
            return self.coffee_machine_has()
        elif action == "buy":
            return self.buy()
        elif action == "fill":
            return self.fill()
        elif action == "take":
            return self.take()
        elif action == "exit":
            return "exit"

    def buy(self):
        print("What do you want to buy? 1 - espresso, \
               2 - latte, 3 - cappuccino, back - to main menu:")
        coffee = input()
        if coffee == "back":
            print()
        elif int(coffee) == 1:
            self.make_coffee(250, 0, 16, 1, 4)
        elif int(coffee) == 2:
            self.make_coffee(350, 75, 20, 1, 7)
        elif int(coffee) == 3:
            self.make_coffee(200, 100, 12, 1, 6)

    def make_coffee(self, w, m, b, c, p):
        water1 = self.water - w
        milk1 = self.milk - m
        beans1 = self.beans - b
        cups1 = self.cups - c
        if water1 > 0 and milk1 > 0 and beans1 > 0 and cups1 > 0:
            self.water -= w
            self.milk -= m
            self.beans -= b
            self.cups -= c
            self.money += p
            print("I have enough resources, making you a coffee!")
            print()
            return self.water, self.milk, self.beans, self.cups, self.money
        else:
            if self.water < w:
                print("Sorry, not enough water!")
            elif self.milk < m:
                print("Sorry, not enough milk!")
            elif self.beans < b:
                print("Sorry, not enough beans!")
            elif self.cups < c:
                print("Sorry, not enough cups!")
        print()

    def fill(self):
        self.water += int(input("Write how many ml of water \
                                do you want to add:\n"))
        self.milk += int(input("Write how many ml of milk \
                                do you want to add:\n"))
        self.beans += int(input("Write how many grams of coffee beans \
                                do you want to add:\n"))
        self.cups += int(input("Write how many disposable cups of coffee \
                                do you want to add:\n"))
        print()
        return self.water, self.milk, self.beans, self.cups

    def take(self):
        print(f"I gave you ${self.money}")
        print()
        self.money -= self.money
        return self.money

    def main(self):
        self.write_action()
        while self.write_action() != "exit":
            self.write_action()

coffee = CoffeeMachine()
coffee.main()
