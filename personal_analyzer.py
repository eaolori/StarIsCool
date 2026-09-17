name = input("What is your full name? ")
name = name.strip()
age = int(input("How old are you? "))
height = float(input("How tall are you? "))
is_learning = True
favorite_language = input("What is your favorite programming language? ")
favorite_color = input("What is your favorite color? ")

# name_display = "Name: "
# name_display += name
# print(name_display)

# age_display = "Age: "
# age_display += str(age)
# print(age_display)

#Part 1
profile_summary = "Name: " + name + "\n"
profile_summary += "Age: " + str(age) + "\n" 
profile_summary += "Height: " + str(height) + "\n" 
profile_summary += "Learning Python: " + str(is_learning) + "\n"
profile_summary += "Favorite Language: " + favorite_language + "\n" 
profile_summary += "Favorite Color: " + favorite_color
print(profile_summary)

#Part2
def analyze_name(name):
    return (
        f"NAME ANALYSIS \n"
        f"Name: {name} \n"
        f"Length: {len(name)} \n"
        f"First character: {name[0]} \n"
        f"Last character: {name[-1]} \n"
        f"Contains Olori: {'Olori' in name}"
        f"Username: {''.join(name.lower().split())}"
    )
result = analyze_name()
print(result)