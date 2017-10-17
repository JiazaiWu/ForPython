import numpy as np

if __name__ == '__main__':
    m1 = np.mat("0 1 2;1 0 3;4 -3 8")
    print(m1)

    # inv - get m^-1
    inv = np.linalg.inv(m1)
    print(inv)

    # solve - get the solution of linear equation
    B = np.mat("1 -2 1;0 2 -8;-4 5 9")
    b = np.array([0,8,-9])
    x = np.linalg.solve(B, b)
    print(x)

    # eig - get eigval and eigvector
    C = np.mat("3 -2;1 0")
    val, vec = np.linalg.eig(C)
    print(val)
    print(vec) # the vector is the column element of vec

    # SVD（Singular Value Decomposition) - get U sigma V; U and V are orthogonal matrix
    D = np.mat("4 11 14;8 7 -2")
    U,Sigma,V = np.linalg.svd(D,full_matrices=False)
    print('U:',U)
    print('V:',V)
    print('sigma:0', Sigma)

    # np.linalg.det - easy...
