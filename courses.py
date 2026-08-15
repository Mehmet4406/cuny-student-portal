from utils import get_int_input
from data_manager import save_data , load_data 

grade_points = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.7,
    "B+": 3.3,
    "B": 3.0,
    "B-": 2.7,
    "C+": 2.3,
    "C": 2.0,
    "C-": 1.7,
    "D+": 1.3,
    "D": 1.0,
    "D-": 0.7,
    "F": 0.0
}
 

courses = load_data("data/courses.json")

def create_course(): #class creation menu function#

    course_code = (input("\nPlease enter the class code: ")).upper().strip()
    course_name = input("Please enter the class name: ")
    course_credit = get_int_input("Please enter the amount of class credit: ")
    course_capacity = get_int_input("Please enter the class capacity: ")
    courses[course_code] = {
        "code": course_code ,
        "name":  course_name , 
        "credits":  course_credit , 
        "capacity":  course_capacity , 
        "enrolled_students":  []
    }

    save_data("data/courses.json" , courses)

    print(f"{course_code} - {course_name} added as a new class")

def enroll_course(course_code , student_id , student_info): #class enrollment function for students#
    
    if course_code not in courses:
        print("This class does not exist")
        return 

    course_info = courses[course_code]

    if course_code in student_info["enrolled_courses"]:
        print(f"You are already enrolled in {course_info['name']}")
        return

    if len(course_info["enrolled_students"]) >= course_info["capacity"]:
        print("This class is full")
        return
    
    course_info["enrolled_students"].append(student_id)
    student_info["enrolled_courses"].append(course_code)
    save_data("data/courses.json" , courses)

    students_data = load_data("data/students.json")
    students_data[student_id] = student_info
    save_data("data/students.json" , students_data)

    print(f"You have successfully enrolled in {course_code} - {course_info['name']}")
    

    
def view_course_list_admin(): #class view menu function for admins#
    if not courses: 
        print("\nThere is no existing classes")
        return

    print("\nCourse List: ")

    for course_code, course_info in courses.items():
        print(f"\n{course_code} - {course_info['name']}")
        
    
    while True:
        
        print("1. Search a class")
        print("2. Quit")
        view_class_option = get_int_input("\nPlease select your operation: ")

        while view_class_option == 1:
    
            course_input = input("\nPlease type the code of the course you want to view: ").upper().strip()

            if course_input not in courses:
                print(f"{course_input} can not find")
                continue
    
    
            else:
                
                
                course_info = courses[course_input]
                
                print(f"{course_info["code"]} - {course_info["name"]}")
                print(f"Course Credit: {course_info["credits"]}")
                print(f"Course Capacity: {course_info["capacity"]}")
                print(f"Enrolled Students: {course_info["enrolled_students"]}")

            print("1. Search another class")
            print("2. Quit")
            search_class_option = get_int_input("\nPlease select your operation: ")

            if search_class_option == 1:
                view_class_option = 1

            elif search_class_option == 2:
                view_class_option = 2
            
            else:
                print("Please select a valid option")


        if view_class_option == 2:
            break 

        else:
            print("Please select a valid option")

    return 



def view_course_list_student(student_id = None , student_info = None): #class view menu function for students #
    if not courses: 
        print("\nThere is no existing classes")
        return

    print("\nCourse List: ")

    for course_code, course_info in courses.items():
        print(f"\n{course_code} - {course_info['name']}")
        
    
    while True:
        
        
        print("1. Search a class")
        print("2. Quit")
        view_class_option = get_int_input("\nPlease select your operation: ")

        


        while view_class_option == 1:
    
            course_input = input("\nPlease type the code of the course you want to view: ").upper().strip()

            if course_input not in courses:
                print(f"{course_input} can not find")
                continue
    
    
            else:
                
                course_info = courses[course_input]

                available_seats = course_info["capacity"] - len(course_info["enrolled_students"])
                
                print(f"{course_info["code"]} - {course_info["name"]}")
                print(f"Course Credit: {course_info["credits"]}")
                print(f"Course Capacity: {course_info["capacity"]}")
                print(f"Available Seats: {available_seats}")

                
                
            print("1. Enroll in this class")
            print("2. Search another class")
            print("3. Quit")
            search_class_option = get_int_input("\nPlease select your operation: ")

            while search_class_option == 1:

                confirm_cancel_enrollment = input("Please type 'ENROLL' to confirm the enrollment or type 'CANCEL' to cancel the enrollment: ").upper().strip()
            

                if confirm_cancel_enrollment == "ENROLL":

                    if available_seats > 0:
                        enroll_course(course_input , student_id , student_info )
                        return

                    else:
                        print("This class has no available seats")
                        break   

                elif confirm_cancel_enrollment == "CANCEL":
                    print("You have successfully cancelled the enrollment and directed back to search menu")
                    break 

                else:
                    print("Please type a valid option")

            if search_class_option == 1:
                view_class_option = 1

            elif search_class_option == 2:
                view_class_option = 1 

            elif search_class_option == 3:
                view_class_option = 2 

            else:
                print("Please type a valid option")
            



        if view_class_option == 2:
            break 

        else:
            print("Please select a valid option")

    return 


def drop_course(course_code , student_id , student_info):
    if course_code not in courses:
            print("This class does not exist")
            return 
    
    course_info = courses[course_code]
    
    if course_code not in student_info["enrolled_courses"]:
            print(f"You are not enrolled in {course_info['name']}")
            return

    if student_id not in course_info["enrolled_students"]:
        print("Enrollment data is inconsistent. Please seek help from advisor.")
        return
    
        
    course_info["enrolled_students"].remove(student_id)
    student_info["enrolled_courses"].remove(course_code)
    save_data("data/courses.json" , courses)
    
    students_data = load_data("data/students.json")
    students_data[student_id] = student_info
    save_data("data/students.json" , students_data)
    
    print(f"You have successfully dropped {course_code} - {course_info['name']}")



def calculate_gpa(student_info):

    courses_data = load_data("data/courses.json")

    total_grade_points = 0 
    total_credits = 0 

    for course_code , grade in student_info["grades"].items():

        course_info = courses_data[course_code]

        credits = course_info["credits"]
        points = grade_points[grade]

        total_grade_points += points * credits 
        total_credits += credits 

    if total_credits == 0:
        return 0.0 

    gpa = total_grade_points / total_credits 

    return round(gpa , 2)

def view_transcript(student_info):

    if not student_info["grades"]:
        print("\nThere is no graded classes to create a transcript.")
        return

    courses_data = load_data("data/courses.json")

    print("-------------TRANSCRIPT-------------")

    for course_code , grade in student_info["grades"].items():

        course_info = courses_data[course_code]
        print(f"{course_code} - {course_info['name']}   -   Credits: {course_info['credits']}   -   {grade}")

    print(f"\nCumulative GPA: {student_info['gpa']}")

    





