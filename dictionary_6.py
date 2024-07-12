#DICTONARIES->Dictionaries are used to store data values in key:value pairs KEY : value

# They are unordered, mutable(changeable) & don’t allow duplicate keys

# Creating a Dictionary
info = {
    "key": "value",
    "name": "Krishna",
    "age": 20
}
print(info)

# Accessing Values
print(info["name"])  # Output: Krishna
print(info["age"])   # Output: 20

# Modifying Values
info["name"] = "Mansi"
print(info)

# Creating an Empty Dictionary
null_dict = {}
print(null_dict)

# Creating a Nested Dictionary
student = {
    "name": "Mohenjo",
    "age": 87,
    "subject": {
        "phy": 45,
        "chem": 89
    }
}
print(student)

# Accessing Values in a Nested Dictionary
print(student["subject"]["phy"])  # Output: 45

#DICTIONARY METHODS 

dict={
    "name":"mansi agarwal",
    "age":19,
    "hobbies":"movies",
    "aim":"healthy and wealthy life"
}
print(dict) #{'name': 'mansi agarwal', 'age': 19, 'hobbies': 'movies', 'aim': 'healthy and wealthy life'}

print(dict.keys()) #dict_keys(['name', 'age', 'hobbies', 'aim'])
print(dict.values()) #dict_values(['mansi agarwal', 19, 'movies', 'healthy and wealthy life'])

print(list(dict.keys())) #['name', 'age', 'hobbies', 'aim']

print(dict.get("name"))  #mansi agarwal

#update 
new_dict={"city" : "delhi"}
dict.update(new_dict)
print(dict)  #{'name': 'mansi agarwal', 'age': 19, 'hobbies': 'movies', 'aim': 'healthy and wealthy life', 'city': 'delhi'}


