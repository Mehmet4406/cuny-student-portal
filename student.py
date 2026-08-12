from utils import get_int_input
from courses import create_course , view_course_list_admin , view_course_list_student , enroll_course
from data_manager import save_data , load_data 

students = load_data("data/students.json")

def student_register(): #register menu function for students#
    register_name = input("Please enter your first name: ").strip()
    register_lastname = input("Please enter your last name: ").strip()
    register_email = input("Please enter your email").strip().lower()
    register_password = input("Please enter your password: ")
    register_password_confirm = input("Please enter your password one more time to confirm: ")




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

    
