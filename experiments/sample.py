students = []
            

def insert( Register_no, Name, Gender, Branch, Semister, phone_no, Address):
    student = {
        "Register_no": Register_no,
        "Name": Name,
        "Gender":Gender,
        "Branch": Branch,
        "Semister": Semister,
        "phone_no": phone_no,
        "Address": Address
    }

    students.append(student)

    print("Student details inserted successfully")


def view_student_details(students):

    if not students:
        print("No student records found")
        return

    for s in students:
        print(f"Register Number: {s['Register_no']}")
        print(f"Name: {s['Name']}")
        print(f"Gender:{s['Gender']}")
        print(f"Branch: {s['Branch']}")
        print(f"Semester: {s['Semister']}")
        print(f"Phone Number: {s['phone_no']}")
        print(f"Address: {s['Address']}")


def search():

    Enter_regi_no = input("Enter the register number: ")

    found = False

    for s in students:

        if s["Register_no"] == Enter_regi_no:
            print(f"Register Number: {s['Register_no']}")
            print(f"Name: {s['Name']}")
            print(f"Gender:{s['Gender']}")
            print(f"Branch: {s['Branch']}")
            print(f"Semester: {s['Semister']}")
            print(f"Phone Number: {s['phone_no']}")
            print(f"Address: {s['Address']}")

            found = True
            break

    if not found:
        print("Student details not found")
def update(Register_no, new_Register_no, new_name, new_Branch, new_Semister, new_phone_no, new_Address):
    for s in students:
        if s["Register_no"] == Register_no:
            s["Register_no"] = new_Register_no
            s["Name"] = new_name
            print(f"Gender:{s['Gender']}")
            s["Branch"] = new_Branch
            s["Semister"] = new_Semister
            s["phone_no"] = new_phone_no
            s["Address"] = new_Address
            print("Student details updated successfully")
            return
    print("Student details not found")

def delete(Register_no):
    for s in students:
        if s ["Register_no"] == Register_no:
            students.remove(s)
            print("Student details deleted successfully")
            return
    print("Student details not found")

options = {
    "1": insert,
    "2": view_student_details,
    "3": search,
    "4": update,
    "5": delete
}

    
while True:
        print("\nStudent Management System")
        print("1. Insert Student Details")
        print("2. View Student Details")
        print("3. Search Student Details")
        print("4. Update Student Details")
        print("5. Delete Student Details")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            Register_no = input("Enter Register Number: ")
            Name = input("Enter Name: ")
            Gender =input(str("Enter Your gender M/F: "))
            Branch = input("Enter Branch: ")
            Semister = input("Enter Semester: ")
            phone_no = input("Enter Phone Number: ")
            Address = input("Enter Address: ")
            insert(Register_no, Name, Gender, Branch, Semister, phone_no, Address)

        elif choice == "2":
            view_student_details(students)

        elif choice == "3":
            search()

        elif choice == "4":
            Register_no = input("Enter Register Number to update: ")
            new_Register_no = input("Enter new Register Number: ")
            new_name = input("Enter new Name: ")
            new_gender=input(str("Enter new Gender M/F: "))
            new_Branch = input("Enter new Branch: ")
            new_Semister = input("Enter new Semester: ")
            new_phone_no = input("Enter new Phone Number: ")
            new_Address = input("Enter new Address: ")
            update(Register_no, new_Register_no, new_name, new_Branch, new_Semister, new_phone_no, new_Address)

        elif choice == "5":
            Register_no = input("Enter Register Number to delete: ")
            delete(Register_no)

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

