import numpy as np

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
b = np.delete(a, [4, 6]) # Delete item at index 4 and 6
print('Deleted Array: ', b)
