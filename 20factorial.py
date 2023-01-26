num=int(input("Enter the number to find factorial: "))

def factorial(num):
    if num==0:
        print(f'Factorial of {num} is 1')
    elif num==1:
        print(f'Factorial of {num} is 1')
    elif num<0:
        print('Sorry Negative Numbers do not have factorial')
    else:
        fact=1
        for i in range(1,num+1):
            fact=fact*i
        print(f'Factorial of {num} is {fact}')

factorial(num)