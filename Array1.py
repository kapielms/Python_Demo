from array import *

num = array('i',[])
n=int(input("Enter the number for Array: "))

for i in range(n):
    y = int(input("Enter the number: "))
    num.append(y)
    print(num)

search =int(input("Enter the number to search: "))
k=0
for e in num:
    if (e==search):
        print (k)
        break
    k+=1
