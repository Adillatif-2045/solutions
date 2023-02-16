#for total no of students in class

print("Enter Total no of students in class ")
total_student = input()
print("Total students are:  " + total_student)

#for math students
print("Enter no of students with mathematics ")
math_students = input()
print(" Math students are: " + math_students)

#for bio students
print("Enter no of students with bio ")
bio_students = input()
print("Bio students are: " + bio_students)

#for math and bio students
math_and_bio = int(math_students) + int(bio_students)

#for students with out math and bio
students_with_out_math_and_bio = int(total_student) - int(math_and_bio)

print("students with out math and bio are :" + str(students_with_out_math_and_bio))

print("students with math and bio are:  " + str(math_and_bio))

#end of the code









