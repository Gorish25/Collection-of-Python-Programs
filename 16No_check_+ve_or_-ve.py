no=int(input("Enter a number to check: "))

def checking(no):
    if no<0:
        print('Negative Number')
    elif no==0:
        print('Zero')
    else:
        print('Positive Number')

checking(no)