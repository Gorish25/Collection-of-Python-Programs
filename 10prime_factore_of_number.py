num=int(input("Enter the number"))

def prime_factors(num):

    for i in range(1,num+1):
        if num%i==0:
            for j in range(2,i):
                if i%j==0:
                    break
            else:
                print(i,end=' ')

prime_factors(num)