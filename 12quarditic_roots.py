import cmath

a=int(input("Enter a number(a!=0) : "))
b=int(input("Enter b number: "))
c=int(input("Enter c number: "))

# ax**2 + bx + c

d=(b**2)-(4*a*c)

root1 = (-b-cmath.sqrt(d))/(2*a)
root2 = (-b+cmath.sqrt(d))/(2*a)

print('First root of the equation is: ',root1)
print('Second root of the equation is: ',root2)