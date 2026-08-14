from utils import get_int_input
from courses import create_course , view_course_list_admin , view_course_list_student , enroll_course
from data_manager import save_data , load_data 

students = load_data("data/students.json")

def student_register(): #register menu function for students#
    register_name = input("Please enter your first name: ").strip()
    register_lastname = input("Please enter your last name: ").strip()
    register_email = input("Please enter your email: ").strip().lower()
    register_password = input("Please enter your password: ")
    register_password_confirm = input("Please enter your password one more time to confirm: ")

    if register_password != register_password_confirm:
         print("Passwords do not match.")
         return 

    for student_info in students.values():
         if student_info["email"].lower().strip() == register_email:
              print("This email is already in use.")
              return 

    new_student_id = generate_student_id()

    students[new_student_id] = {
         "name" : register_name ,
         "lastname" : register_lastname ,
         "email" : register_email , 
         "password" : register_password , 
         "major" : "Undeclared" ,
         "gpa" : 0.0 ,
         "enrolled_courses" : []
    }

    save_data("data/students.json" , students)

    print("Registration is successful!")
    print(f"Your student ID is {new_student_id}")


def generate_student_id(): #student id generator function#

        highest_student_number = 0 

        for student_id in students:
            student_number = int(student_id[1:])     #"1:" is used to skip the index 0 so we don't pull "S"#

            if student_number > highest_student_number:
                highest_student_number = student_number 

        new_student_number = highest_student_number + 1 
        new_student_id = f"S{new_student_number:03d}" #"03d" is used to make new student number at least 3 digits#
        return new_student_id 

        
         
         




def student_login(): #login menu function for students#

    while True:

        student_email = input("Please enter your email: ")
        student_password = input("Please enter your password: ")

        for student_id, student_info in students.items():
            if student_info["email"] == student_email and student_info["password"] == student_password:
                return student_id , student_info

        
        print("Email or password is incorrect. Please try again.")
            



def manage_courses_student(student_id , student_info): #course management menu function for students#

    while True: 

        print("\n1. View Classes")
        print("2. View Enrolled Classes")
        print("3. Back")
        
        manage_classes_student_option = get_int_input("Please select your operation: ")

        if manage_classes_student_option == 1:
        
                    view_course_list_student(student_id , student_info)
        
                    
                

        elif manage_classes_student_option == 2:
            pass
            
        
        elif manage_classes_student_option == 3:
            break
        
        
        else: 
            print("Please select a valid option")

    
