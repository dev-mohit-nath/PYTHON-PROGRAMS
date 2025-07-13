collection = {1, 2, 3, 4, 5} # A set collection
print("collection:", collection) # Set does not allow duplicates
print(type(collection)) # Displaying the type of collection
print("Length of collection:", len(collection)) # Displaying the length of the set

students = set() # Creating a set with integers
print("students:", students) # Displaying the set of students
print(type(students)) # Displaying the type of students set
students.add(6) # Adding an element to the set
students.add(2) 
students.add(5) 
students.add("mohit") 
students.add(50) 
students.add(11) 
print("Updated students:", students) # Displaying the updated set of students
students.remove(2) # Removing an element from the set
print("Students after removal:", students) # Displaying the set after removal
students.discard(50) # Discarding an element from the set
print("Students after discard:", students) # Displaying the set after discard
 # Clearing the set
print("Students after clear:", students) # Displaying the set after clearing
print("Length of students:", len(students)) 
students.clear()

print("Programming languages:")
languages = {"Python", "Java", "C++", "JavaScript"} # Creating a set of programming languages
print(languages) # Displaying the set of programming languages
languages.add("Ruby") # Adding a new language to the set
print("Languages after adding Ruby:", languages) # Displaying the set after adding Ruby
languages.remove("Java") # Removing Java from the set
print("Languages after removing Java:", languages) # Displaying the set after removing Java
languages.pop() # Removing an arbitrary element from the set
print("Languages after pop:", languages) # Displaying the set after pop
