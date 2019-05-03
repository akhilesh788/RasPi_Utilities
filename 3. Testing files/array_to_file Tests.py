import RasPiUtilities
import numpy as np

# Test 1 : Normal Numpy matrix passed.
a= np.array([[b'\xAA', b'\xBB'], [b'\xFF', b'\x0b'], [b'\x0c', b'\xff']], dtype="S1")
# Works OK

# Test 2 : missing value in Numpy Array after/between commas  ['val',]
# a2= np.array([[b'\xAA', ], [b'\xFF', b'\x0b'], [b'\x0c', b'\xff']], dtype="S1")
# (Non Critical Error, error occurs in caller function, not called function.) Result: ValueError: setting an array element with a sequence.

# Test 3: Normal 1-D list passed.
# a3=[b'\xAA',b'\xAB',b'\xAF']
# Works OK

# Test 4: passing a list of integers.
# a4=[1,2,3,4,4,5,6,250]
# Works OK

# Test 5: passing a list of integer values where some values not in the range [0,255]
# a5 = [5456,564564,3453454,[345345345,465645]]
# Works OK

# Test 6: Passing a list of floats.
# a6=[45.0,23.4,555,23232]
# Works OK

# Test 7: Passing a list of strings.
# a7 = ["adds","sjdhn","sdhnsjfkshm"]
# Works OK

# Test 8 : Mixed array of ints and bytes
#a= np.array([[555, 3453], [b'\xFF', b'\x0b'], [b'\x0c', b'\xff']], dtype="S1")
# Works OK

# Test 9: Normal 1-D numpy array passed.
# a=np.array([b'\xAA',b'\xAB',b'\xAF'],dtype="S1")
# Works OK

# Test 10: passing a numpy array of integers.
# a=np.array([1,2,3,4,4,5,6,250])
# Works OK

# Test 11: passing a numpy array/matrix of integer values where some values not in the range [0,255]
# a = np.array([[5456,564564],[345345345,465645]])
# Works OK

# Test 12: passing a numpy array/matrix of integer values where shape of matrix not proper / rectangular
# a = np.array([5456,564564,[345345345,465645]])
# ValueError: setting an array element with a sequence.(Non-critical : Error occurs in caller function, not called function)

# Test 13: Passing a numpy array of floats.
# a=np.array([45.0,23.4,555,23232])
# Works OK

# Test 14: Passing a numpy array of strings.
# a = np.array(["adds","sjdhn","sdhnsjfkshm"])
# Works OK

#print(type(a[0,0]))
RasPiUtilities.RasPiUtilities.array_to_file(a,"Data1.txt")
