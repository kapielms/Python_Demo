def evenOdd(list_num):
    even = 0
    odd = 0
    for e in (list_num):
        if (e % 2 == 0):
            even += 1   
        else:
            odd +=1
    return even, odd

num = int(input("Enter the number of list element:  "))
my_list = ([])

for i in range (num):
    a = int(input("Enter the number in the list: "))
    my_list.append(a)

print(my_list)

a,b = evenOdd(my_list)
print('Even :',a)
print('Odd :',b)
           