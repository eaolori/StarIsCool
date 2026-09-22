def validate_profile(name, age=18, language="Python"):
    name = name.strip()
    words = name.split()
    if len(words) >= 2:
        name_valid = True
    else:
        name_valid = False

    if age >= 18 and age <= 100:
        age_valid = True
    else:
        age_valid = False

    if language[0].isupper():
        language_valid = True
    else:
        language_valid = False

    username = name.lower().replace(" ", "")

    valid = name_valid and age_valid and language_valid

    return (
        f"Name: {name}\n"
        f"Username: {username}\n"
        f"Age: {age}\n"
        f"Language: {language}\n"
        f"Valid: {valid}"
    )
print(validate_profile("Star", 65, "JS"))
print(validate_profile("  Esther Olori  ", 34, "Python"))
print(validate_profile("John", 16, "python"))



#     if len(name) >= 2:
#         print(f"Name: {name}")
#     elif age <= 100 and age >= 18:
#         print(f"Age: {age}")
#     elif language :
#         print(f"Language: {language}")

# result = validate_profile("Star", 34, "Java")
# print(result)
#pyttsx3
    
    