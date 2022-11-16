numday = int(input("Enter the number of days: "))
total = 0
temp = []
for i in range(numday):
    numday = int(input("Day"+str(i+1)+" 's high temparature: "))
    temp.append(i)
    total=temp[i]

avg= round(total/numday,2)
print("\n average= "+str(avg))
above = 0
for i in temp:
    if i>avg:
        above+=1
print(str(above)+"day(s)' temparature is higher that average temparature")
