from bot1 import spam_bot

with open("C:\python\Python_mini_projects\texts.txt","r") as txt:
    context = txt.read()
    for word in context.split(" "):
        print(word)
        spam_bot(word)
    