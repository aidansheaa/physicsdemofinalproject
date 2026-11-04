import math
import tkinter as tk


t = 0
gravity = 9.8

#massslider
current_value = tk.DoubleVar()
slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    variable=current_value)

#initalangleslider
current_value2 = tk.DoubleVar()
slider2 = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    variable=current_value)

#initialvelocityslider 
current_value3 = tk.DoubleVar()
slider3 = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    variable=current_value)
