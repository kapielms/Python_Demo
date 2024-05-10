from array import *


Arr = array('i',[])

x = int(input("Enter the Arrays : "))

for i in range(x):
    y = int(input("Please enter the number: "))
    Arr.append(y)
print(Arr)

z = int(input("Enter the index to remove"))
k=0
for e in Arr:
    if (e == z):
        Arr.remove(z)
        print(Arr)
        k+=1
