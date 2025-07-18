
with open("C:\python\learning_program\File_I_O\example.txt", "r") as f:
    lines = f.readlines()
    
lineNo = 1
for line in lines:
    if "python" in line:
        print(f"python word is exist in file. line NO: {lineNo}")
        break
    lineNo += 1
    
else:
    print("python word is not exist in file.")
    