import numpy as np
print(np.__version__)

#array creation
arr1=np.array([1,2,3,4,5])
print("Array 1:", arr1)

arr2=np.array([[1,2,3],[4,5,6]])
print("Array 2:\n", arr2)   

#---------------------------------------------------
#Built-in functions
zeros_arr=np.zeros((2,3))
print("Zeros Array:\n", zeros_arr)
ones_arr=np.ones((3,2))
print("Ones Array:\n", ones_arr)
eye_arr=np.eye(3)
print("Identity Matrix:\n", eye_arr)
np.full((2,2),7)
print("Full Array:\n", np.full((2,2),7))
rand_arr=np.random.rand(2,3)
print("Random Array:\n", rand_arr)

#---------------------------------------------------
#Ranges
range_arr=np.arange(0,10,2)
print("Range Array:", range_arr)

#spacing
linspace_arr=np.linspace(0,1,5)
print("Linspace Array:", linspace_arr)

#Dimensions 
arr2=np.array([[1,2,3],[4,5,6]])
print("Array 2 Dimensions:", arr2.ndim)
print("Array 2 Shape:", arr2.shape)


#Reshaping
reshaped_arr=arr2.reshape(3,2)
print("Reshaped Array:\n", reshaped_arr)

#---------------------------------------------------
#Indexing and Slicing
print("Element at (0,1):", arr2[0,1])   
print("First Row:", arr2[0,:])
print("Second Column:", arr2[:,1])
print("Sliced Array:\n", arr2[0:2,1:3])

arr=np.array([[1,2,3],[4,5,6],[7,8,9]])
#Mathematical Operations
print("Array + 10:\n", arr + 10)
print("Array * 2:\n", arr * 2)  

#---------------------------------------------------
#array addition
arr_a=np.array([[1,2,3],[4,5,6]])   
arr_b=np.array([[7,8,9],[10,11,12]])
print("Array A + Array B:\n", arr_a + arr_b)
print("Array A * Array B:\n", arr_a * arr_b)
#Statistical Functions
print("Mean:", np.mean(arr))

#---------------------------------------------------
#array comparison
print("Elements greater than 5:\n", arr > 5)
#Boolean Masking
mask=arr > 5
print("Elements greater than 5:", arr[mask])
#or directly
print("Elements greater than 5:", arr[arr > 5]) 

#---------------------------------------------------
#Mathematical/statistical functions
print(arr)
print("Sum of all elements:", np.sum(arr))  
print("Standard Deviation:", np.std(arr))
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))
print("Transpose of Array:\n", arr.T)

print("Index/postion of the minimum value",np.argmin(arr))
print("Index/position of the maximum value",np.argmax(arr))
print("Flattened Array:", arr.flatten())
print("Sorted Array:", np.sort(arr, axis=None))
print("Unique Elements:", np.unique(arr))

#---------------------------------------------------
#Random Number Generation
random_ints=np.random.randint(0,100,size=5)
print("Random Integers:", random_ints)
random_floats=np.random.rand(5) 
print("Random Floats:", random_floats)
#Set seed for reproducibility

#---------------------------------------------------
np.random.seed(42)
random_nums1=np.random.rand(3)
random_nums2=np.random.rand(3)
print("Random Numbers Set 1:", random_nums1)
print("Random Numbers Set 2:", random_nums2)