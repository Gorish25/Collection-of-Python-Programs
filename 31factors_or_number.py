num=int(input("Enter the number"))

def factors(n):
    l=[]
    for num in range(1,n+1):
        if n%num==0:
            l.append(num)
    return l

print(f'The factors of {num} is {factors(num)}')
