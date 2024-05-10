
def palindrome(n):
    temp =n
    rev = 0
    while (n > 0):
        Dig = (n % 10)
        rev = rev * 10 + Dig
        n= n//10

    if (temp == rev):
        print ("The Given number is a Palindrome")
    else:
        print ("The Given number is not a Palindrome")

n = int(input("Enter the Number : "))
print(palindrome(n))