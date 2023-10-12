import matplotlib.pyplot as plt
import numpy as np
import math

# Define the function
def f(x1,x2,x3):
    return (x1 -1)**2  + 2*(2*(x2**2) - x1)**2 + 3*(2*(x3**2)-x2)**2

def grad_f(x1,x2,x3):
    return np.array([2*(x1-1) -4*(2*(x2**2) - x1) , 8*(2*(x2**2)-x1)*(2*x2) - 6*(2*(x3**2)-x2) , 24*(2*(x3**2)-x2)*(x3)])

def hess_f(x1,x2,x3):
    return np.array([[6,-16*x2,0],[-16*x2,16*(2*(x2**2) -x1)+64*(x2**2)+6,-24*x3],[0,-24*x3,24*(2*(x3**2)-x2)+96*(x3**2)]])

def step_size(x1,x2,x3):
    return np.linalg.inv(hess_f(x1,x2,x3))@grad_f(x1,x2,x3)

def gradient_descent(x1,x2,x3):
    x1_new = x1 - step_size(x1,x2,x3)[0]
    x2_new = x2 - step_size(x1,x2,x3)[1]
    x3_new = x3 - step_size(x1,x2,x3)[2]
    return x1_new,x2_new,x3_new

def Norm_grad(x1,x2,x3):
    return np.sqrt(grad_f(x1,x2,x3)[0]**2+grad_f(x1,x2,x3)[1]**2+grad_f(x1,x2,x3)[2]**2)

x1,x2,x3 = float(input("Enter x1: ")),float(input("Enter x2: ")),float(input("Enter x3: "))
epsilon = float(input("Please input the epsilon value: "))

while(Norm_grad(x1,x2,x3)> epsilon):
    x1,x2,x3 = gradient_descent(x1,x2,x3)

print("The minima is: ",x1,x2,x3)
print(f"The value of f(x) is {int(f(x1,x2,x3))}")