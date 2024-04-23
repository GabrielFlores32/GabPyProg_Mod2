#create a file.txt that contains students name and gwa in a file.txt
#the output must show the name of the student with the highest gwa together with its   

def find_highest_gwa():
    with open("students_gwa.txt", "r") as grade_file:
        data = grade_file.read()
        students_list = eval(data)
        highest_gwa = None
        highest_gwa_student = None
        for name, gwa in students_list.items():
            float_value = float(gwa)
            if highest_gwa is None or float_value < float(highest_gwa):
                highest_gwa_student = name
                highest_gwa = gwa
        return highest_gwa_student, highest_gwa
name, gwa = find_highest_gwa()
print (f"{name} has the highest GWA with {gwa}")
