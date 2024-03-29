from tkinter import Button, Label
from random import sample
import settings
import ctypes
import sys

class Cell:
    all = []
    cell_count_label_object = None
    cell_count = settings.CELL_COUNT
    def __init__(self,x ,y, is_mine=False):
        self.is_mine=is_mine
        self.cell_btn_object = None
        self.x=x
        self.y=y
        self.is_opened = False
        self.is_mine_candidate = False
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
            if self.surrounded_cells_mines_length == 0:
                for cell_object in self.surrounded_cells():
                    cell_object.show_cell()
            self.show_cell()
        self.cell_btn_object.config(state='disabled')
        self.cell_btn_object.unbind('<Button-3>')


    def get_cell_by_axis(self, x, y):
        #Return a cell obj based on the value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
            
    def show_mine(cell):
        cell.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(
            0, 'You clicked on a mine!', 'Game Over', 0
            )
        sys.exit()
    
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells


    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells():
            if cell.is_mine:
                counter+=1
        return counter

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
    
    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            #Replace the test of cell count label with newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                    text=f'Cells left:{Cell.cell_count}'
                    )
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )
        
        self.is_opened = True

    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            text=f"Cells Left:{Cell.cell_count}",
            bg='black',
            fg='white',
            width=12,
            height=4,
            font=("", 16)
        )
        Cell.cell_count_label_object = label
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"