import numpy as np
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

#1) How many negative numbers are there?
def count_negative(a):
    return a[a < 0]
len(count_negative(a))

#2) How many positive numbers are there?
def count_positive(a):
    return a[a > 0]
len(count_positive(a))

#3) How many even positive numbers are there?
a = a[a % 2 == 0]
a = a[a > 0]
len(a)

#4) If you were to add 3 to each data point, how many positive numbers would there be?
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

a1 = a + 3
a1 = a1[a1 > 0]
len(a1)

#5) If you squared each number, what would the new mean and standard deviation be?
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

ar = a ** 2
ar = ar.mean(), ar.std()
ar

#6) A common statistical operation on a dataset is centering. 
# This means to adjust the data such that the mean of the data is 0. 
# This is done by subtracting the mean from each data point. 
# Center the data set. See this link for more on centering.
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
x = a-a.mean()
x 

#7) Calculate the z-score for each data point. Recall that the z-score is given by:
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
m = a-a.mean()
s = a.std()
a = a-a.mean()/a.std()
a

#8) 
import numpy as np
# Life w/o numpy to life with numpy

## Setup 1
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = sum(a)

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = min(a)

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = max(a)

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = a.mean()

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a = a.product()
product_of_a

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a = np.square(a)
squares_of_a

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = a[a % 2 != 0]
odds_in_a

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = a [a % 2 == 0]
evens_in_a

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = np.array ([
    [3, 4, 5],
    [6, 7, 8]])

b = b.min(), b.max(), b.sum(), np.average(b), b.prod(), np.square(b)

b
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. **Hint, you'll first need to make sure that the "b" variable is a numpy array**
b = np.array ([
    [3, 4, 5],
    [6, 7, 8]])

sum_of_b = b.sum()
sum_of_b

# Exercise 2 - refactor the following to use numpy. 
min_of_b = b.min()
min_of_b

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = b.max()
max_of_b

# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b= b.mean()
mean_of_b

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = b.prod()
product_of_b
# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = np.square(b)
squares_of_b

# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = b[b % 2 != 0]
odds_in_b

# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = b[b % 2 == 0]
evens_in_b

# Exercise 9 - print out the shape of the array b.
b.shape

# Exercise 10 - transpose the array b.
np.transpose(b)

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
b = np.reshape(1, 6)
b
# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
b = np.reshape(6, 1)
b
## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
# Exercise 1 - Find the min, max, sum, and product of c.

# Exercise 2 - Determine the standard deviation of c.

# Exercise 3 - Determine the variance of c.

# Exercise 4 - Print out the shape of the array c

# Exercise 5 - Transpose c and print out transposed result.

# Exercise 6 - Get the dot product of the array c with c. 

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d

# Exercise 2 - Find the cosine of all the numbers in d

# Exercise 3 - Find the tangent of all the numbers in d

# Exercise 4 - Find all the negative numbers in d

# Exercise 5 - Find all the positive numbers in d

# Exercise 6 - Return an array of only the unique numbers in d.

# Exercise 7 - Determine how many unique numbers there are in d.

# Exercise 8 - Print out the shape of d.

# Exercise 9 - Transpose and then print out the shape of d.

# Exercise 10 - Reshape d into an array of 9 x 2