count = 0
with open("C:\python\Python_learning\File_I_O\practic.txt", "r") as f:  
    data = f.read()  # Reading the file content
    # print(data)  # Printing the content of the file
    
    # num = ""
    # for i in range(len(data)):
    #     if data[i] == ",":
    #         print(int(num))
    #         num = ""
    #     else:
    #         num += data[i]
    num = data.split(",")
    for val in num:
        if int(val) %2 == 0:
            count += 1
print("Total even numbers in the file:", count)  # Printing the count of even numbers
        