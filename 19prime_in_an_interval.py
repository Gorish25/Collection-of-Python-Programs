a=int(input("Enter the origin number: "))
b=int(input("Enter the last number: "))

def primes(a,b):
    for num in range(a,b+1):
        if num>1:
            for i in range(2,num):
                if num%i==0:
                    break
            else:
                print(f'Prime Number: {num}')

primes(a,b)