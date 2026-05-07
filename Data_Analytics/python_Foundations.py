import numpy as np
# Create a list and multiply it by 2
list1 = [1,2,3,4,5]
print(list1 *2) # Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]

# converting the list to a numpy array and multiplying it by 2

print(np.array(list1) * 2) # Output: [ 2  4  6  8 10]


# we are able to see dimensions of the array
zero_dimension = np.array((3,4))
print(zero_dimension.ndim) # Output: 0

ones_dimension = np.array([1,2,3,4,5])
print(ones_dimension.ndim) # Output: 1

two_dimension = np.array([[1,2,3],
                          [4,5,6]])
print(two_dimension.ndim) # Output: 2

three_dimension = np.array([[[1,2,3],[4,5,6]],
                             [[7,8,9],[10,11,12]]])
print(three_dimension.ndim) # Output: 3

# accessing elements in a 2D array
print(two_dimension[0,0]) # Output: 1
print(two_dimension[0,1]) # Output: 2

# accessing elements in a 3D array
print(three_dimension[0,0,0]) # Output: 1
print(three_dimension[0,0,1]) # Output: 2
print(three_dimension[0,1,0]) # Output: 4

#slicing arrays
print(two_dimension[0,:]) # Output: [1 2 3]
print(two_dimension[:,0]) # Output: [1 4]
print(three_dimension[0,:,:]) # Output: [[1 2 3]
#                                     [4 5 6]]
                                    
#reshaping arrays
reshaped_array = two_dimension.reshape(3,2)
print(reshaped_array) # Output: [[1 2]
#                            [3 4]
#                            [5 6]]

# concatenating arrays
array1 = np.array([1,2,3])
array2 = np.array([4,5,6])
concatenated_array = np.concatenate((array1, array2))
print(concatenated_array) # Output: [1 2 3 4 5 6]

# list of methods of numpy arrays
## 1. np.array() - creates a numpy array from a list or tuple
## 2. np.zeros() - creates an array filled with zeros
## 3. np.ones() - creates an array filled with ones
## 4. np.arange() - creates an array with a range of values
## 5. np.reshape() - reshapes an array to a specified shape
## 6. np.concatenate() - concatenates two or more arrays
## 7. np.mean() - calculates the mean of an array
## 8. np.median() - calculates the median of an array
## 9. np.std() - calculates the standard deviation of an array
## 10. np.sum() - calculates the sum of an array



