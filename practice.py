num=int(input("Enter a number to check for armstrong number"))

def armstrong(n):
    original=n
    power=len(str(n))
    sum=0

    while n>0:
        digit=n%10
        sum+=digit**power
        n=n//10
    
    if original==sum:
        print("It's an Armstrong Number")
    else:
        print('No its not an Armstrong Number')

armstrong(num)