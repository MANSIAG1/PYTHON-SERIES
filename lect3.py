#strings


str1="this is a string "
str2='this is a string 2'
str3=""""this is string 3"""
print(str1,str2,str3)

#escape sequence character-formatting 
str1="helooo.\nthis is mansi agarwal"
print(str1)

#concatenation of string 
str1="hello"
str2="world"
print(str1+str2)
print(len(str1+str2)) #return length of string 


#indexing in a string 

# A P N A C O L L E G E
# 0 1 2 3 4 5 6 7 8 9 10
# indexing count space also 

str="apna college"
ch=str[0]
ch2=str[1]
print(ch)
print(ch2)



#slicing -accesing part of string 
#formula - str[starting index : ending index] where ending index part is not included 

str="apna college"

print(str[1:4])
print(str[: 4]) #apna
print(str[1:]) # return pna college
# print(str[: 4])= this is same as str[0:4]
#print(str[1:]) is same as str[1:len(str)]

#string function
#1) endswith()
str="hello  welcome to apni kaksha"
print(str.endswith("sha")) #if yes then it will return true 

#2) str.capitalize
str="hello"
print(str.capitalize())

#3) str.replace(old,new)
str="i am studying python "
#if we want to replace  i with a 
print(str.replace("i" , "a"))

#4)str.find(word) - return 1st index of 1st occurence 

#5)str.count("am")- count the occurence of substring of string

#q1) wap to input user first name and print its length
str1=input("enter name")
print(str1)
print(len(str1))

#q2) wap to find occurence of $ in a string 
str="hi, $$$$$$$$$$hi i am $$$"
print(str.count("$"))










