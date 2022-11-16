def countConsistentStrings(allowed, words):
    count = 0
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] not in allowed:
                break
        else:
            count += 1
    return count

mylist= list(map(str, input("Enter the list elements separated by space ").strip().split()))
mystring = input()

print(countConsistentStrings(mystring,mylist))