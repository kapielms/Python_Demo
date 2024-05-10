num = int(input("Enter the Year :  "))

if (num % 400 == 0 or num % 100 != 0 and num % 4 == 0  ):

    print ("Year is leap Year") 
else:
    print ("Year is not Leap Year")

