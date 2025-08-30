
while True:
    num1 = float (input ("Enter first number :"))
    optr = input ("Enter operator(+,-,*,/):")
    num2 = float (input("Enter second number :")) 
    if optr == "+" : print (num1+num2)
    elif optr == "-": print(num1-num2)
    elif optr == "*": print (num1 * num2)
    elif optr == "/": print (num1/num2 if num2 !=0 else ("cannot divide by zero1"))
    else: print ("operator to daal!")
    if input ("continue? (y/n): ") !="y":break
    