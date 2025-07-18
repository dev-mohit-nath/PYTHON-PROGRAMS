#writing to a file
with open("example.txt","w") as file:
    file.write("this is a file handling exepent.\n")
    
    file.write("we are writting to a file.\n")
    
#Appending to the file

with open("example.txt","a")as file:
    file.write("This line is append.\n")
    
#Reading from the file
with open("example.txt","r")as file:
    content =file.read()
    print("Content of the file")
    print(content)