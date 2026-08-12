from utils import get_int_input

admins = {      
    "A001" : {
        "name" : "Mehmet" , 
        "email" : "mehmet@cuny.edu" ,
        "password" : "2005" , 
   } ,

    "A002" : {
        "name": "Haci" ,
        "email": "haci@cuny.edu" ,
        "password" : "1976" ,
    } , 

    "A003" : {
        "name" : "Gur" ,
        "email" : "gur@cuny.edu" ,
        "password" : "1975" , 
    }
}

def admin_login(): #login menu function for admins#

    while True:
    
        admin_email = input("Please enter your email: ")
        admin_password = input("Please enter your password: ")

        for admin_id, admin_info in admins.items():

            if admin_info["email"] == admin_email and admin_info["password"] == admin_password:
                return admin_id , admin_info
            
        
        print("Email or password is incorrect. Please try again.")

            



