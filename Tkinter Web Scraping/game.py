from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup


sudoku_page = requests.get("http://west.websudoku.com/")
soup = BeautifulSoup(sudoku_page.content, 'html.parser')
board = [[0 for element in range(9)] for row in range(9)] # pravi matricu nula
for i in range(9):
    for j in range(9):
        cell_id = f"f{i}{j}"
        cell = soup.find("input", id=cell_id)
        if cell and "readonly" in cell.attrs:
            board[i][j] = int(cell["value"])
        else:
            board[i][j] = 0


root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()
martix_of_inputs = []

def on_key_release(event, row, col):
    print(row, col)
    print(event.widget.get())
    board[row,col] = event.widget.get()

for i in range(0,9):
    row_of_inputs = []
    for j in range(0,9):
        input = ttk.Entry(frame, width=4)
        input.grid(column=j, row=i)
        input.bind("<KeyRelease>", lambda event, row=i, col=j: on_key_release(event, row, col))
        if not board[i][j] == 0:
            input.insert(0, board[i][j])
        row_of_inputs.append(input)
    martix_of_inputs.append(row_of_inputs)

root.mainloop()
