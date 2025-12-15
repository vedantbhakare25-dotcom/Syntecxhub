import numpy as np
import time

arr=np.array([10,20,30,40,50])
matrix=np.arange(1,10).reshape(3,3)#


print("First Element of Array:",arr[0])
print("matrix Slice",matrix[:2,:2])

print("Addition:",arr + 5)
print("Multiplication:",arr * 2)

print("Mean:",np.mean(arr))
print("Max:",np.max(arr))
print("Standard Deviation:",np.std(arr))


print("Column-wise sum:",np.sum(matrix,axis=0))
print("Row-wise sum:",np.sum(matrix,axis=1))

reshaped=arr.reshape(5,1)
broadcasted=reshaped + np.array([1,2,3])
print("Broadcasted array",broadcasted)

np.save("data.npy",arr)
loaded_arr=np.load("data.npy")
print("Loaded array:",loaded_arr)

size=1000000
python_list=list(range(size))
numpy_array=np.arange(size)

start=time.time()
[x * 2 for x in python_list]
print("Python list time:",time.time() - start)

start=time.time()
numpy_array * 2
print("NumPy array time:",time.time() - start)
