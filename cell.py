from tkinter import Button
from random import sample
import settings
class Cell:
    all = []
    def __init__(self,x ,y, is_mine=False):
        self.is_mine=is_mine
        self.cell_btn_object = None
        self.x=x
        self.y=y
        #Append the obj to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=3
        )
        btn.bind('<Button-1>', self.left_click_actions) #<Button-1> means left click
        btn.bind('<Button-3>', self.right_click_actions) #<Button-3> means right click
        self.cell_btn_object = btn
        
    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()

    def get_cell_by_axis(self, x, y):
        #Return a cell obj based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
            
    def show_mine(cell):
        cell.cell_btn_object.configure(bg='red')

    def show_cell(self):
        surrounding_cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        print(surrounding_cells)

    def right_click_actions(self, event):
        print(event)
        print("I am right clicked")

    @staticmethod
    def randomize_mines():
        picked_cells = sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"