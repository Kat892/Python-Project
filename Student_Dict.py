student_name=input("Enter student's name: ")
student_marks={'Karthik':100,'Alice':85,'Jimmy':90,'Rocky':95}
if student_name in student_marks:
    print(student_name+"'s marks: ",student_marks[student_name])
else:
    print("Student not found.")
