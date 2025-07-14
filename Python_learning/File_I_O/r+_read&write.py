f = open("C:\\python\\Python_learning\\File_I_O\\demo.txt", "r+")  # Opening the file in read and write mode
data = f.read()  # Reading the file content
print(data)  # Printing the content of the file
f.close()  # Closing the file after writing and reading
