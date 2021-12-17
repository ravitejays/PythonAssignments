print("Enter + for Addition, - for Subtraction, / for Division, * for Multiplication, ^ for Power")

n = str(input())
a = float(input("Enter the 1st number: "))
b = float(input("Enter the 2nd number: "))

def add(a,b):
        return a+b

def subtract(a, b):
    return a - b

def divide(a, b):
    return a / b

def multiply(a, b):
    return a * b

def power(a, b):
        return a**b

if n == '+':
        print("Result: ",add(a,b))
if n == '-':
        print("Result: ",subtract(a,b))
if n == '/':
        print("Result: ",divide(a,b))
if n == '*':
        print("Result: ",multiply(a,b))
if n == '^':
        print("Result: ",power(a,b))