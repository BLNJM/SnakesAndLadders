import tkinter as tk


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Snakes and Ladders")
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()
        

if __name__ == "__main__":
    root = tk.Tk()
    game = GUI(root)
    root.mainloop()
