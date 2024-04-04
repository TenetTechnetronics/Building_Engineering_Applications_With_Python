import numpy as np

a = np.array([1, 2, 3])
a = np.append(a, [4, 5])
print('Append Array: ', a)

b = np.insert(a, 2, [7, 8])  # Insert 7 and 8 at index 2
print('Insert Array', b)

c = np.concatenate((a, b))
print('Concatenate Array: ', c)
