#loops=> is used to repeat instructions  
#syntax of while loop

#while condition:
#     #some work
    
# while True :
#     print("hello")  #infinite loop   


count=1
while(count<=10):
    print("hello")
    count+=1
print(count)    

i=1
while(i<=5):
    print("hello world",i)
    i+=1    
    
    
#q1)print no from 1 to 100
i=1
while(i<=100):
    print(i)  
    i+=1
print("loop ended ")    
    
    
#q2)print multiplication of a table n
n=int(input("enter any number "))
i=1
while(i<=10):
    print( n*i)
    i+=1
print("loop ended")    
    
    
#q3)print the square of a number until 10 
i=1
while(i<=10):
    print(i*i)
    i+=1
print("loop ended")

#q4) search for a number x in this tuple using loop
#(1,4,9,16,25,36,49,64,81,100)
tuple=(1,4,9,16,25,36,49,64,81,100)
x=36
i=0 #initalization
while(i<len(tuple)):
    
    if(tuple[i]==x):
        print("found at index ",i)
    i+=1 #updation 
    
    
#BREAK AND CONTINUE KEYWORD
#break- use to terminate the loop when encountered 
#continue-terminate execution of current iteration and continue iteration of next iteration 

i=1
while(i<=5):
    if(i==3):
        break
    i+=1
print("loop ended")


i=0
while(i<=5):
    if(i==3):
        i+=1
        continue #skip 
    print(i)
    i+=1
print("loop ended")    





    
    

