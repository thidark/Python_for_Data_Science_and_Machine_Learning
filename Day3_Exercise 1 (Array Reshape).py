# Create 1D array contraining numbers from 10 to 24(inclusive
import numpy as np
arr = np.arange(10, 25)
print("1D Array from 10 to 24:", arr)

#Create 1D array using np.arange() (should have 15 elements from 5 to 19
arr2 = np.arange(5, 20)
print("1D Array from 5 to 19:", arr2)

#Reshape it into a 3D array of shape (3, 5, 1)
reshaped_arr = arr2.reshape(3, 5, 1)
print("Reshaped 3D Array (3, 5, 1):\n", reshaped_arr)