import matplotlib.pyplot as plt
import numpy as np
import random

def generate_Points():
    mean = [3, 3]
    cov = [[1, 0], [0, 1]]
    a = np.random.multivariate_normal(mean, cov, 500).T
    mean = [-3, -3]
    cov = [[2, 0], [0, 5]]
    b = np.random.multivariate_normal(mean, cov, 500).T
    #c = np.concatenate((a, b), axis=1)
    #c = c.T
    #np.random.shuffle(c)
    #c = c.T
    #x = c[0]
    #y = c[1]
    #plt.plot(x, y, 'x')
    plt.scatter(a[0],a[1],marker='1',label="a")
    plt.scatter(b[0],b[1],marker='1',label="b")
    plt.axis('equal')
    plt.show()




if __name__ == '__main__':
    random.seed(1)
    generate_Points()
