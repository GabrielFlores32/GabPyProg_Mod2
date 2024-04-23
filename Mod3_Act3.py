def read_students_gwa(file_name):
    students = []
    with open("students_gwa.txt", 'r') as f:
        for line in f:
            name, gwa = line.strip().split()
            students.append((name, float(gwa)))
    return students

def find_max_gwa(students):
    max_gwa = max(s[1] for s in students)
    max_gwa_students = [s for s in students if s[1] == max_gwa]
    if len(max_gwa_students) == 1:
        return max_gwa_students[0]
    else:
        max_gwa_students.sort(key=lambda x: x[0])
        return max_gwa_students[-1]

students = read_students_gwa('students.txt')
max_gwa_student = find_max_gwa(students)

print(f"The student with the highest GWA is {max_gwa_student[0]} with a GWA of {max_gwa_student[1]}")