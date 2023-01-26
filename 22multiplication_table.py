num=int(input("Enter the number for multiplication table: "))

def multiplication_table(num):
    for i in range(1,11):
        print(f'{num} * {i} = {num*i}')

multiplication_table(num)