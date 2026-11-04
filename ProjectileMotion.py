import math
import tkinter as tk
from tkinter import ttk
import pyplot as plt

#constants
tinitial = 0.0
gravity = 9.8
initialposition = [0, 0, 0]
acceleration = [0, -(gravity), 0]

#sliders
mass = root = Tk()  
root.geometry("400x300") 

v1 = DoubleVar()

def show1():  
    
    sel = "Horizontal Scale Value = " + str(v1.get())
    l1.config(text = sel, font =("Courier", 14))  


s1 = Scale( root, variable = v1, 
           from_ = 1, to = 100, 
           orient = HORIZONTAL)   

l3 = Label(root, text = "Horizontal Scaler")

b1 = Button(root, text ="Display Horizontal", 
            command = show1, 
            bg = "yellow")  

l1 = Label(root)


s1.pack(anchor = CENTER) 
l3.pack()
b1.pack(anchor = CENTER)
l1.pack() 

root.mainloop()


initialangle = 

initialvelocityval  = 


#equations 
intialvelocity = [(initialvelocityval) * math.cos(initialangle), (initialvelocityval) * math.sin(initialangle), 0 ]
finalpositionx = initialposition(0) + initialvelocity(0) * tfinal + (1/2) * (acceleration(0)) * (tfinal**2)
finalvelocityx = initialvelocity(0) + (acceleration(0)) * (tfinal)
finalpositiony = initialposition(1) + initialvelocity(1) * tfinal + (1/2) * (acceleration(1)) * (tfinal**2)
finalvelocityy = initialvelocity(1) + (acceleration(1)) * (tfinal)

distancex = finalpositionx - initialposition(0)
distancey = finalpositiony - initialposition(1)

while positionx > 0 or positiony > 0:
    

#graphing
plt.plot(x, y)
plt.title('Graph of Projectile Motion')
plt.xlabel('Horizontal distance')
plt.ylabel('Vertical Distance')
plt.grid(True)
plt.show()
