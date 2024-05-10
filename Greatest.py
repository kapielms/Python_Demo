num1 = int(input("Enter the Number 1: "))
num2 = int(input("Enter the Number 2: "))
num3 = int(input("Enter the Number 3: "))

if (num1 > num2 and num3):
    print("Number 1 is Greatest of all")
elif (num2 > num3 and num1):
        print("Number 2 is Greatest of all")
elif (num3 > num1 and num2):
    print("Number 3 is Greatest of all")
else:
    print("All numbers are equal")