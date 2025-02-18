a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=input("select the operation of your desire(+,-,*,/)")
def add(a,b):
    if (c=="+"):
        ("sum=",a+b)
def subtraction (a,b):
    if (a>b )and (c=="-"):
        print("difference=",a-b)
def multiplication(a,b):
    if (c=="*"):
        print("product=",a*b)
def division(a,b):
    if (c=="/") and (b!=0):
        print("quotient=",a/b)
    elif(b==0):
        print("ZeroDivisionError")
    
add(a,b)
subtraction(a,b)
multiplication(a,b)
division(a,b)
