num=int(input("Enter the number for finding the factors"))

def factors(num):
    for i in range(1,num+1):
        if num%i==0:
            print(i,end=' ')

factors(num)