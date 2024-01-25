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
    bg='black', #change later
    width=utils.width_percentage(100),
    height=utils.height_percentage(20)
    )
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 30)
)

game_title.place(
    x=utils.width_percentage(25), y=0
)
left_frame = Frame(
    root,
    bg='black',
    width=utils.width_percentage(25),
    height=utils.height_percentage(80)
)
left_frame.place(x=0,y=utils.height_percentage(20))

center_frame = Frame(
    root,
    bg='black',
    width=utils.width_percentage(75),
    height=utils.height_percentage(80)
)
center_frame.place(x=utils.width_percentage(25),y=utils.height_percentage(20))



for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
#Call the label
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
Cell.randomize_mines() 
root.mainloop()
