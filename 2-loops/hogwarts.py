"PRINT LIST of STUDENTS one by one"

students = ["deegii", "baagii", "orgil"]

# 1===========================================
for student in students:
    print(student)

# 2===========================================
for i in range(len(students)):
    print(i + 1 ,students[i])

"PRINT DICT of STUDENTS one by one"

studentsObjects = {
    "deegii": "tennis",
    "baagii": "tennis",
    "orgil": "basketball",
}

for studentObject in studentsObjects:
    print(studentObject, studentsObjects[studentObject], sep=", ")


"PRINT LIST_DICT combo"

students_list_dict = [
    {"name": "orgil", "sport": "basketball", "major": "cs"},
    {"name": "deegii", "sport": "tennis", "major": "business"},
    {"name": "baagii", "sport": "tennis", "major": None}
]

for student_list_dict in students_list_dict:
    print(student_list_dict["name"], student_list_dict["major"], sep=": ")