from utils import get_int_input
from data_manager import save_data , load_data

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
                    print("3. Back to Student Details")

                    manage_student_option = get_int_input("\nPlease select an option: ")

                    if manage_student_option == 1:
                        assign_major(student_id , student_info , students_data)

                    elif manage_student_option == 2:
                        pass 

                    elif manage_student_option == 3:
                        break

                

            elif view_student_option == 2:
                break 

            elif view_student_option == 3:
                return

            else:
                print("\nPlease select a valid option.")


def assign_major(student_id , student_info , students_data):

    new_major = input("Please enter the student's new major: ")

    if not new_major:
        print("Major can not be empty")
        return

    student_info["major"] = new_major
    students_data[student_id] = student_info

    save_data("data/students'json" , students_data)

    print(f"{student_info['name']} {student_info['lastname']}'s major successfully updated to {new_major}.")