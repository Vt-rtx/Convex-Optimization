import numpy as np
import matplotlib.pyplot as plt

z = np.array([1.842,1.342,1.571], dtype = float)

# Define the system
def f1(x1,x2,x3):
    #print(x1*x3)
    return (np.sin(x1))**2 + np.exp(x1-x2) + np.log(abs(x1*x3))
    
def f2(x1,x2,x3):
    #print(x2*x3)
    return (np.cos(x1))**2 + np.exp(x2 - x3) + np.log(abs(x2*x3))

def f3(x1,x2,x3):
    #print(x1*x2*x3)
    return np.sin(x1)*np.cos(x1) + np.exp(x3-x1) + np.log(abs(x1*x2*x3))

def f(x1,x2,x3):
    return np.array([f1(x1,x2,x3),f2(x1,x2,x3),f3(x1,x2,x3)] , dtype = float)

# Define the Jacobian
def J(x1,x2,x3):
    J = np.array([[2*np.sin(x1)*np.cos(x1) + np.exp(x1-x2) + 1/(x1)  ,  -np.exp(x1-x2)  ,  1/(x3)],
                  [-2*np.sin(x1)*np.cos(x1)   , np.exp(x2-x3) + 1/(x2)   , -np.exp(x2-x3) + 1/(x3)],
                  [(np.cos(x1))**2 - (np.sin(x1))**2 - np.exp(x3-x1) + 1/(x1)   , 1/(x2)   ,   np.exp(x3-x1) + 1/(x3)]], dtype = float)
    return J

# Define the delta x
def Dx(x1,x2,x3):
    return (np.linalg.inv(((J(x1,x2,x3)).T)@J(x1,x2,x3))) @ (((J(x1,x2,x3)).T)@((z - f(x1,x2,x3))))

x1,x2,x3 = float(input("Enter x1: ")),float(input("Enter x2: ")),float(input("Enter x3: "))
epsilon = float(input("Enter epsilon: "))

norm = []

while(np.linalg.norm(z - f(x1,x2,x3)) > epsilon):
    norm.append(np.linalg.norm(z - f(x1,x2,x3)))
    a = x1 + Dx(x1,x2,x3)[0]
    b = x2 + Dx(x1,x2,x3)[1]
    c = x3 + Dx(x1,x2,x3)[2]
    print(Dx(x1,x2,x3))
    x1,x2,x3 = a,b,c
    print(x1,x2,x3)

print("The solution is: ",x1,x2,x3)
plt.plot(norm)
plt.xlabel("Iteration",size = 15)
plt.ylabel("||z - f(x)||",size = 15)
plt.show()