num=int(input("Enter the number for which the you want sum: "))

def sum(n):

    if n>0:
        s=0
        for i in range(1,n+1):
            s+=i
        print(f'The sum upto {n} Natural Numbers is {s}')
    else:
        print('Please give a positive number or greater than 0')

sum(num)