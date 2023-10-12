import matplotlib.pyplot as plt
import numpy as np


def f(x):
    return (1 - (x**2)*np.exp(-x))

def df(x):   
    return (-2*x*np.exp(-x) +(x**2)*np.exp(-x))


e = float(input("Enter value of Epsilon:"))
l = -0.5
r = 2.5
k = np.linspace(l,r,10000)

width = []
                                                                            
while(abs(r -l) > 2*e):
    c = (r + l )/ 2
    plt.scatter([c], [f(c)], color="green")
    if df(c) > 0 :
        r = c
        width.append(r-l)
    elif df(c) < 0:
        l = c
        width.append(r-l)
    else:
        l = c
        r = c
        width.append(r-l)
        break


minima = (l + r )/2    
print(f"The minima is at {minima}")

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
