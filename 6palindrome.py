num=int(input('Enter the number to check palindrome or not'))

def check_palindrome(num):

    number=str(num)
    if num==int(number[::-1]):
        print('Palindrome ')
    else:
        print("not a palindrome")

check_palindrome(num)