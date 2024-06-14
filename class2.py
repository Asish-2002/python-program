name = "asish"
age= 23
salary=22000.00
onTime= False
a = None

# print(type(name))
# print(type(age))
# print(type(salary))
# print(type(onTime))
# print(type(a))

# comments
# single line comments 

"""
today is a day
we just learn python
do some code 
"""
    
# print a sum of two numbers
a=10
b=20
sum = a + b
print("my total sum is:",sum)

#opertor
#arithmatic operator

a = 5
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

#relational operator

a=50
b=20
print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)

#assignment operator
num=10
num= num+10
print("num:",num)

#logical operator

val1= True
val2= False
print("AND operator:", val1 and val2) #it takes both val1  and val2 -false
print("OR opertor:", val1 or val2) #it takes both both val1 or val2-true

# true + true= true
# true + false= false
# false + false = false
# false + true= false

#input

#write a program to input 2 numbers and print their sum .

a = int(input("enter a number"))
b = int(input("enter another number"))
sum = a + b

print("the sum of the two numbers is:",sum)


#write a program to input side of a square and print its area.

side = float(input("enter the side of the square"))
area = side * side 

print("the area of the square is:",area)

# write a progrm to input 2 floating point numbers and print their average.


a = float(input("enter a float number"))
b = float(input("enter another float number"))
avg = (a + b) / 2

print("the average of two numbers is:",avg)


# write a program to input 2 int numbers a & b, print true if a is greater then or equal to b. if not print false.

a = int(input("enter a number"))
b = int(input("enter another number"))
if(a >= b):{
    print("true")
}
else:{ 
    print("false")
}