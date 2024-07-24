#First we initialize Dictionary
student_grade ={
}
#function for add new student
def add_student(name ,grade):
    student_grade[name] = grade
    print(f"Added {name} with grade is {grade}")

#function for update student grade
def update_date(name , grade):
    if name in student_grade:
        student_grade[name] = grade
        print(f"The {name} is updated to {grade}")
    else:
        print("The student name is not found")

#function for deleting name of student
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f"The student {name} is succesfully Deleted")
    else:
        print(f"The student with {name} is not present in this system")

#view all student in dictionary
def display_all():
    if student_grade:
        for name , grade in student_grade.items():
            print(f"{name} : {grade}")
    else:
        print("The list is empty.")
#for checking the Grade of Student
def check_grade():
    if student_grade:
        for name , grade in student_grade.items():
            Absolute_grade = int(grade)
            if Absolute_grade >= 80 :
                print(f"{name} with {grade} is obtained A grade")
            elif Absolute_grade >= 60 :
                print(f"{name} with {grade} is obtained B or B+ grade")
            elif Absolute_grade >= 50 :
                print(f"{name} with {grade} is obtained C or C+ grade")
            else :
                print(f"{name} with {grade} is fail this time better luck for next time")
                
def main():
    while True:
        print("\n Student Grade Management System\n")
        print("1. Add Student ")
        print("2. Update Student ")
        print("3. Delete Student ")
        print("4. View Student")
        print("5. Check Grade of Student")
        print("6. Exit ")
        choice = int(input("Enter your choice = "))
        if choice == 1 :
            name = input("Enter the name of Student =  ")
            grade = input("Enter the Grade of Student = ")
            add_student(name, grade)
            print("Student name is succesfully added.")
        elif choice == 2 :
            name = input("Enter the name of Student that you want to update = ")
            grade = input("Enter the updated Grade of Student = ")
            update_date(name , grade)
        elif choice == 3 :
            name = input("Enter the name of Student that you want to Delete = ")
            delete_student(name)
        elif choice == 4 :
            display_all()
        elif choice == 5 :
            check_grade()
        elif choice == 6 :
            print("Thanks for using this Program")
            break
        else:
            print("Invalid Choice")
main()
