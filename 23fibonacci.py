number=int(input('Enter the range for fibonacci series: '))

def fibo(n):
    a,b=0,1

    if n<0 and n==0:
        print('Error, Give the correct length')
    elif n==1:
        print(a)
    elif n==2:
        print(a,b)
    else:
        print(a,b,end=' ')
        sum=0
        for i in range(n-2):
            sum=a+b
            print(sum,end=' ')
            a=b
            b=sum

fibo(number)