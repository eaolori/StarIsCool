#Exercise 4
age = 25
print(age > 18)
print(age < 18)
print(age == 25)
print(age != 30)
print(age >=25)
print(age <= 20)

#5
username = "Star"
password = "python123"
entered_username = "Star"
entered_password = "python123"
if entered_username == username and entered_password == password:
    print('Login successful')
else:
    print('Invalid username or password')

#6
age = 70
if age < 13:
    print('Child')
elif age >= 13 and age <= 17:
    print("Teenager")
elif age >= 18 and age <= 64:
    print('Adult')
else:
    print('Senior')

#7
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("You can enter")
    else:
        print("You need an ID")
else:
    print('You are too young')

#8
temperature = 30
if temperature >= 30:
    print('Hot')
elif temperature >= 20:
    print('Warm')
elif temperature >= 10:
    print('Cool')
else:
    print('Cold')

#9
age = 20
has_id = True
is_banned = False
if age >= 18 and has_id and not is_banned:
    print('Access granted')
else:
    print('Access denied')

#10
score = 85
attendance = 90
if attendance < 75:
    print('Fail')
else:
    if score >= 90:
        print('A')
    elif score >= 80:
        print('B')
    elif score >= 70:
        print('C')
    elif score >= 60:
        print('D')
    else:
        print('F')

#Rough
name = "Esthe"
age = 25
height = 1.75
is_learning = True
print(name, age, height, is_learning)
print(type(name), '\n', type(age), '\n', type(height), '\n', type(is_learning))
print(isinstance(name, str), isinstance(age, int), isinstance(height, float), isinstance(is_learning, bool))
