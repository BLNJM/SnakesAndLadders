import random
import tkinter as tk


class GUI:
    def __init__(self, root, num_players):
        self.root = root
        self.num_players = num_players
        self.root.title("Snakes and Ladders")
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.players = [{'name': f'Player {i + 1}', 'position': 1} for i in range(num_players)]
        self.current_player = 0

        # assign the snakes and the ladders; left is starting position and right is ending position
        self.board = {
            9: 4,
            13: 25,
            16: 5,
            19: 29,
            27: 20,
            39: 11,
            42: 59,
            46: 33,
            52: 29,
            57: 66,
            64: 50,
            77: 44,
            83: 73,
            91: 75,
        }

        # dice roll button
        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

        # current dice roll label
        self.roll_label = tk.Label(root, text="")
        self.roll_label.pack()

        # current player status label
        self.turn_label = tk.Label(root, text="Welcome to Snakes and Ladders. Player 1's turn")
        self.turn_label.pack()

        self.draw_board()

    def draw_board(self):
        self.canvas.delete("all")
        # draw all the numbers on the board, including the snakes and ladders
        for i in range(10):
            for j in range(10):
                x = j * 50
                y = (9 - i) * 50
                pos = i * 10 + j + 1
                if pos in self.board:
                    target = self.board[pos]
                    self.canvas.create_text(x + 30, y + 20, text=f"{pos}->{target}")
                else:
                    self.canvas.create_text(x + 30, y + 20, text=pos)
        # draw circles around the current positions of each player
        for player in self.players:
            x = ((player['position'] - 1) % 10) * 50
            y = (9 - (player['position'] - 1) // 10) * 50
            self.canvas.create_oval(x + 15, y + 5, x + 45, y + 35, outline="red")

    def roll_dice(self):
        self.move_player(random.randint(1, 6))
        self.update()

    def move_player(self, distance):
        # move the player
        player = self.players[self.current_player]
        player['position'] += distance
        if player['position'] > 100:
            player['position'] = 100

        # the player has landed on a snake/ladder; move them accordingly
        if player['position'] in self.board:
            player['position'] = self.board[player['position']]

        self.roll_label.config(text=f"{player['name']} rolled a {distance} and is now at tile {player['position']}!")

        # declare a winning player and end the game
        if player['position'] == 100:
            self.turn_label.config(text=f"{player['name']} wins!")
            self.roll_button.config(state="disabled")

        self.current_player += 1
        if self.current_player is num_players:
            self.current_player = 0

    # updates the status label and redraws the board
    def update(self):
        player = self.players[self.current_player]
        self.turn_label.config(text=f"{player['name']}'s turn")
        self.draw_board()


if __name__ == "__main__":

    num_players = 0

    # ask the user for the player count
    while True:
        try:
            num_players = int(input("Enter the player count: "))

            # only accept answer if it is valid (an integer >= 2)
            if num_players < 2:
                print("At least 2 players are required")
            if isinstance(num_players, int) and num_players > 1:
                break
        except ValueError:
            # only accept answer if it is an integer
            print("Invalid response, please enter the number of players")

    root = tk.Tk()
    game = GUI(root, num_players)
    root.mainloop()
