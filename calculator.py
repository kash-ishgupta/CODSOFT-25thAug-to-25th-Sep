"""Let's create a basic calculator"""
a=int(input("Enter number1= "))
b=int(input("Enter number2= "))
operation=['+','-','*','/']
print("+,-,*,/")
operation=input("select the operation you wish to perform= ")
if operation=='+':
    print(a+b)
elif operation=='-':
    print(a-b)
elif operation=='*':
    print(a*b)
elif operation=='/':
    print(a/b)
else:
    print("INVALID INPUT")





