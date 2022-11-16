import numpy

myarray = numpy.array([[1,2,3,4],[5,6,7,8]])
def travserse(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])
travserse(myarray)