from tkinter import *
import settings
import utils
from cell import Cell

root = Tk()
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('minesweeper game')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red', #change later
    width=utils.width_percentage(100),
    height=utils.height_percentage(20)
    )
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue',
    width=utils.width_percentage(25),
    height=utils.height_percentage(80)
)
left_frame.place(x=0,y=utils.height_percentage(20))

center_frame = Frame(
    root,
    bg='green',
    width=utils.width_percentage(75),
    height=utils.height_percentage(80)
)
center_frame.place(x=utils.width_percentage(25),y=utils.height_percentage(20))



for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell()
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
root.mainloop()
