a,b=input("Enter 2 numbers using comma(,) : ").split(',')
a=int(a); b=int(b);

def swapping(a,b):
    print(f'before swapping a is {a} and b is {b}')
    temp=a
    a=b
    b=temp
    print(f'after swapping a is {a} and b is {b}')


def swap(a,b):
    print(f'before swap a is {a} and b is {b}')
    a,b=b,a
    print(f'After swap a is {a} and b is {b}')

swapping(a,b)
swap(a,b)