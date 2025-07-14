def searching_word_in_file():
    word = input("Enter the word to find in the file: ")  # Prompting user for the word to search
    line_no = 1
    data = True
    with open("C:\python\Python_learning\File_I_O\practic.txt", "r") as f:  # Opening the file in read mode
        while data:
            data = f.readline()
            if word in data:
                print(line_no)
                return
            line_no += 1
    return -1
                
print(searching_word_in_file())  # Calling the function to search for the word in the file               
            