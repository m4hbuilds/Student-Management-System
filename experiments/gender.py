
def Gender(genders):
    if genders not in ["M", "F"]:
        print(f"Invalid input. Please enter 'M' for Male or 'F' for Female  \n{genders}\n")
        print("Invalid genders are: ",len(genders))
    else:
        if genders == "M":
            boys.append(genders)
        else:
            girls.append(genders)
            
girls=[]
boys=[]
Gender("G")
Gender("M")
Gender("F")
Gender("M")
Gender("M")
Gender("F")
Gender("M")
Gender("F")
Gender("M")
Gender("M")
Gender("F")
Gender("M")
print("\nBoys class:", boys)
print("\nGirls class:", girls)
print("\nTotal number of boys are: \n",len(boys),"\nTotal number of girls are: \n",len(girls))
