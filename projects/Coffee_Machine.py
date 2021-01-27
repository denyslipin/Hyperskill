water = 400
milk = 540
beans = 120
cups = 9
money = 550

def coffee_machine_has():
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{beans} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")

def write_action():
    action = input("Write action (buy, fill, take, remaining, exit):\n")
    print()
    if action == "remaining":
        return coffee_machine_has()
    elif action == "buy":
        return buy()
    elif action == "fill":
        return fill()
    elif action == "take":
        return take()
    elif action == "exit":
        return "exit"

def buy():
    coffee = input("What do you want to buy? 1 - espresso, \
                    2 - latte, 3 - cappuccino, back - to main menu:\n")
    if coffee == "back":
        print()
    elif int(coffee) == 1:
        make_coffee(250, 0, 16, 1, 4)
    elif int(coffee) == 2:
        make_coffee(350, 75, 20, 1, 7)
    elif int(coffee) == 3:
        make_coffee(200, 100, 12, 1, 6)

def make_coffee(w, m, b, c, p):
    global water, milk, beans, cups, money
    water1 = water - w
    milk1 = milk - m
    beans1 = beans - b
    cups1 = cups - c
    if water1 > 0 and milk1 > 0 and beans1 > 0 and cups1 > 0:
        water -= w
        milk -= m
        beans -= b
        cups -= c
        money += p
        print("I have enough resources, making you a coffee!")
        print()
        return water, milk, beans, cups, money
    else:
        if water < w:
            print("Sorry, not enough water!")
        elif milk < m:
            print("Sorry, not enough milk!")
        elif beans < b:
            print("Sorry, not enough beans!")
        elif cups < c:
            print("Sorry, not enough cups!")
    print()

def fill():
    global water, milk, beans, cups
    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    beans += int(input("Write how many grams of coffee beans \
                        do you want to add:\n"))
    cups += int(input("Write how many disposable cups of coffee \
                       do you want to add:\n"))
    print()
    return water, milk, beans, cups

def take():
    global money
    print(f"I gave you ${money}")
    print()
    money -= money
    return money

def main():
    write_action()
    while write_action() != "exit":
        write_action()

main()
