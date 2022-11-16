matrix = ([1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16])
number = 89
def searchfor(matrix, number):
    for row in matrix:
        for element in row:
            if element == number:
                return True
    return False

if searchfor(matrix, number):
    print("Found")
else:
    print("Not found")