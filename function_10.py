#function-> block of statement that perfrom a specific task

#SYNTAX OF FUNCTION


# def func_name(parameter1,paramter2.....):  this is function defintionqz
         #some work
        #return val
#function_name(arg1,arg2...) this is a function call


#adding two number 
def sum(a,b):
    s=a+b
    print(s)
    return s
n=int(input("enter n"))
m=int(input("enter m"))
sum(n,m)


#FACTORIAL OF  A NUMBER 

def fac(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
    return fact
n=int(input("enter n "))
fac(n)


#find maximum of three number 
def max(n,m,x):
    if n>m and n>x:
        print(n)
    elif m>n and m>x:
        print(m)
    else:
        print(x)


n=int(input("enter n "))
m=int(input("enter m "))
x=int(input("enter x "))
max(n,m,x)

#check if a number is even or odd
def even_odd(n):
    if n%2==0:
        print("even no")
    else:
        print("odd no ")    
n=int(input("enter n "))
even_odd(n)


#there are two types of functions in python 
#1)built in function -> print(),len(),type(),range()
#2)user-defined function 

#convert USD TO INR 
def converter(usd_val):
    inr_val=usd_val*83
    print(usd_val,"USD=",inr_val,"INR")

converter(1)
 