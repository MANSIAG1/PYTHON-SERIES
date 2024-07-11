#LISTS-> a built in data type that store set of values
# it can store different types of integer (int,float,str etc)

marks =[23,34,5,6,7,8]
marks[2]=67 # this is allowed in python 
print(marks)
print(len(marks))
print(marks[0])
print(marks[1])
print(marks[2])


student=["karan","arjun",29]
print(student)

#LIST SLICING -> this is similar to string slicing 
# str1=[starting index : ending index] #ending index is not include 

marks=[23,45,67,32,12,34,67,567]
print(marks[1:4])
print(marks[1 :])

#list methods
list=[1,3,2,4]
list.append(6)
print(list)

list.sort()
print(list)

list.reverse()
print(list)

#we have to insert element at index
list=[12,34,23,45,67,86]
# list.insert(index,element)
list.insert(6,10)
print(list)


list1=[2,1,3,1]
list1.remove(1)
print(list1)


#TUPLES IN PYTHON ->a built in data type that store set of values
#can store element of diff types(int,float,string etc)
#tuples can be denotes by '()'

tup=(23,56,78,99)
print(tup)
# tup[0]=23   #not allowed in python 


tup1=(2,1,3,1)
print(tup1.index(1)) #return index of first occurence 
print(tup1.count(1)) # count total occurence 


#q1) wap to check if a list contain a palindrome of elements 
list1=[1,2,1]
list2=[1,2,3]


copy_list1=list1.copy()
copy_list1.reverse
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")    

