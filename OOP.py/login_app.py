username = str(input("Username : "))
password = str(input("Password : "))

if len(username) > 1 and len(password) > 1:
    print('Account created .')
    print('Login now')
else:
    print('Account not created')

username2 = str(input("Username : "))
password2 = str(input("Password : "))

if username2 == username and password == password2:
    print("Login succesful")
else:
    print("Login unsuccesful")
