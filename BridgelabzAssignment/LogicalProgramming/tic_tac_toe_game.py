import random

board = {}
for i in range(1, 10):
    board.__setitem__(i, " ")

win_list = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 5, 9), (3, 5, 7), (1, 4, 7), (2, 5, 8), (3, 6, 9)]

print("Hello and welcome to tic tac toe game!!!!")


def comp_turn():
    comp_option = random.randint(1, 9)
    if board[comp_option] == ' ':
        board[comp_option] = '0'
        return
    comp_turn()


def user_turn():
    option = int(input("Enter Position:"))
    if board[option] == ' ':
        board[option] = 'X'
        return
    user_turn()


def display():
    print(f"{board[1]} {board[2]} {board[3]}\n{board[4]} {board[5]} {board[6]}\n{board[7]} {board[8]} {board[9]}")


def main():
    try:
        while True:
            display()
            user_turn()
            comp_turn()
            for i in win_list:
                if board[i[0]] == 'X' and board[i[1]] == 'X' and board[i[2]] == 'X':
                    print("You Win!!!")
                    display()
                    return
                if board[i[0]] == '0' and board[i[1]] == '0' and board[i[2]] == '0':
                    print("Comp Win!!!")
                    display()
                    return
    except ValueError:
        print("invalid input from user")


if __name__ == "__main__":
    main()





"""
import random

class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self):
        try:
            for i in range(3):
                row = []
                for j in range(3):
                    row.append('-')
                self.board.append(row)
        except ValueError:
            print("invalid literals")

    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_spot(self, row, col, player):
        self.board[row][col] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        try:
            self.create_board()

            player = 'X' if self.get_random_first_player() == 1 else 'O'
            while True:
                print(f"Player {player} turn")

                self.show_board()

                # taking user input
                row, col = list(
                    map(int, input("Enter row and column numbers to fix spot: ").split()))
                print()

                # fixing the spot
                self.fix_spot(row - 1, col - 1, player)

                # checking whether current player is won or not
                if self.is_player_win(player):
                    print(f"Player {player} wins the game!")
                    break

                # checking whether the game is draw or not
                if self.is_board_filled():
                    print("Match Draw!")
                    break

                # swapping the turn
                player = self.swap_player_turn(player)

            # showing the final view of board
            print()
            self.show_board()
        except ValueError:
            print("invalid literals")


# starting the game
tic_tac = TicTacToe()
tic_tac.start()

"""
