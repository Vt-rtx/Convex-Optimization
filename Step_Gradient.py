import numpy as np
import pandas as pd

a = pd.read_csv('/home/vatsalc/Desktop/Sem 4/Convex_Optimization/Assignment_10(Regression)/Data.csv',delimiter='  ').to_numpy()

#Jacobian
J = np.array([[a[0][4] , np.sin(a[0][2] * a[0][3]) , np.cos(a[0][1] * a[0][0])]])
for i in range(1,len(a)):
    row = [[a[i][4] , np.sin(a[i][2] * a[i][3]) , np.cos(a[i][1] * a[i][0])]]
    J = np.append(J , row , axis = 0)

#F(X)
def F(c1,c2,c3):
    F = np.array([[ c1* J[0][0] + c2 * J[0][1] + c3 * J[0][2]]])
    for i in range(1,len(J)):
        row = [[ c1* J[i][0] + c2 * J[i][1] + c3 * J[i][2]]]
        F = np.append(F , row , axis = 0)
    return F

#Z
Z = np.array([[a[0][5]]])
for i in range(1,len(a)):
    row = [[a[i][5]]]
    Z = np.append(Z , row , axis = 0)

#Gradient of ||Z - F(C)||^2
def g(c1,c2,c3):
    return -2 * (Z - F(c1,c2,c3)).T @ J

c1,c2,c3 = 10.0,10.0,10.0
epsilon = 0.5

while(np.linalg.norm(g(c1,c2,c3)) > epsilon):

    a = 1.0
    while(np.linalg.norm(Z - F(c1 - a*g(c1,c2,c3)[0][0],c2 - a*g(c1,c2,c3)[0][1],c3 - a*g(c1,c2,c3)[0][2])) > np.linalg.norm(Z - F(c1,c2,c3))):
          a = a * 0.5

    c1 = c1 - a*g(c1,c2,c3)[0][0]
    c2 = c2 - a*g(c1,c2,c3)[0][1]
    c3 = c3 - a*g(c1,c2,c3)[0][2]

print(c1,c2,c3)    