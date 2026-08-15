from courses import create_course , view_course_list_admin , view_course_list_student , view_transcript
from admin import admin_login , admin_view_student , assign_grade , assign_major 
from student import student_login , manage_courses_student , student_register ,student_profile 
from utils import get_int_input



def student_menu(): #Student menu function# 
    while True:

        print("\n1. Login")
        print("2. Sign up")
        print("3. Back To Main Menu")

        student_menu_operation = get_int_input("Please select your operation: ")

        if student_menu_operation == 1:
            login_result = student_login()
            if not login_result:
                continue 

            student_id , student_info = login_result

            print(f"\nWelcome to CUNY Student Portal - {student_info['name']}")
        
            while True: 
                        
                print("\n1. View Your Profile")
                print("2. View Your Transcript")
                print("3. Manage Classes")
                print("4. Log Out")
                
                student_option = get_int_input("\nPlease select your operation: ")
        
                if student_option == 1:
                    student_profile(student_id , student_info)

                elif student_option == 2:
                    view_transcript(student_info)
        
                elif student_option == 3:
                    manage_courses_student(student_id , student_info)
        
                elif student_option == 4:
                    break

                else: 
                    print("Your operation is invalid.")
        

        elif student_menu_operation == 2:
            student_register()

        elif student_menu_operation == 3:
            break

        else:
            print("Your operation is invalid. ")
    
    
    



def admin_menu(): #Admin menu function#
        
    login_result = admin_login()

    if not login_result:
        return
    
    admin_id , admin_info = login_result 
    
   
    print(f"\nWelcome to CUNY Admin Portal - {admin_info['name']} ")

    while True:
            
        print("\n1. View Classes")
        print("2. Create a new class")
        print("3. View a Student")
        print("4. Back to Main Menu")

        admin_option = get_int_input("\nPlease select your operation: ")

        if admin_option == 1:
            view_course_list_admin()
        
        elif admin_option == 2:
            create_course()

        elif admin_option == 3:
            admin_view_student()

        elif admin_option == 4:
            break

        else:
            print("Your option is invalid")



def main_menu(): #Main menu function#

    print("Welcome to CUNY portal")   

    while True:
    
        print("\n1. Student")
        print("2. Admin")
        print("3. Quit")

        login_option = get_int_input("\nPlease select your operation: ")
    
        if login_option == 1:
            student_menu()


        elif login_option == 2:
            admin_menu()
       

        elif login_option == 3:
            break 

        else:
            print("Your option is invalid")




main_menu()        

