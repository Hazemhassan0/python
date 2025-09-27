import random

class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def make_move(self, board):
        raise NotImplementedError("Subclasses must implement make_move()")

class HumanPlayer(Player):
    def make_move(self, board):
        while True:
            try:
                position = int(input(f"{self.name} ({self.symbol}), choose a position (1-9): "))
                if position < 1 or position > 9:
                    raise ValueError("Invalid position! Choose between 1 and 9.")
                if board.is_position_taken(position - 1):
                    print("Position already taken. Try again.")
                else:
                    return position - 1
            except ValueError as e:
                print(e)

class ComputerPlayer(Player):
    def make_move(self, board):
        print(f"{self.name} ({self.symbol}) is thinking...")
        available_positions = [i for i in range(9) if not board.is_position_taken(i)]
        return random.choice(available_positions)

class Board:
    def __init__(self):
        self.grid = [' ' for _ in range(9)]

    def display(self):
        print("\nBoard:")
        for i in range(0, 9, 3):
            print(f" {self.grid[i]} | {self.grid[i+1]} | {self.grid[i+2]} ")
            if i < 6:
                print("---|---|---")
        print()

    def update(self, position, symbol):
        self.grid[position] = symbol

    def is_position_taken(self, position):
        return self.grid[position] != ' '

    def check_winner(self):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  
            [0, 4, 8], [2, 4, 6]              
        ]
        for combo in winning_combinations:
            if self.grid[combo[0]] == self.grid[combo[1]] == self.grid[combo[2]] != ' ':
                return self.grid[combo[0]]  
        return None

    def is_full(self):
        return all(space != ' ' for space in self.grid)

class Game:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.board = Board()
        self.current_turn = 0

    def play(self):
        self.board.display()
        while True:
            current_player = self.players[self.current_turn]
            print(f"\n{current_player.name}'s turn ({current_player.symbol}):")
            position = current_player.make_move(self.board)
            self.board.update(position, current_player.symbol)
            self.board.display()

            winner = self.board.check_winner()
            if winner:
                print(f"{current_player.name} wins!")
                break
            elif self.board.is_full():
                print("It's a draw!")
                break

            self.switch_turns()

    def switch_turns(self):
        self.current_turn = 1 - self.current_turn

def start_game():
    print("Welcome to Tic-Tac-Toe!")
    game_mode = input("Do you want to play with a friend (type '1') or vs computer (type '2')? ")

    if game_mode == "1":
        name1 = input("Enter Player 1 name: ")
        name2 = input("Enter Player 2 name: ")
        player1 = HumanPlayer(name1, 'X')
        player2 = HumanPlayer(name2, 'O')
    elif game_mode == "2":
        name = input("Enter your name: ")
        player1 = HumanPlayer(name, 'X')
        player2 = ComputerPlayer("Computer", 'O')
    else:
        print("Invalid choice. Exiting.")
        return

    game = Game(player1, player2)
    game.play()

if __name__ == "__main__":
    start_game()
