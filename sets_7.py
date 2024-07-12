#sets-> is the collection of unordered items
# each element in the set is unique and mutuable means non changeable

nums={1,2,3,4}
set={1,2,2,2}
#repeated elements stored only at once in set 
print(nums) #{1,2,3,4}
print(set) #{1,2}

#empty set syntax
# collection=set()
# print(type(collection))

#set methods
set={1,2,3,4,2,3,5,6}
set.add(10)
print(set)

set.remove(2)
print(set)

set.pop()
print(set)

set1={1,2,3,4,5,6,7,"hello","hi"}
set2={2,3,4,7,9,"how are you"}
print(set1.union(set2))  #{1, 2, 3, 4, 5, 6, 7, 9, 'how are you', 'hello', 'hi'}
print(set1.intersection(set2))#{2, 3, 4, 7}

#q1)You are given a list of subjects for students. Assume one classroom is required for 1
#subject. How many classrooms are needed by all students.
#”python”
