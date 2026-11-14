# Student Data — JSON Structure

## 1. Storage Location

The application currently stores student records in:

`data/students.json`

JSON is used as the project's current persistence method. The backend loads records from this file and saves changes to it.

## 2. Student Fields

| JSON key | Description | Example |
|---|---|---|
| `Register_no` | Student registration number | `DEMO001` |
| `Name` | Student name | `Sample Student` |
| `Branch` | Academic branch | `CSE` |
| `Semister` | Semester | `5` |
| `phone_no` | Contact number | `0000000000` |
| `Address` | Address | `Sample Address` |

The spelling `Semister` matches the current code field name. If the code is later changed to `Semester`, update existing JSON data and related code consistently.

## 3. Example JSON

The following is sample data for documentation only. It is not a real student record.

```json
[
  {
    "Register_no": "DEMO001",
    "Name": "Sample Student",
    "Branch": "CSE",
    "Semister": "5",
    "phone_no": "0000000000",
    "Address": "Sample Address"
  }
]
```

## 4. Data Handling Notes

- Use registration number as the main identifier for searching a student.
- Check that registration numbers are unique before inserting records.
- Store phone numbers as strings rather than numbers so formatting and leading zeros are preserved.
- Validate input before saving updates.
- Do not upload real student names, phone numbers, or addresses to a public GitHub repository.

## 5. Future Database Work

JSON is the current storage method. A relational database such as SQLite or PostgreSQL may be introduced later. If that happens, document the table structure, primary key, constraints, and migration process here.
