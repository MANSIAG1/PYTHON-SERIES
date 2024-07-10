# Printing simple messages
print("hiiii ")
print("this is mansi agarwal")

# Performing arithmetic operations and printing the result
a = 20  # Assigning the value 20 to variable 'a'
b = 30  # Assigning the value 30 to variable 'b'
result = a + b  # Adding the values of 'a' and 'b' and storing the result in 'result'
print(result)  # Printing the value of 'result', which is the sum of 'a' and 'b'

# Printing a number directly
print(23)

# Working with variables of different types
name = "mansi agarwal"  # Assigning a string value to variable 'name'
age = 20  # Assigning an integer value to variable 'age'
price = 2344.56  # Assigning a float value to variable 'price'
print(name, age, price)  # Printing the values of 'name', 'age', and 'price'

# Checking the types of variables
print(type(name))  # Printing the type of the variable 'name', which is <class 'str'>
print(type(age))  # Printing the type of the variable 'age', which is <class 'int'>
print(type(price))  # Printing the type of the variable 'price', which is <class 'float'>


#datatypes
#integers
#string
#float,boolean,none
#boolean return True or False
age=23
old=False
a=None
print(type(old))
print(type(a))


#Keywords- reserved words in python 
#while writing keywords they are case-sensitive 

#TYPES OF OPERATOR 
#Arithmetic operator(+,-,/,%,**)
#relational/comparison operator(==,!=,>,<,<=,>=)
#assignment operator(=,+=,*=,/=,%=)
#logical operator(not,and,or)

a=5
b=4
sum=a+b
print(sum)
diff=a-b
print(diff)
multi=a*b
print(multi)
divide=a/b
print(divide)
print(a%b) #remainder
print(a **b)#power calculate

#relational 
a=5
b=4
print(a==b) #return false
print(a!=b)  #return true
print(a>b)
print(a<b)


#aasignment operator
num=10
num+=10
num/=10
num*=10
print("num:",num)

#logicaloperator - work on boolean expression
print(not False)
print(not True)
a=50
b=90
print(not(a<b))

#   AND operator work on two values 
val1=True
val2=False
print("ans operator:",val1 and  val2)
print("ans operator",val1 or val2)


#type conversion 
a=2
b=4.86
print(a+b)

a=1
b="2"
c=int(b)
sum=a+c
print(sum)

a=3.14
a=str(a)
print(type(a))