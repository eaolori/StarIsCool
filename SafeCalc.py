def safe_calculator(a, operator, b):
    operators = {
        "+": a + b,
        "-": a - b,
        "*": a * b,
        "**": a ** b
    }

    if operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return round(a / b, 2)

    if operator == "%":
        if b == 0:
            return "Cannot divide by 0"
        return a % b

    return operators.get(operator, "Invalid operator")



# def safe_calculator(a, operator, b):
#     result = None

#     if operator == "+":
#         result = a + b
#     elif operator == "-":
#         result = a - b
#     elif operator == "*":
#         result = a * b
#     elif operator == "**":
#         result = a ** b
#     elif operator == "/":
#         if b == 0:
#             return "Cannot divide by zero"
#         result = round(a / b, 2)
#     elif operator == "%":
#         if b == 0:
#             return "Cannot divide by zero"
#         result = a % b
#     else:
#         result = "Invalid operator"
    
#     return result

print(safe_calculator(10, "+", 5))
print(safe_calculator(10, "-", 5))
print(safe_calculator(10, "*", 5))
print(safe_calculator(10, "/", 4))
print(safe_calculator(10, "%", 3))
print(safe_calculator(2, "**", 3))
print(safe_calculator(10, "/", 0))
print(safe_calculator(10, "@", 5))