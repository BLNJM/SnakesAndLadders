import tkinter as tk


class GUI:
    def __init__(self, root, num_players):
        self.root = root
        self.num_players = num_players
        self.root.title("Snakes and Ladders")
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        

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
