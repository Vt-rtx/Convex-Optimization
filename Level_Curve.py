import numpy as np
import matplotlib.pyplot as plt
import math

def plot_level_curve(f, levels, xlim, ylim, resolution=1000):

    x = np.linspace(xlim[0], xlim[1], resolution)
    y = np.linspace(ylim[0], ylim[1], resolution)

    X, Y = np.meshgrid(x, y)

    Z = f(X, Y)

    for level in levels:
        
        x_contour = []
        y_contour = []
    
        for i in range(len(x)):
            for j in range(len(y)):
                
                if abs(Z[i,j] - level) < 0.01:
                    
                    x_contour.append(x[i])
                    y_contour.append(y[j])

        plt.scatter(x_contour, y_contour)

    plt.show()


def f(x, y):
    return x**2 + y**2

plot_level_curve(f, levels=[1], xlim=(-10, 10), ylim=(-10, 10))
