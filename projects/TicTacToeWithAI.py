from random import choice


class TicTacToeWithAI:
    def __init__(self):
        self.board = []
        self.turn = 0
        self.player = ""
        self.player1 = ""
        self.player2 = ""
        self.menu()

    def menu(self):
        while (parameters := input("Input command: ")) != "exit":
            try:
                command, self.player1, self.player2 = parameters.split()
            except ValueError:
                print("Bad parameters!")
                continue
            if command == "start" and self.player1 in ["user", "easy", "medium", "hard"] \
                    and self.player2 in ["user", "easy", "medium", "hard"]:
                self.board = [[" " for _ in range(3)] for _ in range(3)]
                self.turn = 1
                self.game()
            else:
                print("Bad parameters!")

    def game(self):
        while True:
            self.print_board()
            self.player = self.x_or_o()
            x_coordinate, y_coordinate = 0, 0
            if self.player == "X":
                if self.player1 == "user":
                    x_coordinate, y_coordinate = self.user_make_move()
                elif self.player1 == "easy":
                    x_coordinate, y_coordinate = self.easy_make_move()
                elif self.player1 == "medium":
                    x_coordinate, y_coordinate = self.medium_make_move()
                elif self.player1 == "hard":
                    x_coordinate, y_coordinate = self.hard_make_move("X")
                self.board[x_coordinate][y_coordinate] = "X"
            elif self.player == "O":
                if self.player2 == "user":
                    x_coordinate, y_coordinate = self.user_make_move()
                elif self.player2 == "easy":
                    x_coordinate, y_coordinate = self.easy_make_move()
                elif self.player2 == "medium":
                    x_coordinate, y_coordinate = self.medium_make_move()
                elif self.player2 == "hard":
                    x_coordinate, y_coordinate = self.hard_make_move("O")
                self.board[x_coordinate][y_coordinate] = "O"
            game_state = self.check_result()
            if game_state == "X wins":
                self.print_board()
                print("X wins")
                break
            elif game_state == "O wins":
                self.print_board()
                print("O wins")
                break
            elif self.turn == 9:
                self.print_board()
                print("Draw")
                break
            else:
                self.turn += 1

    def x_or_o(self):
        if self.turn % 2:
            return "X"
        else:
            return "O"

    def print_board(self):
        print("---------")
        print("| {} {} {} |".format(self.board[0][0], self.board[0][1], self.board[0][2]))
        print("| {} {} {} |".format(self.board[1][0], self.board[1][1], self.board[1][2]))
        print("| {} {} {} |".format(self.board[2][0], self.board[2][1], self.board[2][2]))
        print("---------")

    def user_make_move(self):
        while True:
            try:
                x, y = input("Enter the coordinates: ").split()
            except ValueError:
                print("You should enter two numbers!")
                continue
            if not x.isdigit() or not y.isdigit():
                print("You should enter numbers!")
            elif x not in "123" or y not in "123":
                print("Coordinates should be from 1 to 3!")
            elif len(x) != 1 or len(y) != 1:
                print("Coordinates should be from 1 to 3!")
            elif self.board[int(x) - 1][int(y) - 1] != " ":
                print("This cell is occupied! Choose another one!")
            else:
                break
        return int(x) - 1, int(y) - 1

    def easy_make_move(self):
        print('Making move level "easy"')
        while True:
            x = choice([0, 1, 2])
            y = choice([0, 1, 2])
            if self.board[x][y] != " ":
                continue
            else:
                break
        return x, y

    def medium_make_move(self):
        print('Making move level "medium"')
        x, y = self.check_medium_move()
        if (x, y) != (-1, -1):
            return x, y
        else:
            while True:
                x = choice([0, 1, 2])
                y = choice([0, 1, 2])
                if self.board[x][y] != " ":
                    continue
                else:
                    break
            return x, y

    def check_medium_move(self):
        if "".join(self.board[0]) in ["XX ", "X X", " XX", "OO ", "O O", " OO"]:
            x, y = 0, self.board[0].index(" ")
        elif "".join(self.board[1]) in ["XX ", "X X", " XX", "OO ", "O O", " OO"]:
            x, y = 1, self.board[1].index(" ")
        elif "".join(self.board[2]) in ["XX ", "X X", " XX", "OO ", "O O", " OO"]:
            x, y = 2, self.board[2].index(" ")
        elif "".join([self.board[0][0], self.board[1][0], self.board[2][0]]) \
                in ["XX ", "X X", " XX", "OO ", "O O", " OO"]:
            line = [self.board[0][0], self.board[1][0], self.board[2][0]]
            x, y = line.index(" "), 0
        elif "".join([self.board[0][1], self.board[1][1], self.board[2][1]]) \
                in ["XX ", "X X", " XX", "OO ", "O O", " OO"]:
            line = [self.board[0][1], self.board[1][1], self.board[2][1]]
            x, y = line.index(" "), 1
        elif "".join([self.board[0][2], self.board[1][2], self.board[2][2]]) \
                in ["XX ", "X X", " XX", "OO ", "O O", " OO"]:
            line = [self.board[0][2], self.board[1][2], self.board[2][2]]
            x, y = line.index(" "), 2
        elif "".join([self.board[0][0], self.board[1][1], self.board[2][2]]) \
                in ["XX ", "X X", " XX", "OO ", "O O", " OO"]:
            line = [self.board[0][0], self.board[1][1], self.board[2][2]]
            x, y = line.index(" "), line.index(" ")
        elif "".join([self.board[2][0], self.board[1][1], self.board[0][2]]) \
                in ["XX ", "X X", " XX", "OO ", "O O", " OO"]:
            line = [self.board[2][0], self.board[1][1], self.board[0][2]]
            x, y = 2 - line.index(" "), line.index(" ")
        else:
            x, y = -1, -1
        return x, y

    def check_result(self):
        solutions = [self.board[0], self.board[1], self.board[2],
                     [self.board[0][0], self.board[1][0], self.board[2][0]],
                     [self.board[0][1], self.board[1][1], self.board[2][1]],
                     [self.board[0][2], self.board[1][2], self.board[2][2]],
                     [self.board[0][0], self.board[1][1], self.board[2][2]],
                     [self.board[2][0], self.board[1][1], self.board[0][2]]]
        check_solutions = [solution[0] for solution in solutions if
                           solution[0] == solution[1] == solution[2]]
        if 'X' in check_solutions:
            return 'X wins'
        elif 'O' in check_solutions:
            return 'O wins'

    def hard_make_move(self, symbol):
        print('Making move level "hard"')
        best_score = -1
        best_i = 0
        best_j = 0
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    score = self.minimax(self.board, i, j, 0, symbol)
                    if best_score == -1 or (best_score < score):
                        best_score = score
                        best_i = i
                        best_j = j
        return best_i, best_j

    def who_wins(self, fld):
        for i in range(3):
            if fld[i][0] == fld[i][1] == fld[i][2] != " ":
                return "wins"
        for i in range(3):
            if fld[0][i] == fld[1][i] == fld[2][i] != " ":
                return "wins"
        if fld[0][0] == fld[1][1] == fld[2][2] != " " or fld[0][2] == fld[1][1] == fld[2][0] != " ":
            return "wins"
        for i in range(3):
            for j in range(3):
                if fld[i][j] == " ":
                    return "game not finished"
        return "draw"

    def minimax(self, fld, cur_i, cur_j, turn, symbol):
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        for i in range(3):
            for j in range(3):
                board[i][j] = fld[i][j]
        if turn == 0:
            board[cur_i][cur_j] = symbol
        else:
            if symbol == "O":
                board[cur_i][cur_j] = "X"
            else:
                board[cur_i][cur_j] = "O"
        best_score = -1
        if self.who_wins(board) == "wins":
            if turn == 0:
                return 10
            else:
                return -10
        elif self.who_wins(board) == "draw":
            return 0
        else:
            pass
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    score = self.minimax(board, i, j, abs(turn - 1), symbol)
                    if best_score == -1 or (turn == 1 and best_score < score) or (turn == 0 and best_score > score):
                        best_score = score
        return best_score


if __name__ == '__main__':
    program = TicTacToeWithAI()
