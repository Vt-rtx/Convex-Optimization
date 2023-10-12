import numpy as np
import cvxpy as cp
# Define the variables
x = cp.Variable(5)

# Define the objective function using matrix form
Q = np.diag([2, 2, 2, 2, 2])
Q[0, 1] = -1
Q[1, 0] = -1
Q[1, 2] = -1
Q[2, 1] = -1
Q[2, 3] = -1
Q[3, 2] = -1
Q[3, 4] = -1
Q[4, 3] = -1
b = np.array([-1, -1, -1, -1, 0])
objective = cp.Minimize(cp.quad_form(x, Q) - b.T @ x)

# Define the constraints (there are no constraints in this example)

# Solve the problem
problem = cp.Problem(objective)
problem.solve()

# Print the optimal values of x
print(x.value)
print(problem.value)