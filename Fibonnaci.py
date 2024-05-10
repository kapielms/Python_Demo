
def fib(n):
    n1 = 0
    n2 = 1
    sum =0
    if (n <=0 ):
        print ("Please enter the number greater then 0 ")
    else:
        for i in range(0,n):
            n1 = n2
            n2= sum
            sum =n1 + n2
            print (sum,end=" ")

n = int(input("Enter the number for Fibonacci: " ))
print(fib(n))









        