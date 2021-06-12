import numpy as np
import time

# Kanto = np.array([73, 67, 888])
# weight = ([0.3, 0.2, 0.5])
# weight.shape

# print(Kanto)
# print(type(Kanto))
# print(np.dot(Kanto, weight))
# print(Kanto*weight).sum()

# starttime = time.perf_counter()
# arr1 = list(range(1000))
# arr2 = list(range(1000, 2000))
# # result = 0
# # for i1, i2 in zip(arr1, arr2):
# #     result += i1*i2
# #     print(result)

# # print('Total time taken is ', endtime-starttime)

# arr1_np = np.array(arr1)
# arr2_np = np.array(arr2)
# print(arr2_np.shape)
# # Find the Shape of materix
# np.dot(arr1_np, arr2_np)
# endtime = time.perf_counter()
# print('Total time taken is ', endtime-starttime)

# Have to be of Same datatype .dtype if One is other data then the whole answer will be Same type
# np.matmul is used to find the matrix Multiplication another Way is"@"

# arr2 = np.array([[[1, 2, 3, 4],
#                 [5, 6, 7, 8],
#                 [9, 10, 11, 12]]])
# arr3 = np.array([[12, 11, 10, 9],
#                  [8, 7, 6, 5],
#                  [4, 3, 2, 1]])

# Indexing
# print(arr2[0, 2])
# print(arr2[1:])

# print(arr2.shape)
# print(arr3.shape)
# arr4 = arr2+arr3
# print(arr2 == arr3)
# print(arr2 != arr3)
# print(arr2 > arr3)
# print(arr2 == arr3).sum()
# print(arr4)

# print(np.zeros([1, 2, 3]))
# print(np.ones([1, 2, 3]))
# print(np.eye([1, 2, 3]))
# Rand for random value between (0,1)  and randn for   (1,2)
