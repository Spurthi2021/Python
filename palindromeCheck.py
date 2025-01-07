#Program to check if the entered string is Palindrome

String1 = input("Enter the String : ")

String2 = String1[::-1]
print(String2)

if ( String1 == String2 ):
    print("Entered String is Palindrome")
else:
    print("Entered String is not a Palindrome")



#Program to check if the entered list is Palindrome

list1 = list(input("Enter the List : "))
print(list1)

cplist = list1.copy()
cplist.reverse()
print(cplist)

if (cplist == list1):
    print("Palindrome List")
else:
    print("Not a Palindrome List")
