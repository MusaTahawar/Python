user_name = str(input("Enter Your Name\n"))
user_mail = str(input("Enter You Email\n"))
user_password = str(input("Enter You Password\n"))
user_phonenumber = int(input("Enter You Phone Number\n"))
if user_name:
    f = open(user_name + ".txt", "a")
    f.write(user_name), "\n"
    f.write(user_mail), "\n"
    f.write(user_password), "\n"
    f.write(user_phonenumber), "\n"
else:
    print("Sorry Phone Number dose not accept string")
