from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()


m = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]]
martix_of_inputs = []

for i in range(0,9):
    row_of_inputs = []
    for j in range(0,9):
        input = ttk.Entry(frame, width=4) # make it almost a square
        input.grid(column=j, row=i)
        input.insert(0, m[i][j]) # set initial value from the m
        row_of_inputs.append(input)
    martix_of_inputs.append(row_of_inputs)

root.mainloop()