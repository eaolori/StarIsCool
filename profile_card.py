name = "  Esthe Olori  "
age = 25
height = 1.75
is_learning = True
favorite_language = "Python"
favorite_color = "Green"

#1
name = name.strip()  # Remove leading and trailing whitespace

#2
print(''.join(name.lower().split()))  # Convert to lowercase

#3
print(f"Name length: {len(name)}")
print(f"First character: {name[0]}")
print(f"Last character: {name[-1]}")
print(f"Contains Olori: {'Olori' in name}")

#4
print(f"Language: {favorite_language.upper()}")
print(f"Lowercase: {favorite_language.lower()}")
print(favorite_language.startswith('Py'))
print(favorite_language.endswith('on'))
print(favorite_language.count("P"))

#5
print(name.split())

#6
print(f"Name: {name}")
print(f"Username: {''.join(name.lower().split())}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Learning Python: {is_learning}")
print(f"Favorite Language: {favorite_language}")
print(f"Favorite Color: {favorite_color}")

#7
print(f"Next year, I will be {age + 1}.")