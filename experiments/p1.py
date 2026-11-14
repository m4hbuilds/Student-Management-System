name=str(input("Enter your name: "))
if name=="" or len(name)<8:
    print("You didn't enter a valid name.")
else:
    print("Hello, " + name + "!")