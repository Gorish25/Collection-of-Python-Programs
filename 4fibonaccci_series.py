num=int(input('Enter the length for fibonacci numbers : '))

def fibo_using_loop(num):
    n1,n2=0,1
    sum=0
    if num<=0:
        print('Enter number greater than 1')
    else:
        for i in range(0,num):
            print(sum,end=' ')
            n1=n2
            n2=sum
            sum=n1+n2

fibo_using_loop(num)