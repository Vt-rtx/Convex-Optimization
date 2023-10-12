import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return (1 - (x**2)*np.exp(-x))

def df(x):   
    return (-2*x*np.exp(-x) +(x**2)*np.exp(-x))

def ddf(x):
    return  (-2*np.exp(-x)+2*x*np.exp(-x))-(-2*x*np.exp(-x) +(x**2)*np.exp(-x))

p = float(input("Enter value of x_0:" ))
e = float(input("Enter value of Epsilon: "))

k = np.linspace(-0.5,2.5, 10000)
x_arr = []
y_arr = []

while (abs(df(p)) > e ):
    x_arr.append(p)
    y_arr.append(df(p))
    
    temp = p - (df(p)/ddf(p))
    p = temp

plt.plot(p,f(p),'.', label= "o")
plt.plot(k,f(k))
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid()
plt.show()


plt.stem(range(1,len(y_arr)+1),y_arr)
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.xlabel("Iteration no.")
plt.ylabel("f'(x)")
plt.grid()
plt.show()
