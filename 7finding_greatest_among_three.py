a,b,c=input("Enter three number using comma (,) : ").split(',')
a=int(a); b=int(b); c=int(c);

def greater(a,b,c):
    if a>b and a>c:
        print(f'{a} is bigger')
    elif b>a and b>c:
        print(f'{b} is bigger')
    else:
        print(f'{c} is bigger')

greater(a,b,c)
