num=int(input("Enter the number for checking prime or not : "))

def check_prime(num):

    if num<2:
        print('Not a prime Number')
    else:
        for i in range(2,num):
            if num%i==0:
                print('Printed number is not a Prime number')
                break

        else:
            print(f'Number {num} is a prime number')

check_prime(num)