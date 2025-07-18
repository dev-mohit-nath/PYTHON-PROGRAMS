def find_string_in_file():
    word = input("Enter the word to find in the file: ") 
    with open("C:\python\Python_learning\File_I_O\practic.txt", "r") as f:  # Opening the file in read mode
        data = f.read()  # Reading the updated file content
        if (data.find(word) != -1):
            print("found")
        else:
            print("not found")        
        
find_string_in_file()  # Calling the function to find the string in the file
