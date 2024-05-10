from array import *


num = ([1,2,3,4,5,8,6,7])
min_num = num[0]
max_num =num[0]

for i in num:
    if i < min_num:
        min_num = i
    if i > max_num:
        max_num = i


print (min_num)
print (max_num)


