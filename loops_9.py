#loops->are used for sequential traversal.For traversing list,string,list,tuples etc

#for loops 

string="hello world"
for el in string:
    print(el)
else:
    print("end")    


list=[1,2,3,4,5,6]
for el in list:
    print(el)


#found number 
list=[1,4,9,16,25,36,49,64,81,100]
x=36;i=0
for el in list:
    if(el==x):
        print("element found at index ", i)
    i+=1     



#range 
# range function return a sequence of no ,starting from 0 by default,and increments by 1
# (by default),and stops before a specified number
#SYNTAX OF RANGE 
# 
# 
#range(start? , stop , step?)
print(range(5)) #range(0,5)
# start=0 (by default), step size is basically ki hum kitne step size se increase krna chahte hai 
# stop=5 means 5 se phele end krdo

seq=range(5)
print(seq[0])  #0
print(seq[1])  #1
print(seq[2])  #2
print(seq[3])  #3
print(seq[4])  #4

#forloop
seq=range(5)
for i in seq:
    print(i)


#3 methods to write range 
#1st method 
seq1=range(5) #5 represent stop
for el in seq1:
    print(el)

#2nd method 
seq =range(1,5) # here 1 represnt start and 5 represent stop 
for el in seq:
    print(el) #1,2,3,4

#3rd method
seq=range(1,10,1)
#         start,stop,step
for el in seq:
    print(el)   


#print even numbers using range 
seq=range(2,100,2)
for el in seq:
    print(el)

#multiplication of n 
n=int(input("enter n "))
for i in range(1,11):
    print(n*i)


#WAP TO FIND SUM OF FIRST N NUMBER USING WHILE
n=5
sum=0
for i in range(n+1):
    sum+=i  
print(sum)    


#find factorial of a no 
n=int(input("enter n "))
fact=1
i=1
while(i<=n):
    fact=fact*i
    i+=1

print("th factorial of n is ", fact)   

#USING FOR LOOP
n=int(input("enter n "))
fact=1
i=1
for i in range(i,n+1):
    fact*=i
print("the factorial is ", fact)    








   