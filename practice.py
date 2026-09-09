# Practice


# return the square of a number
def square(a):
    return a ** 2
print(square(3))

# return the cube of a number
def cube(a):
    return a ** 3
print(cube(4))

# return the sum of two numbers
def sum(a, b):
    return a + b
print(sum(2, 4))

# return the larger of two numbers
def maximum(a, b):
    return max(a, b)
print(maximum(23, 4))

#or

def max(a, b):
    if a > b:
        return a
    else:
        return b
print(max(34,50))

person = {
    "name": "Esther",
    "age": 25,
    "country": "Nigeria"
}
print(person.get("name", "No name"))
print(person.get("age", "No age"))
print(person.get("country", "No country"))