#if-elif-else COMMAND 
#SYNTAX->


#if(conditon):
#    statement1
# elif(condition):
#     statement2
# else:
#     statement N   

# age=int(input("enter age "))
# if(age>=18):
#     print("can vote")
# else:
#     print("cannot vote")    
    

# marks=int(input("enter marks"))
# if(marks>=90):
#     print("grade a")
# elif(90>marks>=80):
#     print("grade b")
# elif(80>marks>=70):
#     print("grade c")
# else:
#     print("grade c")            


#q1) no entered by user is even or odd
num=int(input("enter the number"))
if(num%2==0):
    print("even no")
else:
    print("odd no")    


#q2) wap to find greatest of 3 no entered by user
a=int(input("enter first no"))
b=int(input("enter second no"))
c=int(input("enter third no"))
if(a>b and a>c ):
    print(a)
elif(b>c and b>a):
    print(b)
else:
    print(c)        
