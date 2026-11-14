# JSON Data Structure

## Current storage
Student records are currently stored in:

`data/students.json`

## Known student fields

| Key | Meaning |
|---|---|
| `Register_no` | Student registration number |
| `Name` | Student name |
| `Branch` | Academic branch |
| `Semister` | Semester (key spelling used in current code) |
| `phone_no` | Phone number |
| `Address` | Address |

## Example shape

The following is an illustrative example only. Use fake data in documentation and public repositories.

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

## Notes
- Keep registration numbers unique.
- Treat phone numbers as strings so leading zeros and formatting are preserved.
- Do not commit real student names, phone numbers, or addresses.
- If field names are changed in code, update this document and migrate existing JSON data carefully.
