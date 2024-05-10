string_Name = input("Please enter the Number:  ")
temp = string_Name
rev_String =""

for i in string_Name:
    rev_String = i + rev_String
if (temp.lower() == rev_String.lower()):
    print("The String is Palindrone")
else:
    print("The String is not palindrone")