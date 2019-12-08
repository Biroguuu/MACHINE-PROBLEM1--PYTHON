#MACHINE PROBLEM 1 - 2ECE-A , GROUP 3:  PEREZ,PIOLO - SERGIO, RICHARD 
#import needed libraries for plotting 
import matplotlib.pyplot as plt
import numpy as np

#function to get values for y 
def function(n):
    if (n>=0) and (n<9):
        return n*n-7;
    elif (n>=10) and (n<100):
        return function(n-10);
    else:
        return;

x = np.arange(100)
y = []
for num in x:
    y.append(function(num))

#output showing the graph 
plt.stem(x,y)
plt.show()