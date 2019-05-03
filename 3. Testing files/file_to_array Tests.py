import RasPiUtilities
import numpy as np

a3=RasPiUtilities.RasPiUtilities.file_to_array("Data1.txt")
print(a3)
print(type(a3))
print(type(a3[0,0]))

a= np.array([[b'\xAA', b'\xBB'], [b'\xFF', b'\x0b'], [b'\x0c', b'\xff']], dtype="S1")

print(type(a[0,0])==type(a3[0,0]))

