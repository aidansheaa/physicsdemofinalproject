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
mass = 

initialangle = 

initialvelocityval  = 


#equations 
intialvelocity = [(initialvelocityval) * math.cos(initialangle), (initialvelocityval) * math.sin(initialangle), 0 ]
finalpositionx = initialposition(0) + initialvelocity(0) * tfinal + (1/2) * (acceleration(0)) * (tfinal**2)
finalvelocityx = initialvelocity(0) + (acceleration(0)) * (tfinal)
finalpositiony = initialposition(1) + initialvelocity(1) * tfinal + (1/2) * (acceleration(1)) * (tfinal**2)
finalvelocityy = initialvelocity(1) + (acceleration(1)) * (tfinal)


while positionx > 0 or positiony > 0:
    

#graphing
plt.plot(x, y)
plt.title('Graph of Projectile Motion')
plt.xlabel('Horizontal distance')
plt.ylabel('Vertical Distance')
plt.grid(True)
plt.show()
