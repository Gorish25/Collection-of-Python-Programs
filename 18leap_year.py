year=int(input("Enter the year to check for leap year:"))

def leap(y):
    if (y%400==0) and (y%100==0):
        print(f"{y} is a leap year")
    elif (y%4==0) and (y%100!=0):
        print(f'{y} is a leap year')
    else:
        print(f'{y} is not a leap year')

leap(year)