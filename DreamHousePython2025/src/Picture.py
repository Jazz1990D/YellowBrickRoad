import tkinter as tk
from tkinter import ttk
from Square import Square
from Triangle import Triangle
from Circle import Circle
from Rectangle import Rectangle

class Picture:
    def __init__(self, root=None):
        self.root = root
        self.root.title("House Drawing Application")
        self.root.geometry("800x600")

        # Create main frame
        main_frame = ttk.Frame(root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create canvas for drawing
        self.canvas = tk.Canvas(main_frame, width=600, height=400, bg='salmon1')
        self.canvas.pack(side=tk.LEFT, padx=(0, 10))

        self.wall = None
        self.window = None
        self.roof = None
        self.sun = None
        self.moon = None
        self.door = None
        self.draw()

    def draw(self):
        self.wall = Square(canvas=self.canvas, size=200, color="yellow", fill="pink", line=2)
        self.wall.move_horizontal(50)
        self.wall.move_vertical(75)
        self.wall.make_visible()

        self.door = Rectangle(canvas=self.canvas, height=20, width=100, color="blue", fill="pink", line=2)
        self.door.move_horizontal(154)
        self.door.move_vertical(175)
        self.door.make_visible()

        self.window = Square(canvas=self.canvas, size=65, color="yellow", fill="yellow", line=1)
        self.window.move_horizontal(70)
        self.window.move_vertical(100)
        self.window.make_visible()

        self.door = Square(canvas=self.canvas, size=65, color="black", fill="white", line=2)
        self.door.move_horizontal(160)
        self.door.move_vertical(200)
        self.door.make_visible()

        self.roof = Triangle(canvas=self.canvas, height=125, width=200, color="green", fill="green", line=2)
        self.roof.move_horizontal(60)
        self.roof.move_vertical(107)
        self.roof.make_visible()

        self.sun = Circle(canvas=self.canvas, diameter=60, color="yellow", fill="yellow", line=1)
        self.sun.move_horizontal(400)
        self.sun.move_vertical(-10)
        self.sun.make_visible()

    def set_black_and_white(self):
        if self.wall:
            self.wall.change_color("black")
            self.window.change_color("white")
            self.roof.change_color("black")
            self.sun.change_color("black")

    def set_color(self):
        if self.wall:
            self.wall.change_color("black")
            self.window.change_color("black")
            self.roof.change_color("green")
            self.sun.change_color("yellow")
