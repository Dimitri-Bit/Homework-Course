from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root, padding=10)
frame.grid()

input = ttk.Entry(frame, width=50)

input.grid(column=0, row=3)

def print_input_value_to_console():
    print(input.get())

label_hello_world = ttk.Label(frame, text="Hello World")
button_quit = ttk.Button(frame, text="Quit", command=root.destroy)
button_print_input = ttk.Button(frame, text="Print to console", 
                                command=print_input_value_to_console)

label_hello_world.grid(column=0, row=0)
button_quit.grid(column=0, row=1)
button_print_input.grid(column=0, row=2)

root.mainloop()
