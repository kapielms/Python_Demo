from numpy import *

arr1 = array([1,2,3,4,5])
arr2 = array([6,7,8,9,10])

list =[]
e=0
for i in range(len(arr1)):
    list.append((arr1[i]+arr2[e]))
    e+=1
    print(array(list))