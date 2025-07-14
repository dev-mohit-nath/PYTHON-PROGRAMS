# with open("C:\python\Python_learning\File_I_O\demo.txt", "r") as f:  # Opening the file in read mode
#     data = f.read()  # Reading the file content
#     print(data)  # Printing the content of the file

with open("C:\\python\\Python_learning\\File_I_O\\demo.txt", "w") as f:  # Opening the file in write mode
    f.write("Python is simple syntex language and easy to learn.\n")  # Writing a new line to the file
    f.write("Python and javascript is most powerful programming language.\n")  # Appending
    f.write("Python is server side scripting language.\n")  # Writing another line to the file