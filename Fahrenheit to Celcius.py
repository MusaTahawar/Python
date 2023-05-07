print("MUSA'S FAHRENHEIT TO CELSIUS CONVERTER  ")
while (True):
    inp1 = int(input("Enter the Number\n"))
    iron = str(input("Select the unit You have entered F or C\n"))
    if (iron == "F", "f"):
        inp2 = inp1-32
        inp3 = inp2*5/9
        print(inp1, "Fahrenheit", "=", inp3, "Celsius")
    elif (iron == "C", "c"):
        inp3 = inp2*9/5
        inp2 = inp1+32
        print(inp1, "Celsius", "=", inp3, "Fahrenheit")
