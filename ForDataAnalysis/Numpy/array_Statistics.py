import numpy as np
import os

if __name__ == '__main__':
    arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
    # all element's  sum
    print(arr.sum())
    # all element mul
    print(arr.prod())
    # all mean
    print(arr.mean())

    # axis = 0, handle the colomn; Otherwise row
    print(arr.mean(axis=0))
    print(arr.sum(axis=0))

    # cumsum will count the sum
    # same as cumprod()
    print(arr.cumsum()) # [ 0  1  3  6 10 15 21 28 36]
    print(arr.cumsum(axis=0))

    # unique make element unique
    duparr = np.array([1,1,2,2,3,3])
    print(np.unique(duparr)) # 1, 2, 3

    # union1d(x,y) x | y (with sort and unique)
    # intersect1d(x,y) x & y
    # in1d(x,y) [True if x in y else False]
    # setdiff1d(x,y) [in x and not in y]
    # setxor1d(x,y) [x xor y]
    xarr = np.array([4,1,1,3])
    yarr = np.array([1,2])
    print(np.union1d(xarr,yarr)) # 1, 2, 3, 4

    # save the array
    arr_save = np.arange(10)
    np.save('saved', arr_save) # saved.npy

    if os.path.exists('saved.npy'):
        arr_load = np.load('saved.npy')
        print(arr_load)
