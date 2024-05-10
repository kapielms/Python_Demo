
def fact(num):
    fact =1
    if (num < 0):
        print ("Please Enter a Number Greater then Zero")
    elif(num ==0):
        print ("Factorial of number Zero Is 1")
    else:
        for i in range(1,num + 1):
            fact =fact * i
            print(fact)
        return fact

num = int(input("Enter the Number"))
result = fact(num)
