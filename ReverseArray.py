from array import *

Arr= array('i',[])

num = int(input("Enter the Number of Array Element"))

for i in range(num):
    y= int(input("Enter the Element"))
    Arr.append(y)
print(Arr)

reversed_Arr = Arr[::-1]
print("Reversed Array",reversed_Arr)


    