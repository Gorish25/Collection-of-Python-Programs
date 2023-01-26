num=int(input("Enter the number for finding factorial: "))

def factorial(num):
    if num<0:
        print("Negative numbers do not have any factorial")
    else:
        if num==0:
            return 1
        else:
            return num*factorial(num-1)

print(f'Factorial of {num} is {factorial(num)}')
    