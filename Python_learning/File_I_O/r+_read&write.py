f = open("C:\\python\\Python_learning\\File_I_O\\demo.txt", "r+")  # Opening the file in read and write mode
f.write("Python is simple syntex language and easy to learn.\n")  # Writing a new line to the file
data = f.read()  # Reading the file content
data1 = f.write("\nPython and javascript is most pover full programming language.\n")  # Appending another line
print(data)  # Printing the content of the file
f.close()  # Closing the file after writing and reading
