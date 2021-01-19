import random

print('H A N G M A N')
menu = input('Type "play" to play the game, "exit" to quit: ')
while menu != "exit":
    if menu != "play":
        print()
        menu = input('Type "play" to play the game, "exit" to quit: ')
    else:
        word_list = ['python', 'java', 'kotlin', 'javascript']
        word = list(random.choice(word_list))
        hidden_word = list('-' * len(word))
        lives = 8
        wrong_letters = []
        while lives > 0:
            print()
            print(''.join(hidden_word))
            if hidden_word == word:
                print("You guessed the word!")
                print("You survived!")
                break

            letter = input("Input a letter: ")

            if len(letter) > 1:
                print("You should input a single letter")
                continue

            if letter not in "abcdefghijklmnopqrstuvwxyz":
                print("Please enter a lowercase English letter")
                continue

            if letter not in word:
                if letter not in wrong_letters:
                    print("That letter doesn't appear in the word")
                    wrong_letters.append(letter)
                    lives -= 1
                else:
                    print("You've already guessed this letter")
            else:
                if letter not in hidden_word:
                    for i in range(len(word)):
                        if word[i] == letter:
                            hidden_word[i] = letter
                else:
                    print("You've already guessed this letter")
        if hidden_word != word:
            print("You lost!")
        print()
        menu = input('Type "play" to play the game, "exit" to quit: ')
