name = 'Star'
age = 32
height = 1.5
is_learning = True
favorite_language = 'Python'
favorite_color = 'Green'
print('MY PROFILE')

print('Name: ', name)
print('Age: ', age)
print('Height: ', height)
print('Learning: ', is_learning)
print('Favorite Language: ', favorite_language)
print('Favorite Color: ', favorite_color)

print('Name is string: ', isinstance(name, str))
print('Age is integer: ', isinstance(age, int))
print('Height is float: ', isinstance(height, float))
print('Learning is boolean: ', isinstance(is_learning, bool))
print('Favorite language is string: ', isinstance(favorite_language, str))
print('Favorite color is string: ', isinstance(favorite_color, str))

print('First character: ', favorite_language[0])
print('Last charcter: ', favorite_language[-1])
print('First 3 characters', favorite_language[0:3])
print('Last 3 characters', favorite_language[3:])
print('Length: ', len(favorite_language))
print('Is Python in: ', "Python" in favorite_language)
print(favorite_language.startswith('P'))
print(favorite_language.endswith('n'))
print(favorite_language.find('o'))
print(favorite_language.count('o'))

descrption = " I am learning Python programming "
print(descrption.strip())
print(descrption.upper())
print(descrption.lower())
print(descrption.replace('Python', 'software development'))
print(descrption.split())
print("-".join(descrption))

