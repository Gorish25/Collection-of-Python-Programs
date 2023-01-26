a=int(input("Enter number one: "))
b=int(input("Enter number two: "))

choice=int(input("Enter 1 (for addition), 2 (for subtraction) 3 (for multiplication) 4 (division) "))

if choice==1:
    print(a+b)
elif choice==2:
    print(abs(a-b))
elif choice==3:
    print(a*b)
elif choice==4:
    print(a/b)
else:
    print('wrong choice')