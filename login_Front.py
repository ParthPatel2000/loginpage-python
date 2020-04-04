import loginback

print('/**********welcome**************/')
print('/          1.Login              /')
print('/          2.Signup             /')
print('/       3.change password        /')
print('/*******************************/')
sel = int(input())
if sel is 1:

    usrnm = input("Enter the username")
    passwd = input("Enter the password")
    status = loginback.login(usrnm, passwd)
    if status is False:
        print("Wrong username or password was entered please check credentials")

elif sel is 2:
    usrnm = input("Enter the username")
    pass1 = input("Enter the password")
    pass2 = input("Renter the password")
    while pass1 != pass2:
        print("passwords dont match")
        pass2 = input("Renter the password")
    passwd = pass1
    loginback.signup(usrnm, passwd)

elif sel is 3:
    usrnm = input("Enter the username")
    passwd = input("Enter the password")
    loginback.changepass(usrnm, passwd)
