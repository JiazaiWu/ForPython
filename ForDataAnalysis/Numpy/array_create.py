import numpy as np

if __name__ == '__main__':
    arr1 = np.eye(3)
    # change element's type
    print(arr1.dtype)
    arr1 = arr1.astype(np.int32)
    print(arr1.dtype)

    # Boolean index
    arr2 = np.arange(10)
    bool_idx = (arr2 % 2 ) == 0
    print(bool_idx)
    arr2 = arr2[bool_idx]
    print(arr2) # 0,2,4,6,8

    # fancy index
    arr3 = np.arange(10)
    arr3 = arr3[[1,3,5,7,9]] # note index is another list
    print(arr3) # 1,3,5,7,9

    # isnan -- is not a number
    # abs, fabs -- absolution value, fabs is faster if arr is not complex number
    # exp -- e**arg
    arr4 = np.random.randn(7)*10
    arr4 =  np.modf(arr4)
    print(arr4) # will show two list -- first is after the point; second is before the point

    # where(condition, yes_arr, no_arr)
    # you can format condition by boolean index
    xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
    yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
    cond = np.array([True, False, True, True, False])
    arr5 = np.where(cond, xarr, yarr)
    print(arr5) # 1.1, 2.2, 1.3, 1.4, 2.5
