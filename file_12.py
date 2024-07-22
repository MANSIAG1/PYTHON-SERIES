#python can be used to perform operation on a file 

#types of all files 
#1)text file -> .txt , .docx , .log etc
#2)binary files->.mp4 , .mov , .png , .jpeg etc 


#we have to open read and close file 
#so we have to open a file before reading or writing 

#syntax -> f=open("file_name ", "mode ")
 
#if we caannot tell any mode toh python assume that we open a fle in read mode

f=open("demo.txt","r")
data=f.read()
print(data)
print(type(data))
f.close()


# "r"->open for reading(default)
# "w"->open for writing,truncating the file first means overwrite 
# "x"->creates a new file and open it for writing
# "a"->open for writing,appending to the end of file is it exists
# "b"->binary mode 
# "t"->text mode (default)
# "+"->open a disk for updating(read and writting )

#if we want to read only one line then we use readline() method
f=open("demo.txt","r")
data=f.readline()
print(data)


f=open("demo.txt","w")
f.write("python programming") #this data add into demo.txt 


f.close()

#perform reading and writing both 
f=open("demo.txt","r+")
f.write("abc")
print(f.read())
f.close()




f1=open("demo.txt","a+")
print(f.read())
f.write("mansi , you are okay ")
f.close()




