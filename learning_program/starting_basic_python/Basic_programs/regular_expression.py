import re

# Text to search
text = "Hello, my email is mohitgoswami@gmail.com"

# Proper email regex pattern
pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

# Search for pattern
match = re.search(pattern, text)

# If match found, print it
if match:
    print("Email Found:", match.group())
else:
    print("No email found.")
