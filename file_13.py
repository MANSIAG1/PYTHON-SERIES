#with keyword syntax

with open("demo1.txt","r") as f:
    data=f.read()
    print(data)


with open("demo1.txt","w") as f:
    f.write("hola amigoo")
    f.close()    


#DELETING A FILE ->USING THE OS MODULE 

#MODULE(LIKE A CODE LIBRARY)IS A FILE WRITTEN BY ANOTHER PROGRAMMER THAT GENERALLY HAS A FUNCTION WE CAN USE 

import os
os.remove("demo1.txt")