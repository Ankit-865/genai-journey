#Check if a number is even or odd
i= int (input("enter a number"))
if (i%2==0):
    print ("no is even")

else :
    print ("no is odd")

#Print first 10 natural numbers

for i in range (1,11):
    print (i)

#Sum of numbers in a list

list = [1,10,20,15]
total= 0
for list in list :
    total += list 
print (total)
 


#Factorial using loop
a= 6
fact = 1
for i in range (1, a+1):
    fact *=i
    print (fact)


#Write a function that returns the square of a number

def square(num):
    return num * num
result = square(4)
print(result)  
