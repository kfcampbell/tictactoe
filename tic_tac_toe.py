#!/usr/local/bin/python
""" tic_tac_toe class:
    members: 2d list for a board, player_a_letter, player_b_letter, a string to aid in printing boards """
class tic_tac_toe():
    
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

    def print_row(self, chars):
        print("  " + str(chars[0]) + " | " + str(chars[1]) + " | " + str(chars[2]) + "  ")

    def initialize_board(self):
        self.board = [['0' for j in range(3)] for i in range(3)]

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

        # now need to check whether the number is in an empty spot on the board.
        # coords = to_coords(num) # to_coords is still in progress

        return True

    """ takes in a numeral 1-9 and returns a pair of x,y values in a list that correspond to the tic-tac-toe board coordinates """
    def to_coords(self, num):
        # probably a python dictionary would be the best way to handle this.
        return True # placeholder


    def run_loop(self):
        self.print_input_board()
        is_valid = False

        while is_valid != True:
            try:
                move_square = int(input("Enter the number for where you want to move and press the Enter key: "))
                is_valid = self.is_valid_input(move_square)
                if is_valid:
                    break
            except:
                print("Uh oh: your input isn't valid. Try again.")

        print "Out of the loop"


    """ start the actual input sequence in main """
    def main(self):
        self.initialize_board()
        print("Hello and welcome to the tic tac toe game!")
        print "You'll be " + self.player_letter + " and I'll be " + self.cpu_letter + "."

        # start the actual game.
        self.run_loop()


if __name__ == '__main__':
    game = tic_tac_toe('X', 'O')
    game.main()
