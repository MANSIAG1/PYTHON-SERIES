#when a function calls itself repeatedly 

def fun(n):
    if(n==0):     #base case 
        return
    print(n)
    fun(n-1)
n=int(input("enter n "))        
fun(n)    


#factorial
def fact(n):
    if(n==1 or n==0):
        return 1
    else:
        return fact(n-1)*n  
n=int(input("enter n "))
print(fact(n))



#sum of digit 
def sum_of_digits(n):
    if n == 0:
        return 0
    else:
        return n % 10 + sum_of_digits(n // 10)
n=int(input("enter n"))
print(sum_of_digits(n))


#recursive fibonaaci 
def fib(n):
    if n<=0:
        return 0
    elif n==1:
        return 1
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter n"))
print(fib(n))