origin=int(input("Enter the starting position: "))
end=int(input('Enter the ending position: '))

def armstrong_range(start, end):
    for i in range(start, end+1):
        original=i
        power=len(str(i))
        sum=0
        temp=i
        while temp>0:
            digit=temp%10
            sum+=digit**power
            temp//10
        if original==sum:
            print(f'Armstrong Number: {original}')

armstrong_range(origin,end)