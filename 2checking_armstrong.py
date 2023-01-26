num = int(input('Enter number to check for armstrong number'))

def check_armstrong(num):

    power=len(str(num))
    original=num
    sum=0

    while num>0:
        digit=num%10
        sum+=digit**power
        num=num//10

    if sum==original:
        print(f"Entered number {original} is an Armstrong number")
    else:
        print("Entered number is not an Armstrong number")

check_armstrong(num)