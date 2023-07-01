import numpy as np
from numpy.random import default_rng
rng = default_rng(1234)

mystery_array = (rng.integers(low=0, high=500, size=216)
                * rng.integers(low=0, high=500, size=216)
                ).reshape((6, 6, 6))

# print(mystery_array)

'''Write code to select an array with 6 values
 that start with 6624 and ends with 43290. 
 These values live in the bottom part of the array'''



'''Write code to select the three values 44838, 147312, 91580
as an array These values live in the top part of the array.'''


# print(mystery_array)

# print(mystery_array[:, :, 0])
selected_array1 = mystery_array[4, -1]
# print(selected_array1) # Output: [  6624  26892 149100  16720 154912  43290]

# print(mystery_array[:, :, 4])
selected_array4 = mystery_array[:, :, 4]
# print(selected_array4)
selected_array3 = selected_array4[4]
# print(selected_array3) # Output: [  6357  22320  11024  21750  71149 154912]
# print(mystery_array [4, :, 4])

# print(mystery_array[0, 2, 3:]) # Output: [ 44838 147312  91580]
check_mystery_array = mystery_array[0, 2, 3:]

print(type(check_mystery_array[0]))  # Output: <class 'numpy.ndarray'> != numpy.int64









