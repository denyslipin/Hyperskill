def print_board():
    """ Print the current state of the board. """
    print("---------")
    print("| {} {} {} |".format(board[0][0], board[0][1], board[0][2]))
    print("| {} {} {} |".format(board[1][0], board[1][1], board[1][2]))
    print("| {} {} {} |".format(board[2][0], board[2][1], board[2][2]))
    print("---------")

def make_move():
    while True:
        try:
            x, y = input("Enter coordinates separated by space: ").split(" ")
        except ValueError:
            print("You should enter two numbers!")
            continue
        if not x.isdigit() or not y.isdigit():
            print("You should enter numbers!")
        elif x not in "123" or y not in "123":
            print("Coordinates should be from 1 to 3!")
        elif len(x) != 1 or len(y) != 1:
            print("Coordinates should be from 1 to 3!")
        elif board[int(x) - 1][int(y) - 1] != " ":
            print("This cell is occupied! Choose another one!")
        else:
            break
    x = int(x) - 1
    y = int(y) - 1
    return x, y

def x_or_o(turn):
    """ Return 'X' if it's X's turn. Return 'O' if it's O's turn. """
    if turn % 2:
        return "X"
    else:
        return "O"

def check_result():
    """ Check the state of the board to see if someone has won the game. """
    solutions = [board[0], board[1], board[2],
                [board[0][0], board[1][0], board[2][0]],
                [board[0][1], board[1][1], board[2][1]],
                [board[0][2], board[1][2], board[2][2]],
                [board[0][0], board[1][1], board[2][2]],
                [board[2][0], board[1][1], board[0][2]] ]
    check_solutions = [solution[0] for solution in solutions if
                       solution[0] == solution[1] == solution[2] ]
    if 'X' in check_solutions:
        return 'X wins'
    elif 'O' in check_solutions:
        return 'O wins'

# Board is an empty 3x3 matrix.
board = [[" " for i in range(3)] for i in range(3)]
turn = 1

# Start of game.
while True:
    print_board()
    x_coordinate, y_coordinate = make_move()
    board[x_coordinate][y_coordinate] = x_or_o(turn)
    game_state = check_result()
    if game_state == "X wins":
        print_board()
        print("X wins")
        break
    elif game_state == "O wins":
        print_board()
        print("O wins")
        break
    elif turn == 9:
        print_board()
        print("Draw")
        break
    else:
        turn += 1
