# Code to find the positive integer among 2 numbers user entered
# Used both AND , OR Logic operators and comparison operators

a=int(input('Enter the 1st number: '))
b=int(input('Enter the 2nd number: '))

if a>0 and b>0:
    print('Both the numbers are positive')
elif a<0 and b<0:
    print('Both the numbers are negative')
elif a>0 and b<0:
    print(a,"is Positive and",b,"is negative")
elif a<0 and b>0:
    print(b,"is Positive and",a,"is negative")
elif a==0 or b==0:
    if a==0 and b!=0:
        print(a, "is neither positive nor negative")
        if b>0:
            print(b,"is positive")
        else:
            print(b,"is negative")
    else:
        print(b, "is neither positive nor negative")
        if a > 0:
            print(a, "is positive")
        else:
            print(a, "is negative")
