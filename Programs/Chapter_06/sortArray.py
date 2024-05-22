import numpy as np

a = np.array([4, 3, 6, 2, 7])
b = np.sort(a)
print('sort Array: ', b)

indices = np.argsort(a)
print('Argsort: ', indices)

c = [4, 3, 1, 5, 2]
d = np.sort_complex(c)
print('Complext Sort: ', d)


students = np.array([30, 10, 20])
ages = np.array([20, 12, 10])

lexIndices = np.lexsort((ages, students))

for i in lexIndices:
    print('lexsort: ',students[i] , ", " , ages[i])

