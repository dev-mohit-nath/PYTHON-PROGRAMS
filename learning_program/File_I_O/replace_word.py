words = ["Donkey ", "hello", "good", "but", "nice"]

with open("C:\python\learning_program\File_I_O\example.txt", "r") as f:
    content = f.read()
for word in words:
    content = content.replace(word, "#" * len(word))

with open("C:\python\learning_program\File_I_O\example.txt", "w") as f:
    f.write(content)
    