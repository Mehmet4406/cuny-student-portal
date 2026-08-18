from utils import get_int_input
from data_manager import save_data , load_data
from courses import calculate_gpa , grade_points , view_transcript , view_course_list_admin , create_course ,delete_course


admins = load_data("data/admins.json")

def admin_login(): #login menu function for admins#

    while True:
    
        admin_email = input("Please enter your email: ")
        admin_password = input("Please enter your password: ")

        for admin_id, admin_info in admins.items():

            if admin_info["email"] == admin_email and admin_info["password"] == admin_password:
                return admin_id , admin_info
            
        
        print("Email or password is incorrect. Please try again.")

            



def admin_view_student():  #view student menu function for admins#
    students_data = load_data("data/students.json")

    while True:
        student_id = input("Please enter student ID: ").upper().strip()

        if student_id not in students_data:
            print("This student does not exist.")
            continue

        student_info = students_data[student_id]

        
        while True:

            print(f"\nStudent ID: {student_id}")
            print(f"Name: {student_info['name']}")
            print(f"Last Name: {student_info['lastname']}")
            print(f"Email: {student_info['email']}")
            print(f"Major: {student_info['major']}")
            print(f"GPA: {student_info['gpa']}")
            print(f"Enrolled Courses: {student_info['enrolled_courses']}")


            print("\n1. Manage Student")
            print("2. View another Student")
            print("3. Back to Admin Menu")

            view_student_option = get_int_input("\nPlease select an option: ")

            if view_student_option == 1:

                while True:

                    print("\n1. Assign or Update Major")
                    print("2. Assign or Update Grades")
                    print("3. View Transcript")
                    print("4. Back to Student Details")

                    manage_student_option = get_int_input("\nPlease select an option: ")

                    if manage_student_option == 1:
                        assign_major(student_id , student_info , students_data)
                        break

                    elif manage_student_option == 2:
                        assign_grade(student_id , student_info , students_data)
                        break 

                    elif manage_student_option == 3:
                        view_transcript(student_info)
                        break

                    elif manage_student_option == 4:
                        break

                    else:
                        print("Please select a valid option.")

                

            elif view_student_option == 2:
                break 

            elif view_student_option == 3:
                return

            else:
                print("\nPlease select a valid option.")


def assign_major(student_id , student_info , students_data):

    majors = [
    "Computer Science",
    "Business Administration",
    "Mathematics",
    "Economics",
    "Psychology",
    "Liberal Arts"
]

    print("\nAvailable Majors: ")

    for index, major in enumerate(majors , start = 1):
        print(f"{index}. {major}")


    while True:

        major_option = get_int_input("Please select a major: ")

        if major_option < 1 or major_option > len(majors):
            print("Please select a valid major.")
            continue

        new_major = majors[major_option - 1]

        student_info["major"] = new_major
        students_data[student_id] = student_info

        save_data("data/students.json" , students_data)

        print(f"{student_info['name']} {student_info['lastname']}'s major successfully updated to {new_major}.")

        break 


def assign_grade(student_id , student_info , students_data):

    if not student_info["enrolled_courses"]:
        print("This student is not enrolled to any class. ")
        return

    for course_code in student_info["enrolled_courses"]:
        print(course_code)

    while True:
        course_code = input("Please enter the course code you want to grade: ").upper().strip()

        if course_code not in student_info["enrolled_courses"]:
            print(f"{student_info['name']} {student_info['lastname']} is not enrolled in {course_code}")
            continue
        break 


    while True:

        grade = input("Please enter the grade: ").upper().strip()

        if grade not in grade_points:
            print("Please enter a valid grade. ")
            continue
        break 

    student_info["grades"][course_code] = grade
    student_info["gpa"] = calculate_gpa(student_info)
    students_data[student_id] = student_info
    save_data("data/students.json" , students_data)

    print(f"{student_info['name']} {student_info['lastname']}'s grade successfully updated to {grade}.")


def manage_courses_admin():

    while True:

        print("1. View Classes")
        print("2. Create a New Class")
        print("3. Delete a Classs")
        print("4. Back")

        manage_courses_admin_option = get_int_input("Please select your operation: ")

        if manage_courses_admin_option == 1:
            view_course_list_admin() 

        elif manage_courses_admin_option == 2:
            create_course()

        elif manage_courses_admin_option == 3:
            delete_course() 

        elif manage_courses_admin_option == 4: 
            break 

        else:
            print("Please select a valid option.")
            