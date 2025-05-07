class Board:

    def __init__(self):
        self.board = [' ', ' ', ' ', 
                      ' ', ' ', ' ', 
                      ' ', ' ', ' ']

    def print_board(self):
        print('\n')
        print(' ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2])
        print('-----------')
        print(' ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5])
        print('-----------')
        print(' ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8])

    def update_board(self, position, type):
        # If a player selects a position, it updates the board
        if self.board[position - 1] == ' ':  
            self.board[position - 1] = type
            return True
        else:
            print('Position already selected. Select another position.')
            return False

    def check_winner(self, type):
        # If three symbols appear in a row, return True
        if (self.board[0] == type and self.board[1] == type and self.board[2] == type) or \
           (self.board[3] == type and self.board[4] == type and self.board[5] == type) or \
           (self.board[6] == type and self.board[7] == type and self.board[8] == type) or \
           (self.board[0] == type and self.board[3] == type and self.board[6] == type) or \
           (self.board[1] == type and self.board[4] == type and self.board[7] == type) or \
           (self.board[2] == type and self.board[5] == type and self.board[8] == type) or \
           (self.board[0] == type and self.board[4] == type and self.board[8] == type) or \
           (self.board[2] == type and self.board[4] == type and self.board[6] == type):
            return True
        else:
            return False

    def check_draw(self):
        # If all fields are selected and there is no winner, it's a draw
        return ' ' not in self.board

class Player:

    def __init__(self, type):
        self.type = type
        self.name = self.get_name()

    def get_name(self):
        if self.type == 'X':
            name = input('Player selecting X, enter your name: ')
        else:
            name = input('Player selecting O, enter your name: ')
        return name

class Game:

    def __init__(self):
        self.board = Board()
        self.player1 = Player('X')
        self.player2 = Player('O')
        self.current_player = self.player1

    def play(self):
        # Infinite loop to run the game until a winner is found or it's a draw
        while True:
            message = f'{self.current_player.name}, enter the position (1 - 9): '
            position = int(input(message))

            # Update the board and check if the move was valid
            if self.board.update_board(position, self.current_player.type):
                self.board.print_board()

                # Check if the current player has won
                if self.board.check_winner(self.current_player.type):
                    print(f'{self.current_player.name} wins!')
                    break

                # Check if it's a draw
                if self.board.check_draw():
                    print('The game is a draw!')
                    break

                # Switch players after a valid move
                if self.current_player == self.player1:
                    self.current_player = self.player2
                else:
                    self.current_player = self.player1

# Create and start the game
game = Game()
game.play()
