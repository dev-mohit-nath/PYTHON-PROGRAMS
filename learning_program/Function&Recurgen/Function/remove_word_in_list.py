def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
    
l = ["mohit","rohan", "hit", "rahul","prince", "rohit", "pankaj"]

print(rem(l, "hit"))