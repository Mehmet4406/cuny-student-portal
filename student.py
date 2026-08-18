from utils import get_int_input
from courses import create_course , view_course_list_admin , view_course_list_student , enroll_course , courses ,drop_course 
from data_manager import save_data , load_data 



def student_register(): #register menu function for students#

    students_data = load_data("data/students.json")

    register_name = input("Please enter your first name: ").strip()
    register_lastname = input("Please enter your last name: ").strip()
    register_email = input("Please enter your email: ").strip().lower()
    register_password = input("Please enter your password: ")
    register_password_confirm = input("Please enter your password one more time to confirm: ")

    if register_password != register_password_confirm:
         print("Passwords do not match.")
         return 

    for student_info in students_data.values():
         if student_info["email"].lower().strip() == register_email:
              print("This email is already in use.")
              return 

    new_student_id = generate_student_id(students_data)

    students_data[new_student_id] = {
         "name" : register_name ,
         "lastname" : register_lastname ,
         "email" : register_email , 
         "password" : register_password , 
         "major" : "Undeclared" ,
         "gpa" : 0.0 ,
         "enrolled_courses" : [] ,
         "grades" : {}
    }

    save_data("data/students.json" , students_data)

    print("Registration is successful!")
    print(f"Your student ID is {new_student_id}")


def generate_student_id(students_data): #student id generator function#

        highest_student_number = 0 

        for student_id in students_data:
            student_number = int(student_id[1:])     #"1:" is used to skip the index 0 so we don't pull "S"#

            if student_number > highest_student_number:
                highest_student_number = student_number 

        new_student_number = highest_student_number + 1 
        new_student_id = f"S{new_student_number:03d}" #"03d" is used to make new student number at least 3 digits#
        return new_student_id 

            
def student_login(): #login menu function for students#

    students_data = load_data("data/students.json") 

    while True:

        student_email = input("Please enter your email: ").strip().lower()
        student_password = input("Please enter your password: ")

        for student_id, student_info in students_data.items():
            if student_info["email"].strip().lower() == student_email and student_info["password"] == student_password:
                return student_id , student_info

        
        print("Email or password is incorrect. Please try again.")
            

def manage_courses_student(student_id , student_info): #course management menu function for students#

    while True: 

        print("\n1. View Classes")
        print("2. View Enrolled Classes")
        print("3. Back")
        
        manage_classes_student_option = get_int_input("\nPlease select your operation: ")

        if manage_classes_student_option == 1:
            view_course_list_student(student_id , student_info)
        

        elif manage_classes_student_option == 2:
            view_enrolled_classes(student_id , student_info)
            
        
        elif manage_classes_student_option == 3:
            break
        
        
        else: 
            print("Please select a valid option")


def view_enrolled_classes(student_id , student_info): #view enrolled classes menu function for students#

    if not student_info["enrolled_courses"]:
        print("\nYou are not enrolled in any classes.")
        return

    for course_code in student_info["enrolled_courses"]:
         course_info = courses[course_code]

         print(f"\n{course_info['code']} - {course_info['name']} - {course_info['credits']} Credits") 

    print("\n1. Manage Enrolled Courses")
    print("2. Back")

    enrolled_classes_operation = get_int_input("\nPlease select your operation: ")

    if enrolled_classes_operation == 1: 

        while True:

            select_course_manage = input("Please enter the course code: ").upper().strip()

            if select_course_manage not in student_info["enrolled_courses"]:
                print("You are not enrolled in this class.")
                continue

            else:
                course_info = courses[select_course_manage]

                print(f"\n{course_info['code']}")
                print(f"{course_info['name']}")
                print(f"{course_info['credits']} Credits")
                break 

        while True:

            print("\n1. Drop This Class")
            print("2. Cancel")

            drop_cancel_operation = get_int_input("\nPlease select your operation: ")

            if drop_cancel_operation == 1:

                while True:

                    drop_confirmation = input("Please type 'DROP' to drop the class or type 'CANCEL' to cancel: ").upper().strip()

                    if drop_confirmation == "DROP":
                        drop_course(select_course_manage , student_id , student_info)
                        return 


                    elif drop_confirmation == "CANCEL":
                        break 

                    else:
                        print("Please select a valid option.")

            elif drop_cancel_operation == 2:
                break 

            else:
                print("Please select a valid option: ")



    elif enrolled_classes_operation == 2: 
        print("You have been directed to Manage Classes Menu") 

    else:
        print("Please select a valid option.")


def student_profile(student_id , student_info):

    print(f"\nStudent ID: {student_id}")
    print(f"Name: {student_info['name']}")
    print(f"Last Name: {student_info['lastname']}")
    print(f"Email: {student_info['email']}")
    print(f"Major: {student_info['major']}")
    print(f"GPA: {student_info['gpa']}")
    print(f"Enrolled Courses: {student_info['enrolled_courses']}")


    
