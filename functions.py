#Factorial Function
n = int(input("Enter the number : "))
def factorial(n):
    i = 1
    fact = 1
    for i in range(1, n+1):
        fact *= i
        i += 1
    print("The factoiral of entered number is :", fact) 


factorial(n)



#Function to convert USD to INR
 
dollar = float(input("Enter the USD amount to be converted :"))
sum = 0
def usd_to_inr(dollar):
    sum = 80.76 * dollar
    print("Amount in INR", sum)

usd_to_inr(dollar)


#Function to find entered number is odd or even

num = int(input("Enter the number : "))

def odd_OR_even(num):
    if(num % 2 == 0):
        print("Entered Number is EVEN")
    else:
        print("Entered Number is ODD")

odd_OR_even(num)
