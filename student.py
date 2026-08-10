students = {
    "S001" : {
        "name" : "Ayberk" , 
        "email" : "ayberk@cuny.edu" ,
        "password" : "2005" , 
        "major" : "Computer Science" ,
        "gpa" : 0.0 ,
        "enrolled_courses" : []
   } ,

    "S002" : {
        "name": "Osman" ,
        "email": "osman@cuny.edu" ,
        "password" : "1976" ,
        "major" : "business" , 
        "gpa" : 0.0 , 
        "enrolled_courses" : []
    } , 

    "S003" : {
        "name" : "Emine" ,
        "email" : "emine@cuny.edu" ,
        "password" : "1975" , 
        "major" : "Sociolgy" ,
        "gpa" : 0.0 , 
        "enrolled_courses" : []
    }
}

def student_login():

    while True:

        student_email = input("Please enter your email: ")
        student_password = input("Please enter your password: ")

        for student_id, student_info in students.items():
            if student_info["email"] == student_email and student_info["password"] == student_password:
                return student_id , student_info

        
        print("Email or password is incorrect. Please try again.")
            



