import numpy as np
import time

arr=np.array([10,20,30,40,50])
matrix=np.arange(1,10).reshape(3,3)#


print("First Element of Array:",arr[0])
print("matrix Slice:\n",matrix[:2,:2])

print("Addition:", arr + 5)
print("Multiplication:", arr * 2)

print("Mean:",np.mean(arr))
print("Max:",np.max(arr))
print("Standard Deviation:", np.std(arr))


print("Column-wise sum:",np.sum(matrix, axis=0))
print("Row-wise sum:",np.sum(matrix, axis=1))