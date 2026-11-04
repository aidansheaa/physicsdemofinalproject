import math
import tkinter as tk

current_value = tk.DoubleVar()
slider = ttk.Scale(
    root,
    from_=0,
    to=100,
    orient='horizontal',
    variable=current_value
)
