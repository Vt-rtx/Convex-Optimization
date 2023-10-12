import matplotlib.pyplot as plt
import numpy as np
import math
import sys


def g(x):

    if isinstance (x**(5/3) + 30*x + 20 , complex):
        raise Exception ("Roots are complex")
    else:
        return (x**(5/3) + 30*x + 20)



def dg(x):
 
    if isinstance  ((5/3)*(x**(2/3)) + 30  , complex):
        raise Exception ("Roots are complex")
    else:
        return ((5/3)*(x**(2/3)) + 30)

p = float(input("Enter value of x_0:" ))
e = float(input("Enter value of Epsilon: "))


x_ = []
y_ = []
y__ = []

while(abs(g(p)) > e):
    p = p - (g(p)/dg(p))
    x = p
    y = g(p)
    x_.append(p)
    y_.append(abs(dg(p)))
    y__.append(g(p))


print(f"The root of g(x) is {p}")


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