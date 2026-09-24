name = input("What is your full name? ")
age = int(input("How old are you? "))
language = input("What is your favorite programming language? ")
monthly_income = int(input("What is your monthly income? "))
food = int(input("What is your monthly food expense? "))
transport = int(input("What is your monthly transport expense? "))
miscellaneous = int(input("What is your other monthly expense? "))

def financial_analysis(monthly_income, food, transport, miscellaneous):
    monthly_expenses = food + transport + miscellaneous
    remainder = monthly_income - monthly_expenses
    
    if monthly_income == 0:
        savings_percentage = 0
    else:
        savings_percentage = remainder / monthly_income * 100

    # savings_percentage = remainder / monthly_income * 100
    annual_income = monthly_income * 12

    return (
        f"Total expenses: {monthly_expenses}\n"
        f"Remaining money: {remainder}\n"
        f"Savings percentage: {savings_percentage}\n"
        f"Annual income: {annual_income}"
    )

# print(financial_analysis(monthly_income, food, transport, miscellaneous))

def name_analysis(name):
    name = name.strip()
    username = name.lower().replace(" ", "")
    length = len(name)
    first_char = name[0]
    last_char = name[-1]
    contains_a = "a" in name
    contains_olori = "Olori" in name

    return (
        f"Name: {name}\n"
        f"Username: {username}\n"
        f"Name length: {length}\n"
        f"First character: {first_char}\n"
        f"Last character: {last_char}\n"
        f"Contains 'a': {contains_a}\n"
        f"Contains 'Olori': {contains_olori}"
    )

# print(name_analysis(name))

def language_analysis(language):
    upper = language.upper()
    lower = language.lower()
    language_length = len(language)
    start_with_py = language.startswith("Py")
    end_with_on = language.endswith("on")

    return (
        f"Language: {language}\n"
        f"Uppercase: {upper}\n"
        f"Lowercase: {lower}\n"
        f"Length: {language_length}\n"
        f"Starts with 'Py': {start_with_py}\n"
        f"Ends with 'on': {end_with_on}"
    )

def validate_profile(name, age, language):
    names = name.split()
    word = len(names)
    words = word >= 2
    ages = age >= 18 and age <= 100
    lang = language[0].isupper()
    valid = words and ages and lang

    return f"Valid: {valid}"

financial_report = financial_analysis(monthly_income, food, transport, miscellaneous)
name_report = name_analysis(name)
language_report = language_analysis(language)
validation_report = validate_profile(name, age, language)

def profile(name, age, language, name_report, language_report, financial_report, validation_report):
    return (
        f"========================================\n"
        f"PERSONAL PROFILE ANALYZER\n"
        f"========================================\n \n"
        f"PROFILE\n"
        f"----------------------------------------\n"
        f"Name: {name}\n Age: {age}\n Language: {language}\n \n"
        f"NAME ANALYSIS\n"
        f"----------------------------------------\n"
        f"{name_report}\n \n"
        f"LANGUAGE ANALYSIS\n"
        f"----------------------------------------\n"
        f"{language_report}\n \n"
        f"FINANCIAL ANALYSIS\n"
        f"----------------------------------------\n"
        f"{financial_report}\n \n"
        f"PROFILE STATUS\n"
        f"----------------------------------------\n"
        f"{validation_report}"
    )

print(profile(name, age, language, name_report, language_report, financial_report, validation_report))