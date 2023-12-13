adb = {
    "user": "password",
    "Admin": "Admin",
}

def intro():
    intro_text = "Welcome to Messy CLI\n" \
                 "Please Register OR Login\n" \
                 "1. Login\n" \
                 "2. Register\n" \
                 "3. Quit\n"
    print(intro_text)
    return input("==> ")

def clear():
    i = 0
    while i < 30:
        print("\n")
        i += 1

def auth(user, pswd, adb):
    for key in adb:
        if key == user and adb[key] == pswd:
            return True
    return False

def reg(adb):
    user = input("Please Enter username\n==> ")
    try:
        if auth(user, adb[user], adb):
            print("User already exists")
    except KeyError:
        pswd = input("Please Enter The password\n==> ")
        adb[user] = pswd
        print("Registered")

while True:
    choice = intro()

    if choice == "1":
        clear()
        user = input("Please Enter Your Username\n==> ")
        pswd = input("Please Enter Your Password\n==> ")
        if auth(user, pswd, adb):
            print("Welcome", user)
            break
        else:
            print("Wrong Login")

    elif choice == "2":
        clear()
        reg(adb)

    elif choice == "3":
        print("ByeBye")
        break

    else:
        print("Wrong Pick")