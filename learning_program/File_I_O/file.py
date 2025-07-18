str = "you are grate boy it will be try the perfum"

f = open("example.txt", "r")
content = f.read()

if "mohit" in content:
    print("the word is persent in the content")
else:
    print("the word is not persent in the content")
f.close()