from functools import reduce

num = [1,2,3,4,5,6,7,8,9]

even = list (filter(lambda a : a % 2 ==0,num))
print ('filter even number: ',even)

double= list (map(lambda a : a * 2 ,num))
print('Double the list number: ',double)

minus= reduce(lambda a,b: a-b,double)
print (minus)