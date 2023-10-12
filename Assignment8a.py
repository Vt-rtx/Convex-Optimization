import matplotlib.pyplot as plt
import numpy as np
import math

# Define the function
def f(x1,x2):
    return 100*(x2-x1)**2+(1-x1)**2

# Define the gradient of the function
def grad_f(x1,x2):
    return np.array([-200*(x2-x1)-2*(1-x1),200*(x2-x1)])

# Define the Hessian of the function
def hess_f(x1,x2):
    return np.array([[202,-200],[-200,200]])

# Define the function to calculate the step size
def step_size(x1,x2):
    return np.linalg.inv(hess_f(x1,x2))@grad_f(x1,x2)

# Define the function to calculate the gradient descent
def gradient_descent(x1,x2):
    x1_new = x1 - step_size(x1,x2)[0]
    x2_new = x2 - step_size(x1,x2)[1]
    return x1_new,x2_new

def Norm_grad(x1,x2):
    return np.sqrt(grad_f(x1,x2)[0]**2+grad_f(x1,x2)[1]**2)

x1,x2 = float(input("Enter x1: ")),float(input("Enter x2: "))
epsilon = float(input("Please input the episoln value: "))

while(Norm_grad(x1,x2)> epsilon):
    x1,x2 = gradient_descent(x1,x2)

print("The minimum point is: ",x1,x2)
print(f"The value of f(x) is ${f(x1,x2)}")