import tkinter as tk
from tkinter import messagebox

class MissionariesAndCannibals:
    def __init__(self, root):
        self.root = root
        self.root.title("Missionaries and Cannibals")

        self.canvas = tk.Canvas(root, width=800, height=400, bg="lightblue")
        self.canvas.pack()

        self.boat_side = 1  # 1 means boat on the starting side, 0 means boat on the opposite side

        # Initial state
        self.missionaries_start = 3
        self.cannibals_start = 3
        self.missionaries_end = 0
        self.cannibals_end = 0

        self.draw_scene()

        # Buttons for actions
        self.move_buttons = []
        for i in range(3):
            for j in range(3 - i):
                if 0 < i + j <= 2:
                    button = tk.Button(self.root, text=f"Move {i}M, {j}C", command=lambda i=i, j=j: self.move(i, j))
                    self.move_buttons.append(button)
                    button.pack(side=tk.LEFT)

    def draw_scene(self):
        self.canvas.delete("all")
        self.canvas.create_rectangle(0, 150, 800, 250, fill="blue")  # River

        # Boat
        boat_x = 200 if self.boat_side == 1 else 600
        self.canvas.create_rectangle(boat_x, 200, boat_x + 100, 230, fill="brown")

        # Missionaries and Cannibals on the starting side
        for i in range(self.missionaries_start):
            self.canvas.create_oval(50 + i*30, 100, 80 + i*30, 130, fill="white")
        for i in range(self.cannibals_start):
            self.canvas.create_oval(50 + i*30, 300, 80 + i*30, 330, fill="red")

        # Missionaries and Cannibals on the ending side
        for i in range(self.missionaries_end):
            self.canvas.create_oval(550 + i*30, 100, 580 + i*30, 130, fill="white")
        for i in range(self.cannibals_end):
            self.canvas.create_oval(550 + i*30, 300, 580 + i*30, 330, fill="red")

    def move(self, m, c):
        if self.boat_side == 1:
            new_m_start = self.missionaries_start - m
            new_c_start = self.cannibals_start - c
            new_m_end = self.missionaries_end + m
            new_c_end = self.cannibals_end + c
        else:
            new_m_start = self.missionaries_start + m
            new_c_start = self.cannibals_start + c
            new_m_end = self.missionaries_end - m
            new_c_end = self.cannibals_end - c

        if self.is_valid_state(new_m_start, new_c_start, new_m_end, new_c_end):
            self.missionaries_start = new_m_start
            self.cannibals_start = new_c_start
            self.missionaries_end = new_m_end
            self.cannibals_end = new_c_end
            self.boat_side = 1 - self.boat_side
            self.draw_scene()
            if self.check_win():
                messagebox.showinfo("Congratulations!", "You solved the problem!")
        else:
            messagebox.showwarning("Invalid Move", "This move is not allowed.")

    def is_valid_state(self, ms, cs, me, ce):
        # Check if counts are within valid ranges
        if ms < 0 or ms > 3 or cs < 0 or cs > 3 or me < 0 or me > 3 or ce < 0 or ce > 3:
            return False
        # Check if missionaries are not outnumbered by cannibals on either side
        if (ms > 0 and ms < cs) or (me > 0 and me < ce):
            return False
        return True

    def check_win(self):
        return self.missionaries_end == 3 and self.cannibals_end == 3

root = tk.Tk()
app = MissionariesAndCannibals(root)
root.mainloop()
