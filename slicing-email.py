email = input("Plese input your email :")

if "@" not in email:
    print(f"your email is not valid")
else:
    domain = email[email.index("@"):]
    username = email[:email.index("@")]


    print(f"Your username is {username} and domain is {domain}")
