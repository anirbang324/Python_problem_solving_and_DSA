def arrayStringsAreEqual(word1, word2):
    new1 = ''.join(word1)
    new2 = ''.join(word2)
    if (new1 == new2):
        return True
    else:
        return False

mylist1=list(map(str, input("Enter the list elements separated by space ").strip().split()))
mylist2=list(map(str, input("Enter the list elements separated by space ").strip().split()))
print(arrayStringsAreEqual(mylist1,mylist2))