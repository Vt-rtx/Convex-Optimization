import matplotlib.pyplot as plt
import numpy as np
import math


def f(x):
    return ((np.exp(-x) - np.cos(x))/np.exp(x))

def df(x):   
    return ((np.exp(x)*(np.sin(x) + np.cos(x)) - 2)/np.exp(2*x))


p = float(input("Enter value of x_0:" ))
e = float(input("Enter value of Epsilon: "))

x_ = []
y_ = []
y__ = []

while(abs(f(p)) > e):
    p = p - f(p)/df(p)
    x = p
    y = f(p)
    x_.append(p)
    y_.append(abs(df(p)))
    y__.append(f(p))

plt.stem(range(1,len(x_)+1),x_)
plt.xlabel("Iteration no.")
plt.ylabel("x_k")
plt.grid()
plt.show()

plt.stem(range(1,len(y_)+1),y_)
plt.xlabel("Iteration no.")
plt.ylabel("|g'(x)|")
plt.grid()
plt.show()

k = np.linspace(-0.05,p + 3, 10000)
plt.plot(k,f(k))
plt.scatter([x_] , [y__] , marker = "o")
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid()
plt.show()   