import numpy as np
import matplotlib.pyplot as plt
from numpy.matlib import repmat


ctfile1 = "ciphertext-00112233445566778899aabbccddeeff.txt"
ctfile2 = "ciphertext-unknown_key.txt"
ptfile1 = "plaintext-00112233445566778899aabbccddeeff.txt"
ptfile2 = "plaintext-unknown_key.txt"
trfile1 = "traces-00112233445566778899aabbccddeeff.bin"
trfile1 = "traces-00112233445566778899aabbccddeeff.npy"
trfile2 = "traces-unknown_key.bin"
trfile2 = "traces-unknown_key.npy"

Sbox = np.array([
            0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
            0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
            0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
            0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
            0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
            0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
            0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
            0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
            0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
            0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
            0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
            0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
            0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
            0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
            0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
            0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16
            ])

#Quick python and numpy tutorial

tutorial = '''
The functions myin and myload have been easier to understand at the cost of more complexity
once the data has been extracted from the file. Instead of delimiting your data before loading
it you now get all the data loaded into the variable. Then you can cut out whatever data
you want afterwards. 

To help you understand how to do that I will show some examples of cutting out parts of a
matrix using numpy.

First, let's create a 1-D array
'''

a = np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print("a = ", a, "\n")

tutorial = '''
the dimensions of numpy arrays are denoted by square brackets. If there is a single set of 
square brackets, like above, then it's 1-D. To see the dimensionality of numpy arrays you can
print the "shape" property. Let's try it.
'''

print("shape of a = ", a.shape, "\n")

tutorial = '''
this returns a tuple. If you want to iterate over a matrix you can use these dimensions by
indexing into the tuple. To show this, let's create a 2-D array.
'''

b = np.array([[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], [1,2,1,0,1,2,1,0,1,2,1,0,1,2,1,0], [22,2,22,2,22,2,22,2,22,2,22,2,22,2,22,2]])
print("b = ")
print(b, "\n")
print("shape of b = ", b.shape)
rows = b.shape[0]
columns = b.shape[1]
print("rows in b = ", rows)
print("columns in b = ", columns)

#a useful property of python is that you can return or assign multiple variable at once
r,c = b.shape
print("r = ", r)
print("c = ", c, "\n")

tutorial = '''
To index into multidimensional matrices using numpy you can either do it like this:
matrix[X][Y]

or you can do it like this:
matrix[X,Y]

This would return the singular element at coordinate (X,Y) in the matrix.
If you want all the elements at row X, you use matrix[X].

The character  :  can be used to create delimitations. It can also be used to address
the entirety of a dimension. So if we wanted to return the full column at Y we would do:
matrix[:,Y]

Let's test this.
'''

element = b[0, 13]
print("element at (0, 13) in b = ", element)
element = b[2, 12]
print("element at (2, 12) in b = ", element)
row = b[1]
print()
print("row number 1 in b = ", row)
column = b[:,2]
print("columns number 2 in b = ", column, "\n")

tutorial = '''
Now let's delimit the size of a row. Let's say we want all rows, but only the first
5 elements of each.

To do this you would do:
matrix[:, :5]

let's test this
'''

delimited = b[:, :5]
print("first 5 elements of all rows = ")
print(delimited)

tutorial = '''
If you ever need to transpose a matrix, use:
transpose = matrix.T

now let's do a quick example of plotting something using matplotlib. Let's plot what 
array a is if we first bitwise XOR every element with 13

To make a nice looking plot, refer to the pyplot documentation. For now, we will
leave all axes unlabeled and just plot.
'''

xored = a^13
plt.plot(xored)
plt.show()

#Some more python tutorial
tutorial = '''
You will need to be able to do some combination of iterations, list operations, or broadcasting to do this lab in python.

I will show some simple examples of each of these concepts.

Let's start with the one you should all be familiar with: loops and conditionals.
'''

print("A range counts from a starting number to an end number using a specified step size")
print("\nrange(5):")
for i in range(5):
    print(i)
print("this range counts from 0 to 5. Ranges are not inclusive. Same with list indexing\n\nrange(0,5,1):")
for i in range(0,5,1):
    print(i)
print("these two do the same")

print("\nyou could use while loops. Generally you wouldn't want to.\n")
i = 0
while i < 10:
    i+=1
    if i == 3:
        continue
    print(i)
    if i == 6:
        break
print("notice that 3 is missing because we continued the loop without finishing all steps. It also ends at 6") 
print("because we used a break statement.")

print("\nHere's another way to loop things that is common in python that novices may not know of:\n")
string = "strings are lists of chars"
output = [print(i) for i in string]
output = [ord(i)+1 for i in string]
output = [chr(i)for i in output]

print("\nyou can append elements at the end of a python list using the + operator. Let's rebuild the string we just altered.")
string = ""
print(string)
for char in output:
    string+=char
print(string)

print("\nfinally, let's talk about numpy linear algebra operations. Using numpy you can do so called broadcasting operations")
print("as well as all the regular linear algebra you would expect.")
print("let's calculate the dot product of [[1],[2], [3], [4]] and [[2,3,4]])")
print("but, first, let's learn about the very useful np.atleast_2d function. This forces a 1D vector to become a 2D matrix")
print("with a single width of its first dimentsion. Let's use this and transposition when making the vectors")

A = np.atleast_2d([1,2,3,4])
B = np.atleast_2d([2,3,4])
print("A:", A)
print("B:",B)
print("\ntranspose A\n")
A = A.T
print("new A:")
print(A)
print("\ndot product of A.dot(B):")
mat = A.dot(B)
print(mat)

print("\n\nyou can multiply, divide, add, subtract, exponentiate, etc. all elements of a numpy matrix easily.")
print("\nadding 4 to each index:")
mat = mat+4
print(mat)
print("\ndividing each index by 2:")
mat = mat/2
print(mat)
print("\nsubtracting 3 for each index:")
mat = mat-3
print(mat)
print("\nmultiplying by 10:")
mat = mat*10
print(mat)
print("\neach index to the third power:")
mat = mat**3
print(mat)
print("\nfifth root:")
mat = mat**(1/5)
print(mat)

print("\n")
print("Hadamar product with a vector [1,2,3] repeated 4 times:")
t = repmat([1,2,3], 4, 1)
print("factor for Hadamar product:\n",t)
mat = mat * t
print("\nresult\n",mat)

print("\ntruncate values to ints, then we will bitwise XOR")
mat = mat.astype("uint32")
print("truncated:\n", mat)
print("\nXOR everything with 17")
mat = mat^17
print("results:\n", mat)

print("\n\nFinally you should know that you can intex into one array using another array or matrix. This lets you")
print("swap out all the values in one array for the value they correspond to if they were the indexes of another.")
print("to show this, let's use this final matrix and replace all values with their Sbox values:")
mat = Sbox[mat]
print("\nsubstituted values:\n", mat)

tutorial = '''
The lab can be solved entirely using some of the commands shown in this introduction to using mathematics in python.
Remember that you can choose to do the lab in Matlab instead if you are more comfortable using Matlab.
There may also be fewer lab bookings available for python this year... (2021)
'''
