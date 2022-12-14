#reset username and password
global usr
global pwd
usr = "null"
pwd = "null"

#input username and password
usr = input("Username: ")
pwd = input("Password: ")


#dictionary of users
global users
users = {
  
    "admin": {
        "usr": "admin",
        "pwd": "*******"
  }, 

    "userOne": {
        "usr": "user",
        "pwd": "password"
  },
  
    "guest": {
        "usr": "guest",
        "pwd": "1234"
  }

}

#new user function
def newUser():
    print("It seems you don't have an account with us. Would you like to sign up? Y/N")
    prompt = input("").upper()
    if prompt == "Y":
        print("What will be your username?")
        input("")
        print("What will be your password?")
        input("")
        print("Great!")
    else:
        print(":(")


#check if admin
if usr in users["admin"]["usr"]:
    if pwd in users["admin"]["pwd"]:
        print("Welcome " + users["admin"]["usr"] + "!")
    else:
        print("Wrong password")
#check if user account
elif usr in users["userOne"]["usr"]:
    if pwd in users["userOne"]["pwd"]:
        print("Welcome " + users["userOne"]["usr"] + "!")
    else:
        print("Wrong password")
#check if guest
elif usr in users["guest"]["usr"]:
    if pwd in users["guest"]["pwd"]:
        print("Welcome " + users["guest"]["usr"] + "!")
    else:
        print("Wrong password")
#if nothing works run new user function
else:
    newUser();
