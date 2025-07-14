info = {
    "name": "Mohit",
    "age": 20,
    "city": "Delhi",
    "hobbies": ["reading", "coding", "gaming"], # List of hobbies
    "is_student": True,
    "grades": {"math": 90, "science": 85, "english": 88}, # Dictionary of grades
    "courses": ["Python", "Java", "C++"],
    "skills": {"programming": ["Python", "Java"], "soft_skills": ["communication", "teamwork"]}, # Dictionary with nested list
    "experience": 2,  # Years of experience
    "projects": [  # List of dictionaries
        {"name": "Web Development", "duration": "3 months"},
        {"name": "Data Analysis", "duration": "2 months"}
    ], 
    "languages": ["English", "Hindi"],
    "favorite_numbers": [7, 14, 21],
    "pets": None,  # None value
    "birthdate": "2003-05-15",
    "address": {    # This is a nested dictionary
        "street": "123 Main St",
        "city": "Delhi",
        "state": "Delhi",
        "zip_code": "110001"
    }
}
print("info:", info)
info["hobbies"].append("traveling")
info["grades"]["math"] = 95
info["name"] = "Mohit Goswami"
print("Updated info:", info)
info["courses"].remove("Java")
print("Courses after removal:", info["courses"])
print("Favorite numbers:", info["favorite_numbers"]) 
info["projects"].append({"name": "Machine Learning", "duration": "4 months"})
print("\n") 
info.update({"certifications": ["Python Basics", "Data Science"]})  # Adding a new key-value pair
print("Updated info with certifications:", info)
print(info.keys())  # Print all keys in the dictionary
print(info.values())  # Print all values in the dictionary
print(info.items())  # Print all key-value pairs in the dictionary
print(info.get("name"))  # Print all key-value pairs in the dictionary