import numpy as np
myarray = np.array([[11,12,13,14],[15,16,17,18],[21,22,23,24],[25,26,27,28]])
def searcharray(array,row,column):
    if row>len(array) and column>=len(array[0]):
        print("Incorrect")
    else:
        print(array[row][column])

searcharray(myarray,0,1)