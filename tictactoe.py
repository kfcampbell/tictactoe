#!/usr/local/bin/python
""" tic_tac_toe class:
    members: 2d list for a board, player_a_letter, player_b_letter, a string to aid in printing boards """
import random


class TicTacToe:
    def __init__(self, player_letter, cpu_letter):
        self.player_letter = player_letter
        self.cpu_letter = cpu_letter
        self.board = []
        self.board.append([])
        self.divide = "-------------"

    """ print the board """

    def print_board(self):
        self.print_row(self.board[0])
        print(self.divide)
        self.print_row(self.board[1])
        print(self.divide)
        self.print_row(self.board[2])

    """ print the input board so the user knows where to move """

    def print_input_board(self):
        row = [1, 2, 3]
        self.print_row(row)
        print(self.divide)
        row = [4, 5, 6]
        self.print_row(row)
        print(self.divide)
        row = [7, 8, 9]
        self.print_row(row)

    @staticmethod
    def print_row(chars):
        print("  " + str(chars[0]) + " | " + str(chars[1]) + " | " + str(chars[2]) + "  ")

    def initialize_board(self):
        self.board = [[' ' for j in range(3)] for i in range(3)]

    def is_valid_input(self, num):
        if not isinstance(num, (int)):
            print("Uh oh: your input isn't valid. Try again.")
            return False
        elif num > 9:
            print("Uh oh: your input isn't valid. Try again.")
            return False
        elif num < 1:
            print("Uh oh: your input isn't valid. Try again.")
            return False
        else:
            coords = self.to_coords(num)
            return self.check_square(coords)

    """ takes in a numeral 1-9 and returns a pair of x,y values in a list that correspond to the tic-tac-toe board coordinates """

    def to_coords(self, num):
        # not sure this is the best way to handle this.
        options = {
            1: [0, 0],
            2: [0, 1],
            3: [0, 2],
            4: [1, 0],
            5: [1, 1],
            6: [1, 2],
            7: [2, 0],
            8: [2, 1],
            9: [2, 2]
        }
        return options[num]

    def check_square(self, square):
        return self.board[square[0]][square[1]] is not self.player_letter and self.board[square[0]][
                                                                                  square[1]] is not self.cpu_letter

    def make_random_move(self):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        if self.check_square([x, y]):
            self.board[x][y] = self.cpu_letter
            return
        else:
            self.make_random_move()

    def check_winner(self):
        if self.check_winner_by_letter(self.player_letter):
            return self.player_letter
        elif self.check_winner_by_letter(self.cpu_letter):
            return self.cpu_letter
        else:
            return None

    def check_winner_by_letter(self, letter):
        # top horizontal
        if self.board[0][0] == self.board[0][1] == self.board[0][2] == letter:
            return True
        # middle horizontal
        elif self.board[1][0] == self.board[1][1] == self.board[1][2] == letter:
            return True
        # low horizontal
        elif self.board[2][0] == self.board[2][1] == self.board[2][2] == letter:
            return True
        # left vertical
        elif self.board[0][0] == self.board[1][0] == self.board[2][0] == letter:
            return True
        # middle vertical
        elif self.board[0][1] == self.board[1][1] == self.board[2][1] == letter:
            return True
        # right vertical
        elif self.board[0][2] == self.board[1][2] == self.board[2][2] == letter:
            return True
        # LR diagonal
        elif self.board[0][0] == self.board[1][1] == self.board[2][2] == letter:
            return True
        elif self.board[0][2] == self.board[1][1] == self.board[2][0] == letter:
            return True
        else:
            return False

    def run_loop(self):
        while True:
            if self.check_winner() is not None:
                break
            try:
                print "Current board: \n"
                self.print_board()
                print "\n\nInput board: \n"
                self.print_input_board()
                move_square = int(input("\nEnter the number for where you want to move and press the Enter key: "))
                is_valid = self.is_valid_input(move_square)
                if is_valid:
                    coords = self.to_coords(move_square)
                    self.board[coords[0]][coords[1]] = self.player_letter
                    if self.check_winner() is None:
                        self.make_random_move()
                        continue
                    else:
                        break
                else:
                    print("Uh oh, your input wasn't valid. Try again.")
            except:
                print("Uh oh: there was an exception and your input isn't valid. Try again.")

        print "Final game board: "
        self.print_board()

        result = self.check_winner()

        if result is self.player_letter:
            print "Congratulations, you won!"
        elif result is self.cpu_letter:
            print "Haha! I beat you!"
        else:
            print "The battle of man vs. machine was inconclusive."

    """ start the actual input sequence in main """
    def main(self):
        self.initialize_board()
        print("Hello and welcome to the tic tac toe game!")
        print "You'll be " + self.player_letter + " and I'll be " + self.cpu_letter + "."

        # start the actual game.
        self.run_loop()


if __name__ == '__main__':
    game = TicTacToe('X', 'O')
    game.main()
