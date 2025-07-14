f =  open("C:\python\Python_learning\File_I_O\demo.txt", "r") # Opening the file in read mode
# line1 = f.readline() # Reading the first line
# print(line1) 
# line2 = f.readline() # Reading the second line
# print(line2)
data = f.read()
print(data)  # Reading the rest of the file
f.close()  # Closing the file after reading
