import tkinter as tk


class GUI:
    def __init__(self, root, num_players):
        self.root = root
        self.num_players = num_players
        self.root.title("Snakes and Ladders")
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        self.players = [{'name': f'Player {i + 1}', 'position': 1} for i in range(num_players)]
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
