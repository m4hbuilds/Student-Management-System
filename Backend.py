import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent / "data" / "students.json"
students = []


def save_data():
    """Save the current student records to the project's data file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)
    except OSError as error:
        print(f"Unable to save student details: {error}")
        return False
    return True


def load_data():
    """Load student records, treating missing or invalid data as empty."""
    global students
    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)
        if not isinstance(data, list) or any(not isinstance(item, dict) for item in data):
            raise ValueError("expected a JSON array of student records")
        students = data
    except FileNotFoundError:
        students = []
    except (json.JSONDecodeError, UnicodeDecodeError, ValueError) as error:
        students = []
        print(f"Student data is invalid; starting with no records: {error}")
    except OSError as error:
        students = []
        print(f"Unable to read student details: {error}")


def _valid_details(register_no, name, branch, semester, phone_no, address):
    fields = {
        "Register number": register_no,
        "Name": name,
        "Branch": branch,
        "Semester": semester,
        "Phone number": phone_no,
        "Address": address,
    }
    missing = [label for label, value in fields.items() if value is None or not str(value).strip()]
    if missing:
        print("Required fields cannot be empty: " + ", ".join(missing))
        return False
    return True


def _same_register_number(left, right):
    return str(left).strip() == str(right).strip()


def insert(Register_no, Name, Branch, Semister, phone_no, Address):
    if not _valid_details(Register_no, Name, Branch, Semister, phone_no, Address):
        return False
    if any(_same_register_number(s.get("Register_no", ""), Register_no) for s in students):
        print("Student with this register number already exists")
        return False

    student = {
        "Register_no": str(Register_no).strip(),
        "Name": str(Name).strip(),
        "Branch": str(Branch).strip(),
        "Semister": str(Semister).strip(),
        "phone_no": str(phone_no).strip(),
        "Address": str(Address).strip(),
    }
    students.append(student)
    if not save_data():
        students.pop()
        return False
    print("Student details inserted successfully")
    return True


def view_student_details(students):
    if not students:
        print("No student records found")
        return

    for s in students:
        print(f"Register Number: {s.get('Register_no', '')}")
        print(f"Name: {s.get('Name', '')}")
        print(f"Branch: {s.get('Branch', '')}")
        print(f"Semester: {s.get('Semister', '')}")
        print(f"Phone Number: {s.get('phone_no', '')}")
        print(f"Address: {s.get('Address', '')}")


def search():
    enter_regi_no = input("Enter the register number: ").strip()
    for s in students:
        if _same_register_number(s.get("Register_no", ""), enter_regi_no):
            print(f"Register Number: {s.get('Register_no', '')}")
            print(f"Name: {s.get('Name', '')}")
            print(f"Branch: {s.get('Branch', '')}")
            print(f"Semester: {s.get('Semister', '')}")
            print(f"Phone Number: {s.get('phone_no', '')}")
            print(f"Address: {s.get('Address', '')}")
            return
    print("Student details not found")


def update(Register_no, new_Register_no, new_name, new_Branch, new_Semister, new_phone_no, new_Address):
    record = next(
        (s for s in students if _same_register_number(s.get("Register_no", ""), Register_no)),
        None,
    )
    if record is None:
        print("Student details not found")
        return False
    if not _valid_details(new_Register_no, new_name, new_Branch, new_Semister, new_phone_no, new_Address):
        return False
    if any(
        s is not record and _same_register_number(s.get("Register_no", ""), new_Register_no)
        for s in students
    ):
        print("Student with this register number already exists")
        return False

    updated = {
        "Register_no": str(new_Register_no).strip(),
        "Name": str(new_name).strip(),
        "Branch": str(new_Branch).strip(),
        "Semister": str(new_Semister).strip(),
        "phone_no": str(new_phone_no).strip(),
        "Address": str(new_Address).strip(),
    }
    previous = record.copy()
    record.clear()
    record.update(updated)
    if not save_data():
        record.clear()
        record.update(previous)
        return False
    print("Student details updated successfully")
    return True


def delete(Register_no):
    for index, student in enumerate(students):
        if _same_register_number(student.get("Register_no", ""), Register_no):
            deleted = students.pop(index)
            if not save_data():
                students.insert(index, deleted)
                return False
            print("Student details deleted successfully")
            return True
    print("Student details not found")
    return False


load_data()
