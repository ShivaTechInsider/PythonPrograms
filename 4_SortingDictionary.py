# Sort a List of Dictionaries by a Key

# Example dictionary
student = {
    "name": "John",
    "age": 21,
    "major": "Computer Science"
}


res = sorted(student,key=lambda x:x)
print(res)