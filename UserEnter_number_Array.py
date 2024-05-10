from array import *
from numpy import *

Arr_Num= ([])
num = int(input('Enter the Array : '))


for i in range(num):
    y = int(input("Enter the element : "))
    Arr_Num.append(y)
    
    print(Arr_Num)

num_max = Arr_Num([0])
num_min = Arr_Num([0])

for e in Arr_Num:
 if e > num_max:
   num_max = e
 if e < num_min:
     num_min = e

print (num_max)
print (num_min)
    
