
# using for loop
for i in range(1,100):
    if i%13==0:
        print(i,end=' ')

print()

# using lambda
result=list(filter(lambda x:x%13==0,range(1,100)))
print(result)


# using a given list
l=[39,48,26,98,33,67,87]
result2=list(filter(lambda x:x%13==0,l))
print(result2)