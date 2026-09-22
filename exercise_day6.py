# 1. greet(name)
#    → returns "Hello, [name]!"

# 2. calculate_age(birth_year)
#    → returns the person's approximate age
#    → use 2026 as the current year

# 3. calculate_total(price, quantity=1)
#    → returns price × quantity
#    → quantity should default to 1

name = input("What is your name? ")
#1
def greet(name):
    return (f"Hello, {name}!")

result = greet("Star")
print(result)

#2
def calculate_age(birth_year):
    current_year = 2026
    return current_year - birth_year

result = calculate_age(1997)
print(f"Approximate age: {result}")

#3
def calculate_total(price, quantity=1):
    return price * quantity

result = calculate_total(1000)
print(result)