import random

class RockPaperScissors:

    def __init__(self):
        self.score = 0
        self.name = input('Enter your name:')
        self.list_game = ["rock", "paper", "scissors"]

    def main(self):
        print(f'Hello, {self.name}')
        fhand = open('rating.txt')
        for line in fhand:
            if self.name == line.split()[0]:
                self.score = int(line.split()[1])
        x = input().split(',')
        if len(x) > 1:
            self.list_game = x
        print("Okay, let's start")
        self.game()

    def game(self):
        while True:
            choice = input()
            if choice == '!exit':
                print('Bye!')
                break
            if choice == '!rating':
                print(f'Your rating: {self.score}')
                continue
            if choice not in self.list_game:
                print('Invalid input')
                continue
            x = self.list_game.index(choice)
            new_list_game = (self.list_game[x:] + self.list_game[:x])[1:]
            win_list_game = new_list_game[:len(new_list_game) // 2]
            loose_list_game = new_list_game[len(new_list_game) // 2:]
            cpu_choice = random.choice(self.list_game)
            if choice == cpu_choice:
                print(f'There is a draw ({cpu_choice})')
                self.score += 50
            elif cpu_choice in loose_list_game:
                print(f'Well done. The computer chose {cpu_choice} and failed')
                self.score += 100
            elif cpu_choice in win_list_game:
                print(f'Sorry, but the computer chose {cpu_choice}')


game = RockPaperScissors()
game.main()
