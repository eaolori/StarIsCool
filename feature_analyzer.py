name = "  Esthe Olori  "
age = 25
favorite_language = "Python"
favorite_color = "Green"

name = name.strip()

print("PROFILE ANALYZER")
print()
print(f"Name: {name}")
print(f"Username: {''.join(name.lower().split())}")
print(f"Name length: {len(name)}")
print(f"First initial: {name[0]}")
print(f"Last character: {name[-1]}")
print(f'Has "{favorite_language}": {'Python' in favorite_language}')
print(f"Language: {favorite_language.upper()}")
print(f"Language length: {len(favorite_language)}")
print(f"Next year: {age + 1}")
