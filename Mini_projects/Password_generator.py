import random
import string

pass_length = 12

charValues = string.ascii_letters + string.digits + string.punctuation 

password = "".join([random.choice(charValues) for i in range(pass_length)])
print("Generated Password:", password)

# password = ""
# for i in range(pass_length):
#     password += random.choice(charvalues)
# print("Generated Password:", password)