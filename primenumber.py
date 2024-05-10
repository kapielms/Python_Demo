num =int(input("Enter the Numner :"))

for i in range (2,num):
    if num % i ==0:
        print ("The number is not a prime number")
        break
else:
    print ("The Number is Prime number")