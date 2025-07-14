f = open("C:\\python\\Python_learning\\File_I_O\\demo.txt", "w+")  # Opening the file in write and read mode
f.write("Python is simple syntex language and easy to learn.\n")  # Writing a new line to the file
data = f.read()  # Reading the file content
data1 = f.write("\nPython and javascript is most powerful programming language.\n")  # Appending another line
print(data1)  # Printing the number of characters written
print(data)  # Printing the content of the file