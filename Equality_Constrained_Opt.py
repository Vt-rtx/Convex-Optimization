import numpy as np
import matplotlib as plt

def f(x1,x2,x3 ,l1, l2):
    return 3*(x1**2) + 4*(x2**2) + 4*(x3**2) + x1*x2 + x2*x3 - l1*(x1+x2+1) - l2*(x2 + x3 -1)

def grad_f(x1,x2,x3,l1,l2):
    return np.array([[6*x1 + x2 - l1]  ,[ 8*x2 + x1 + x3 -l1 -l2] , [8*x3 + x2 -l2] , [-x1 - x2 -1 ], [-x2 - x3 +1]])

def hess_f(x1,x2,x3,l1,l2):
    return np.array([[6.0 , 1.0 , 0.0 , -1.0 , 0.0] , [1.0 , 8.0 , 1.0 , -1.0 , -1.0] , [0.0 , 1.0 , 8.0 , 0.0 , -1.0] , [-1.0 , -1.0 , 0.0 , 0.0 , 0.0] , [0.0 , -1.0 , -1.0 , 0.0 , 0.0]])

x1,x2,x3,l1,l2 = 1.0,1.0,1.0,1.0,1.0
epsilon = 0.01

def step_size(x1,x2,x3,l1,l2):
    return np.linalg.inv(hess_f(x1,x2,x3,l1,l2))@grad_f(x1,x2,x3,l1,l2)

print(step_size(x1,x2,x3,l1,l2))

while(np.linalg.norm(grad_f(x1,x2,x3,l1,l2)) > epsilon):
    
        x1 = x1 - step_size(x1,x2,x3,l1,l2)[0][0]
        x2 = x2 - step_size(x1,x2,x3,l1,l2)[1][0]
        x3 = x3 - step_size(x1,x2,x3,l1,l2)[2][0]
        l1 = l1 - step_size(x1,x2,x3,l1,l2)[3][0]
        l2 = l2 - step_size(x1,x2,x3,l1,l2)[4][0]

print(f"The minima is x1 = {x1} , x2 = {x2} , x3 = {x3} , l1 = {l1} , l2 = {l2} ")
print(f"The minimum is: {f(x1,x2,x3,l1,l2) } " )
