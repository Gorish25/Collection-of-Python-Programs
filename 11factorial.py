num=int(input("Enter the numnber for factorial : "))

def factorial(num):
    factorial=1
    if num<0:
        print('Factorial does not exist for negative numbers')
    elif num==0:
        print('The factorial is 1')
    else:
        for i in range(1,num+1):
            factorial=factorial*i
        print(f'The factorial of {num} is {factorial}')

factorial(num)