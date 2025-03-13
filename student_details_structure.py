# students.py

# List of students (dictionaries)
students = [
    {
        'first_name': 'Tommy',
        'last_name': 'Doe',
        'index_number': '2023456',
        'nationality': 'American',
        'starting_date': '2025-03-01',
        'courses': ['Mathematics', 'Computer Science', 'Physics']
    },
    {
        'first_name': 'Janeth',
        'last_name': 'Smith',
        'index_number': '2023457',
        'nationality': 'turkish',
        'starting_date': '2025-02-15',
        'courses': ['Biology', 'Chemistry', 'Mathematics']
    },
    {
        'first_name': 'Alex',
        'last_name': 'Johnson',
        'index_number': '2023458',
        'nationality': 'Canadian',
        'starting_date': '2025-03-10',
        'courses': ['Physics', 'Computer Science', 'Economics']
    }
]

# Loop to display each student's name and index number
for student in students:
    print(f"Student's Name: {student['first_name']} {student['last_name']}")
    print(f"Index Number: {student['index_number']}\n")
