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
        f"---------------- \n"
        f"Name: {name} \n"
        f"Length: {len(name)} \n"
        f"First character: {name[0]} \n"
        f"Last character: {name[-1]} \n"
        f"Contains Olori: {'Olori' in name} \n"
        f"Username: {''.join(name.lower().split())}"
    )
# result = analyze_name(name)
# print(result)

def analyze_language(favorite_language):
    return (
        f"LANGUAGE ANALYSIS \n"
        f"---------------- \n"
        f"Language: {favorite_language} \n"
        f"Uppercase: {favorite_language.upper()} \n"
        f"Lowercase: {favorite_language.lower()} \n"
        f"Length: {len(favorite_language)} \n"
        f"Starts with Py: {favorite_language.startswith('Py')} \n"
        f"Ends with on: {favorite_language.endswith('on')}"
    )
# result = analyze_language(favorite_language)
# print(result)

#3
income = float(input("How much do you make in a month? "))
food = float(input("How much do you spend on food monthly? "))
transport = float(input("How much do you spend on transport monthly? "))
other = float(input("How much do you spend on miscellaneous? "))

def analyze_finances(income, food, transport, other):
    total_expenses = food + transport + other
    balance = income - total_expenses
    savings_percentage = balance / income * 100
    annual_income = income * 12
    daily_average = total_expenses / 30

    return (
        f"FINANCIAL ANALYSIS \n"
        f"------------------ \n"
        f"Monthly income: {income} \n"
        f"Food expenses: {food} \n"
        f"Transport expenses: {transport} \n"
        f"Other expenses: {other} \n"
        f"\n"
        f"Total expenses: {total_expenses: .2f}\n"
        f"Remaining money: {balance} \n"
        f"Savings percentage: {savings_percentage: .2f}% \n"
        f"Annual income: {annual_income: .2f} \n"
        f"Average daily spending: {daily_average: .2f}"
    )
# result = analyze_finances(income, food, transport, other)
# print(result)

def generate_report(name, favorite_language, income, food, transport, other):
    name_report = analyze_name(name)
    language_report = analyze_language(favorite_language)
    financial_report = analyze_finances(income, food, transport, other)

    return (
        f"================================ \n"
        f"PERSONAL LIFE ANALYZER \n"
        f"================================ \n"
        f"{name_report} \n"
        f"\n"
        f"{language_report} \n"
        f"\n"
        f"{financial_report}"
    )
result = generate_report(name, favorite_language, income, food, transport, other)
print(result)