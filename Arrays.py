import os
import numpy as np

def ArrayOut()-> None:
    os.system('cls')
    myArray = np.array([1, 2, 3, 4, 5, ])
    print(myArray)
    print(myArray.min())
    num :int = 10

ArrayOut()