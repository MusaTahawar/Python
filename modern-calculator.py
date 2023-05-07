
while (True):
    try:
        user_input = eval(input("Enter the Expression \n"))
        print("=", user_input)
    except Exception:
        print("Error")
