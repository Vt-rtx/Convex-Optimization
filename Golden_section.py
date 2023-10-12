import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (1 - (x**2)*np.exp(-x))


phi = (3 - 5**0.5) /2

e = float(input("Enter value of Epsilon:"))

l =-0.5
r = 2.5

k = np.linspace(l,r,10000)

width = []

while(abs(l-r) > e):
    
    if f(l) < f(r) :
        r = r - (r -l)*phi
        width.append(r-l)

    else :
        l = l + (r - l)*phi
        width.append(r-l)
 

print(f"The minima is at {(l+r)/2}")

plt.plot(k,f(k))
plt.plot((l+r)/2,f((l+r)/2) ,marker = 'o')
plt.axvline(x=0, c="red")
plt.axhline(y=0, c="red")
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.grid()
plt.show()

plt.stem(range(1,len(width)+1),width)
plt.xlabel("Iteration no.")
plt.ylabel("Width")
plt.grid()
plt.show()