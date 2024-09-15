"""
Gradient Descent Algorithm

Using a learning rate and starting x value the algorithm uses the local slope
(slope at that x-value) to go down the slope and find the lowest point.
In this example, the learning rate is 0.01 and the starting x value is -2 so
the algorithm uses a given formula to calculate the slope and move the x a
certain distance down that slope using the learning rate 10 times
"""

import matplotlib.pyplot as plt
import numpy as np

#gradient descent
lr = 0.01
n_epochs = 20
x = 3
x_list = [x]
for i in range(n_epochs):
  #the negative sign (x-lr...) means it will go down the slope (gradient descent)
  #slope = 3*(x**2)-5
  x = x - lr*(3*(x**2)-5)
  x_list.append(x)
  #print(x)

#plotting curve ***Note: Not always available***
x_curve = np.linspace(-3,3,100)
y_curve = (x_curve**3)-5*x_curve
plt.plot(x_curve, y_curve)

#find path taken during gradient descent
x_list = np.array(x_list)
y_list = (x_list**3)-5*x_list

plt.scatter(x_list, y_list)
plt.axis('equal')
plt.grid()
