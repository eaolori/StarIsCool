def analyze_username(name):
    # name = input("What is your full name")
    name = name.strip()
    username = name.lower().replace(" ", "")
    username_len = len(username)
    first_char = username[0]
    last_char = username[-1]
    letter_a = "a" in username

    return(
        f"Username: {username}\n"
        f"Length: {username_len}\n"
        f"First character: {first_char}\n"
        f"Last character: {last_char}\n"
        f"Contains 'a': {letter_a}"
    )

print(analyze_username("  Esther Olori  "))
# print(analyze_username("Star is cool"))
