import numpy as np
import matplotlib.pyplot as plt
import math

def f(x,n,a):
    return (x**n - a)

def df(x,n,a):
    return (n*(x**(n-1)))

a = float(input("Enter non negative real no: "))
n = int(input("Enter value of n: "))
e = float(input("Enter value of Epsilon: "))

p = a

while (abs(f(p,n,a) > e)):
    p  = p - (f(p,n,a)/df(p,n,a))

print(f"The {n}th root of {a} is: {p} ")

plt.plot(p , f(p,n,a) , marker = "o")
k = np.linspace(0,p+2, 10000)
plt.plot(k,f(k,n,a))
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid()
plt.show()